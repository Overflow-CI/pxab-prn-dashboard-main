import re, json, os
F='/home/user/hello-world/nc_medicaid_bh_dashboard.html'
UP='/root/.claude/uploads/91141d82-7be3-5ffc-bd0c-f501091745a6/'
t=open(F).read()

# ---- county -> plan from F1
p1=open(UP+[f for f in os.listdir(UP) if 'p1-' in f][0]).read()
j=p1.find('```json',p1.find('# perplexity response'))+7
d1=json.loads(p1[j:p1.find('\n```',j)])
cp=d1['counties']; assert len(cp)==100
abbr={'Alliance Health':'A','Trillium Health Resources':'T','Vaya Partners':'V'}

# keep existing region names/counties
m=re.search(r"const NC_REGIONS_DATA = \{",t); 
regs={}
for rm in re.finditer(r"\n      (\d): \{\n        id: \d,\n        name: '([^']+)',",t):
    regs[int(rm.group(1))]=rm.group(2)
cnt={}
for cm in re.finditer(r"\n        counties: \[([^\]]+)\]",t):
    pass
cl=re.findall(r"\n        counties: \[([^\]]+)\]",t)
assert len(regs)==6 and len(cl)==6
for i,c in enumerate(cl): cnt[i+1]=re.findall(r"'([^']+)'",c)
assert sum(len(v) for v in cnt.values())==100 and set(sum(cnt.values(),[]))==set(cp)

PLANS={
 'Alliance Health':{
  'short':'Alliance','asOf':'2026-10-18',
  'phone':'855-759-9700','phoneNote':'Provider Support Line, Mon–Sat 7am–6pm',
  'website':'https://www.alliancehealthplan.org/providers/',
  'office':'5200 W. Paramount Parkway, Suite 200, Morrisville, NC 27560',
  'umPhone':'855-759-9700 (prior authorizations); PA fax 919-651-8691',
  'umEmail':'None published. Use the phone or fax.',
  'networkEmail':'NetworkRelations@AllianceHealthPlan.org',
  'portalLabel':'Alliance Health Provider Portal (single sign-on)','portalUrl':'https://alliancehealth.okta.com/',
  'portalNote':'Portal access requests: ACSSupport@AllianceHealthPlan.org',
  'joinUrl':'https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/',
  'needsUrl':'https://www.alliancehealthplan.org/providers/network/service-needs/',
  'payerId':'23071',
  'intake':{'peer':'closed','saiop':'open','sacot':'open'},
  'note':'Decision on network need within 5 business days of a complete request, then contracting by DocuSign. "Open" means it is taking applications, not that a contract is promised.'},
 'Trillium Health Resources':{
  'short':'Trillium','asOf':'2026-10-18',
  'phone':'1-855-250-1539','phoneNote':'Provider Support Services, Mon–Sat 7am–6pm',
  'website':'https://www.trilliumhealthresources.org/',
  'office':'1019 WH Smith Blvd., Greenville, NC 27834 (mailing: PO Box 12797, Durham, NC 27709)',
  'umPhone':'1-855-250-1539 (UM fax 252-215-6875)',
  'umEmail':'None published. Use NetworkServicesSupport@TrilliumNC.org or the phone.',
  'networkEmail':'NetworkServicesSupport@TrilliumNC.org',
  'portalLabel':'Provider portals hub (Tailored Plan Provider Portal, Provider Direct)','portalUrl':'https://www.trilliumhealthresources.org/for-providers/provider-contact-information-and-portals',
  'portalNote':'Direct login addresses were not confirmed. Use the hub page.',
  'joinUrl':'https://www.trilliumhealthresources.org/contracting-information',
  'needsUrl':'https://www.trilliumhealthresources.org/current-service-needs',
  'payerId':'43072 (Tailored Plan claims from Oct 1, 2026)',
  'intake':{'peer':'closed','saiop':'open','sacot':'open'},
  'note':'Trillium lists SAIOP and SACOT needs only in Dare and Hyde counties. Ask its network team before you sign a lease elsewhere.'},
 'Vaya Partners':{
  'short':'Vaya Partners','asOf':'2026-10-18',
  'phone':'1-866-990-9712','phoneNote':'ACCESS Provider Services, Mon–Sat 7am–6pm',
  'website':'https://providers.vayapartners.org/',
  'office':'200 Ridgefield Court, Suite 218, Asheville, NC 28806; also 901 S. New Hope Road, Gastonia, NC 28054',
  'umPhone':'1-800-893-6246 ext. 1515 (behavioral health)',
  'umEmail':'UM@VayaPartners.org',
  'networkEmail':'ProviderEnrollment@VayaPartners.org (1-855-432-9139)',
  'portalLabel':'Vaya Partners Provider Portal','portalUrl':'https://providers.vayapartners.org/portal/',
  'portalNote':'Whether ProviderCONNECT is still used for dates of service after Oct 1, 2026 was not confirmed.',
  'joinUrl':'https://providers.vayapartners.org/enrollment/',
  'needsUrl':'',
  'payerId':'13010 (dates of service on or after Oct 1, 2026)',
  'intake':{'peer':'closed','saiop':'open','sacot':'open'},
  'note':'Vaya Health and Partners merged on Oct 1, 2026. No service-needs page was found, and whether it accepts new requests in the former Partners counties is not confirmed. Ask Provider Enrollment before you apply.'},
}
for p in PLANS.values(): p['intake'].setdefault('peer','closed')

HUBS={
 1:dict(name='Impact Health',contact='Tamara Smith (point of contact on the NCDHHS hub page)',phone='828-278-9900',phoneNote='Impact Health main line. No ROOTS phone is published.',email='t.smith@impacthealth.org',address='P.O. Box 5378, Asheville, NC 28813',website='https://impacthealth.org/rural-health/',serves='Region 1',note=''),
 2:dict(name='Trillium Health Resources',contact='No named contact published. Use the hub email.',phone='1-855-250-1539',phoneNote='Trillium Provider Support Services. Not a ROOTS line.',email='Region2NCRootsHub@TrilliumNC.org',address='1019 WH Smith Blvd., Greenville, NC 27834',website='https://www.trilliumhealthresources.org/NC-ROOTS-Region-2',serves='Regions 2 and 5',note='The NCDHHS page links to a slightly different mailbox (Region2RootsHub@). If mail bounces, try that spelling or call Trillium.'),
 3:dict(name='Vaya Partners (formerly Vaya Health)',contact='No named contact published. Use the hub email.',phone='',phoneNote='No ROOTS phone published.',email='RHTP@vayahealth.com',address='200 Ridgefield Court, Suite 218, Asheville, NC 28806',website='https://rhtp.vayapartners.org/',serves='Region 3',note='The email may move to a vayapartners.org address after the merger.'),
 4:dict(name='UNC Health',contact='No named contact published. Use the hub email.',phone='984-974-1000',phoneNote='UNC Health main line. Not a ROOTS line.',email='NCROOTSRegion4@unchealth.unc.edu',address='101 Manning Drive, Chapel Hill, NC 27514 (main address)',website='https://www.unchealth.org/ncroots',serves='Region 4',note='UNC says it is still developing its application process.'),
 5:dict(name='Trillium Health Resources',contact='No named contact published. Use the hub email.',phone='1-855-250-1539',phoneNote='Trillium Provider Support Services. Not a ROOTS line.',email='Region5NCRootsHub@TrilliumNC.org',address='1019 WH Smith Blvd., Greenville, NC 27834',website='https://www.trilliumhealthresources.org/NC-ROOTS-Region-5',serves='Regions 2 and 5',note='The NCDHHS page links to a slightly different mailbox (Region5RootsHub@). If mail bounces, try that spelling or call Trillium.'),
 6:dict(name='Access East, Inc.',contact='No named contact published. Use the hub email.',phone='(252) 847-6809',phoneNote='Access East main line. No ROOTS phone is published.',email='rhtp@accesseast.org',address='PO Box 6028, 2410 Stantonsburg Road, Stanton Square, Greenville, NC 27835',website='https://accesseast.org/access-east-nc-roots-hub/',serves='Region 6',note=''),
}

STATE="""const STATE_PROVIDER_SUPPORT = {
      ombudsman: 'NC Medicaid Provider Ombudsman (providers): 866-304-7062, Medicaid.ProviderOmbudsman@dhhs.nc.gov. Hours not published. 877-201-3750 is the member line.',
      contactCenter: 'NC Medicaid Contact Center: 888-245-0179 (Mon–Fri 8am–5pm, closed State holidays)',
      nctracks: 'NCTracks Call Center: 800-688-6696 (Mon–Fri 8am–5pm), NCTracksprovider@nctracks.com',
      hieDesk: 'NC HIEA business office: 919-754-6912, hiea@nc.gov. Technical help desk (SAS): 919-531-2700, HIESupport@sas.com.'
    };

    /* Tailored Plans are assigned by county. Contacts checked against plan pages on 2026-10-18; confirm before relying on them. */
    const PLAN_ORDER = %s;
    const PLANS = %s;
    const COUNTY_PLAN = %s;

    /* Official 6 Medicaid regions (counties verified against the NCDHHS hub map) and the NC ROOTS hub lead for each. */
    const NC_REGIONS_DATA = {
%s
    };

""" 
def js(o): return json.dumps(o,ensure_ascii=False,indent=2).replace('\n','\n    ')
regtxt=[]
for i in range(1,7):
    regtxt.append("      %d: {\n        id: %d,\n        name: %s,\n        rootsHub: %s,\n        rootsHubDetails: %s,\n        counties: %s\n      }"%(i,i,json.dumps(regs[i]),json.dumps(HUBS[i]['name']),json.dumps(HUBS[i],ensure_ascii=False),json.dumps(cnt[i])))
block=STATE%(json.dumps(list(PLANS)),js(PLANS),json.dumps(cp,separators=(',',':')),",\n".join(regtxt))
s=t.index('    const STATE_PROVIDER_SUPPORT')-0
s=t.rfind('/* Statewide contacts',0,s)
e=t.index('    function getRegionColor')
t=t[:s]+block.rstrip('\n').replace('const STATE_PROVIDER_SUPPORT','const STATE_PROVIDER_SUPPORT',1).join(['    ',''])+"\n\n"+t[e:]
# fix leading: block begins "const STATE_..." so prefix indentation done above
open(F,'w').write(t)
print('data ok')
