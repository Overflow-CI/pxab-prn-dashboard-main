import re,os,json,csv
from urllib.parse import urlparse,unquote
from collections import defaultdict
H='/home/user/hello-world/nc_medicaid_bh_dashboard.html'
t=open(H).read()
i=t.index('const DETAIL_SOURCES'); S=json.loads(t[t.index('[',i):t.index('];',i)+1])
# usage
use=defaultdict(set); conf=defaultdict(set)
for m in re.finditer(r"'step_(\d+)_sub_(\d+)': \{(.*?)\n      \},?",t,re.S):
    body=m.group(3)
    sm=re.search(r"sources: \[([\d, ]*)\]",body); cm=re.search(r'confidence: "([^"]+)"',body)
    if not sm: continue
    for n in re.findall(r'\d+',sm.group(1)):
        use[int(n)].add(int(m.group(1)))
        if cm: conf[int(n)].add(cm.group(1))
# research files
UP='/root/.claude/uploads/91141d82-7be3-5ffc-bd0c-f501091745a6/'
def norm(u):
    u=u.split('[')[0].split('?share_frome')[0].split('&share_frome')[0]
    return u.rstrip('.,;:)"\'').rstrip('/')
found=defaultdict(set)
for f in os.listdir(UP):
    if f.endswith('.html'): continue
    lab=re.sub(r'^[0-9a-f]{8}-','',f).rsplit('.',1)[0]
    txt=open(UP+f,errors='ignore').read()
    for u in re.findall(r'https?://[^\s\)\]"<>\\]+',txt):
        found[norm(u)].add(lab)
inapp={norm(u):k for k,u in enumerate(S)}
# publisher map
PUB=[('ncleg.gov','NC General Assembly'),('reports.oah.state.nc.us','NC Office of Administrative Hearings'),('oah.nc.gov','NC Office of Administrative Hearings'),
('ncdhhs.gov','NC DHHS'),('medicaid.ncdhhs.gov','NC Medicaid'),('nctracks.nc.gov','NCTracks (NC Medicaid)'),('hiea.nc.gov','NC Health Information Exchange Authority'),
('ncbroadband.gov','NCDIT Broadband'),('governor.nc.gov','NC Office of the Governor'),('ncmedicaidplans.gov','NC Medicaid Managed Care'),('nc.gov','State of North Carolina'),
('ecfr.gov','Federal (eCFR)'),('cms.gov','CMS'),('congress.gov','U.S. Congress'),('govinfo.gov','U.S. Government Publishing Office'),('federalregister.gov','Federal Register'),
('irs.gov','IRS'),('ada.gov','U.S. DOJ (ADA)'),('hhs.gov','HHS'),('samhsa.gov','SAMHSA'),('dol.gov','U.S. Dept of Labor'),('sam.gov','SAM.gov'),('sba.gov','SBA'),('fbi.gov','FBI'),('oig.hhs.gov','HHS OIG'),
('oah.nc.gov','NC Office of Administrative Hearings'),('oig.hhs.gov','HHS OIG'),('law.cornell.edu','Cornell LII (secondary)'),('alliancehealthplan.org','Alliance Health'),('trilliumhealthresources.org','Trillium Health Resources'),('vayapartners.org','Vaya Partners'),('vayahealth.com','Vaya Health (legacy)'),('partnersbhm.org','Partners (legacy)'),
('carf.org','CARF International'),('coa.org','COA'),('jointcommission.org','The Joint Commission'),('caq.org','CQL'),('thecouncil.org','CQL'),('unchealth.org','UNC Health'),('impacthealth.org','Impact Health'),('accesseast.org','Access East'),
('sos.nc.gov','NC Secretary of State'),('sosnc.gov','NC Secretary of State'),('ncosfm.gov','NC Office of State Fire Marshal'),('nclbgc.org','NC licensing board'),('ncdoi.gov','NC Dept of Insurance'),('ncdor.gov','NC Dept of Revenue'),('ncdol.gov','NC Dept of Labor'),('des.nc.gov','NC Division of Employment Security'),('nccertificationboard.org','NC Substance Abuse Professional Practice Board'),('ncswboard.org','NC Social Work Certification Board'),('ncsbi.gov','NC SBI'),
('pcgus.com','Public Consulting Group'),('durhamnc.gov','City of Durham'),('wake','Wake County'),('legalaid','Legal aid')]
def pub(h):
    h=h.lower().replace('www.','')
    for k,v in PUB:
        if h==k or h.endswith('.'+k) or h.endswith(k): return v
    return h
def category(u):
    h=urlparse(u).netloc.lower().replace('www.',''); p=urlparse(u).path.lower()
    if 'ncleg.gov' in h or 'oah.state.nc.us' in h or 'ecfr.gov' in h or 'law.cornell' in h or 'govinfo' in h or 'federalregister' in h or 'congress.gov' in h: return '1 Law, rules and regulations'
    if any(x in h for x in ['alliancehealthplan','trilliumhealthresources','vayapartners','vayahealth','partnersbhm']): return '4 Tailored Plans (LME/MCOs)'
    if any(x in h for x in ['impacthealth','accesseast','unchealth']) or 'rural-health' in p or 'roots' in p or 'ncbroadband' in h or 'governor.nc' in h: return '6 Rural health (NC ROOTS, RHIF)'
    if 'hiea.nc.gov' in h: return '5 NC HealthConnex'
    if 'nctracks' in h: return '3 NCTracks enrollment'
    if 'medicaid.ncdhhs.gov' in h or 'ncmedicaidplans' in h or 'cms.gov' in h: return '2 NC Medicaid policy and bulletins'
    if 'dhsr' in p or 'ncdhhs.gov' in h: return '2 NC Medicaid policy and bulletins' if 'medicaid' in p else '2 DHHS and DHSR licensure'
    if any(x in h for x in ['carf','coa.org','jointcommission','thecouncil','caq.org']): return '7 Accreditation bodies'
    if 'oig.hhs.gov' in h or 'hhs.gov' in h or 'samhsa' in h or 'childcare' in h: return '10 Federal health and other agencies'
    if any(x in h for x in ['irs.gov','sos.nc','ncdor','des.nc','ncdol','dol.gov','sba.gov','ncdoi','sam.gov','sosnc']): return '8 Business, tax and labor'
    if any(x in h for x in ['ada.gov','ncosfm','durhamnc','fire','zoning']): return '9 Facility, fire and ADA'
    return '10 Other federal, state and local'
def ptype(u):
    h=urlparse(u).netloc.lower()
    if h.endswith('.gov') or '.nc.gov' in h or 'state.nc.us' in h or h.endswith('.us'): return 'Primary (government)'
    if any(x in h for x in ['alliancehealthplan','trilliumhealthresources','vayapartners','vayahealth','partnersbhm','carf.org','coa.org','jointcommission','impacthealth','accesseast','unchealth','thecouncil']): return 'Primary (plan, accreditor or hub lead)'
    return 'Secondary'
rows=[]
for u in sorted(set(inapp)|set(found)):
    h=urlparse(u).netloc
    if not h or '.' not in h or h in('perplexity.ai','www.perplexity.ai','claude.ai','github.com'): continue
    k=inapp.get(u)
    steps=sorted(use.get(k,[])) if k is not None else []
    confs=sorted(conf.get(k,[])) if k is not None else []
    rows.append(dict(Category=category(u),Publisher=pub(h),Type=ptype(u),URL=u,
      UsedInApp='Yes' if k is not None else 'No (research only)',
      AppSteps=';'.join(map(str,steps)),
      ConfidenceOfEntriesCiting=';'.join(confs),
      ResearchFiles=';'.join(sorted(found.get(u,[]))) ,
      Domain=h))
rows.sort(key=lambda r:(r['Category'],r['Publisher'],r['URL']))
out='/home/user/hello-world/nc_medicaid_sources.csv'
with open(out,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
from collections import Counter
print(len(rows),Counter(r['UsedInApp'] for r in rows),Counter(r['Category'] for r in rows),Counter(r['Type'] for r in rows))
print([r['URL'] for r in rows if r['Category'].startswith('10')][:25])
E_=0
