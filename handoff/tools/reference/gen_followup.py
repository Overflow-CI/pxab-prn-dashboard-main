import json
R = json.load(open('regions.json'))
counties = sorted(c for r in R.values() for c in r['counties'])

RULES = '''RESEARCH RULES (apply to every answer)
- It is late October 2026. Use official or primary sources only: NC DHHS, NC Medicaid, NCTracks, DHSR, NC General Assembly, federal agencies, and the plans' own provider pages. Open each page before citing it. Blogs, consultants and forums count only as secondary, and must be labeled that way.
- Never guess or fill a gap. Do not invent phone numbers, emails, addresses, URLs, fees, dates or section numbers. If you cannot verify something on a source you opened, write "NOT VERIFIED" and say what to check and who to call.
- Give the URL and the date shown on the page (or "undated") for every fact. Quote the key sentence, 25 words or fewer, for anything that decides a question.
- If sources conflict, report both with their dates and say which is newer and which is the policy text.
- Values labeled "APP CURRENTLY SHOWS" come from my dashboard and may be wrong. Mark each one CONFIRMED, CORRECTED (give the right value) or NOT VERIFIED.
- Return valid JSON in a json code block exactly as specified, then a short SOURCES table (title, publisher, URL, date, primary or secondary), then OPEN QUESTIONS. Plain text inside JSON strings, one line each, escaped double quotes, no citation markers like [1] inside the JSON. No commentary before the JSON.
- This is research, not legal advice.'''

def region_block():
    out = []
    for r in R.values():
        out.append(f"  {r['name']}: {', '.join(r['counties'])}")
    return '\n'.join(out)

def plan_block():
    seen, out = set(), []
    for r in R.values():
        t = r['tailoredPlanDetails']
        key = t['name']
        if key in seen: continue
        seen.add(key)
        out.append(f"  {t['name']}: provider phone {t['phone']}; website {t['website']}; address {t['address']}; UM phone {t['umPhone']}; UM email {t['umEmail']}; portal {t['portalLabel']} ({t['portalUrl']})")
    return '\n'.join(out)

def hub_block():
    out = []
    for r in R.values():
        h = r['rootsHubDetails']
        out.append(f"  Region {r['id']}: {h['name']} | contact {h['contactPerson']} | phone {h['phone']} | email {h['email']} | website {h['website']} | address {h['address']}")
    return '\n'.join(out)

F1 = f'''PROMPT F1 - NORTH CAROLINA TAILORED PLANS BY COUNTY, AND PLAN CONTACTS

Background: my dashboard assumes each of NC's six Medicaid regions has one Tailored Plan. That is wrong. Tailored Plans are assigned by county. Vaya Health and Partners Health Management merged on Oct 1, 2026 (Vaya Partners), so there are now three plans: Alliance Health, Trillium Health Resources and Vaya Partners.

TASK 1 - County map. For every county in the list below, name the Tailored Plan that covers it today, using the NC Medicaid Plans site (ncmedicaidplans.gov), the NC DHHS LME/MCO directory, NC Medicaid's health plans page and each plan's own county list. Where the NC DHHS directory and the NC Medicaid Plans page disagree (for example a county one omits), report the conflict and say which page is newer.
Counties (100): {', '.join(counties)}

TASK 2 - Plan contacts. For each of the three plans, give provider-facing details. APP CURRENTLY SHOWS (for comparison, includes the old Partners entry):
{plan_block()}

TASK 3 - New provider status. For each plan: does it currently accept new provider applications for Peer Support (CCP 8G), SAIOP (8A-12) and SACOT (8A-13)? Peer support became a closed-network service on July 7, 2026 (Alliance says July 2); quote the sentence that states the effective date and say which source governs. Link each plan's "current service needs" or network-need page if it has one.

OUTPUT (the JSON must have exactly these top-level keys):
{{
  "counties": {{"Alamance": "<plan name exactly as the official source writes it>", "...": "..."}},
  "county_conflicts": [{{"county": "", "source_a": "", "plan_a": "", "source_b": "", "plan_b": "", "newer": ""}}],
  "plans": {{
    "Alliance Health": {{"providerPhone": "", "website": "", "centralOffice": "", "umPhone": "", "umEmail": "", "providerNetworkEmail": "", "portalLabel": "", "portalUrl": "", "newProviderPage": "", "acceptingPeerSupport": "yes|no|unknown", "acceptingSAIOP": "yes|no|unknown", "acceptingSACOT": "yes|no|unknown", "needsPageUrl": "", "asOf": "", "sources": [], "appValueChecks": [{{"field": "", "appValue": "", "result": "CONFIRMED|CORRECTED|NOT VERIFIED", "correct": ""}}]}},
    "Trillium Health Resources": {{}},
    "Vaya Partners": {{}}
  }},
  "peer_support_closed_network": {{"effectiveDate": "", "governingSource": "", "quote": "", "conflict": ""}}
}}
Use "NOT IN SOURCES" or "unknown" instead of guessing. Every one of the 100 counties must appear as a key.'''

F2 = f'''PROMPT F2 - MEDICAID REGIONS, NC ROOTS HUB LEADS AND STATEWIDE SUPPORT CONTACTS

TASK 1 - Region definitions. NC Medicaid and NC DHHS group the 100 counties into six regions (used for Standard Plans and for NC ROOTS hub leads). Verify the county list for each region against the official source. APP CURRENTLY SHOWS:
{region_block()}
Return which counties, if any, are in a different region from what the app shows, and the source.

TASK 2 - NC ROOTS hub leads (the Rural Health Transformation program). For each region, verify the hub lead organization, contact person and title, phone, email, address and website using the NC DHHS hub leads page and press release. APP CURRENTLY SHOWS:
{hub_block()}
Mark each field CONFIRMED, CORRECTED or NOT VERIFIED. Do not keep a person's name or email unless the official page shows it. Also list any regional funding opportunities that are open now (name, region, deadline, link) and the Rural Health Innovation Fund contact and deadline.

TASK 3 - Statewide support contacts. APP CURRENTLY SHOWS: NC Medicaid Provider Ombudsman 877-201-3750 (Medicaid.ProviderOmbudsman@dhhs.nc.gov); NCTracks Call Center 1-800-688-6696 (Mon-Fri 8am-5pm); NC HealthConnex HIEA Helpdesk 919-754-6912 (hiea@nc.gov). An earlier research pass gave the Provider Ombudsman as 866-304-7062 and the NC Medicaid Contact Center as 888-245-0179. Confirm the correct number, email and hours for each, and say which are for providers.

OUTPUT (exactly these top-level keys):
{{
  "regionCounty": {{"<county>": <region number 1-6>}},
  "regionDifferences": [{{"county": "", "appRegion": 0, "officialRegion": 0, "source": ""}}],
  "hubs": {{"1": {{"organization": "", "contactPerson": "", "title": "", "phone": "", "email": "", "address": "", "website": "", "regionsServed": [], "checks": [{{"field": "", "appValue": "", "result": "CONFIRMED|CORRECTED|NOT VERIFIED", "correct": ""}}], "sources": []}}, "2": {{}}, "3": {{}}, "4": {{}}, "5": {{}}, "6": {{}}}},
  "openFunding": [{{"name": "", "region": "", "deadline": "", "link": ""}}],
  "statewide": {{"providerOmbudsman": {{"phone": "", "email": "", "hours": "", "sources": []}}, "medicaidContactCenter": {{}}, "nctracksCallCenter": {{}}, "hiea": {{}}}}
}}'''

F3 = '''PROMPT F3 - OPEN POLICY QUESTIONS FROM THE FIRST RESEARCH PASS

Answer each question separately. For each, give a status: "settled" (one authoritative source decides it), "conflict" (sources disagree) or "unknown" (no source found). Quote the deciding sentences, name the policy section or page, and give the date of each source. If it is a conflict, say which source is newer, which is the policy text, and who at NC Medicaid or DHSR can settle it (office, phone, email, only if on an official page).

Q1. ACCREDITATION DEADLINE. When must each service be nationally accredited: Peer Support (CCP 8G), SAIOP (CCP 8A-12) and SACOT (CCP 8A-13)? The CCPs (effective Jan 1, 2026, section 6.1) appear to say 1 year from enrollment. The Provider Permission Matrix (Aug 16, 2026) appears to say 3 years for SAIOP and SACOT and 1 year for peer support. NC Medicaid's April 16, 2026 bulletin "post-enrollment national accreditation update" and an April 2026 NCTracks notice also address it. Also: when does the clock start (enrollment, service selection, license date)? Which bodies are accepted (COA, The Joint Commission, CARF, CQL)? Is any later notice (May to October 2026) newer than the April bulletin?

Q2. DOES A PEER-SUPPORT-ONLY PROVIDER NEED A DHSR LICENSE? The Provider Permission Matrix shows no DHSR license for Peer Support, and DHSR's new-provider presentation does not list it as a licensed service. Is peer support a "mental health, developmental disabilities or substance abuse facility" under G.S. 122C-3(14), or otherwise exempt? Does DHSR, NC Medicaid or any Tailored Plan say anything about a peer-support-only office (zoning, fire marshal, walkthrough, HCPR checks, criminal checks)?

Q3. WHO CREDENTIALS A NEW PROVIDER? One NCTracks FAQ says LME/MCOs no longer perform credentialing, but CCP 8G section 6.1 says providers must be "credentialed and contracted by" the health plan, and CCPs 8A-12 and 8A-13 say "credentialed and contracted by the DHHS designated contractor." What does each plan (Alliance, Trillium, Vaya Partners) still require after NCTracks enrollment: forms, CAQH, primary-source documents, roster forms, contract steps? What is the new NC DHHS Provider Credentialing Committee's role, and since when? Date each source.

Q4. WHAT DO THE CHECKS COST? (a) NCTracks fingerprinting for owners with 5% or more ownership: the price a provider actually pays at a sheriff's office or approved vendor, and how fees are collected. (b) The NC SBI state-only criminal check fee and the fingerprint-based national check fee for employees under G.S. 122C-80 (the SBI access form shows $38 per fingerprint card; confirm whether that is the national check). (c) How a not-yet-licensed applicant runs checks, given that DHSR's ABCMS system needs a facility license number. (d) Any DHHS Criminal Records Check Unit fee. Give amounts only if a source shows them.

Q5. VAYA PARTNERS INTAKE AFTER OCT 1, 2026. For counties formerly served by Partners, which intake page, form, email and phone should a new provider use? Is Vaya Partners accepting new contracting requests (Partners paused them on Aug 1, 2026)? Which provider portal, claims platform and payer ID apply now? Confirm the payer IDs reported earlier: Alliance 23071, Trillium 43072, Vaya Partners 13010.

Q6. NC HEALTHCONNEX FOR NEW PROVIDERS. G.S. 90-414.4 required connection by Jan 1, 2023. Does a provider that starts billing after that date get any grace period? Does NC Medicaid, NCTracks or any Tailored Plan require proof of connection before billing or credentialing? Should a SAIOP or SACOT program that holds 42 CFR Part 2 records sign the Full or the Submission-only agreement?

Q7. NCTRACKS HIGH-RISK ENROLLMENT. For taxonomy 251S00000X: who performs the pre-enrollment site visit (Public Consulting Group?), how a provider schedules or tracks it, what the visitor checks, how long enrollment typically takes, and whether the site visit and fingerprinting waiver for nationally accredited providers (Sept 14, 2026 bulletin) applies to a brand-new provider that is not yet accredited.

Q8. PEER SUPPORT CLOSED-NETWORK DATE. Quote the effective-date section of Session Law 2026-41 (Senate Bill 257) and the NC Medicaid mandatory closed networks fact sheet. Which date governs, July 2 or July 7, 2026, and does any Tailored Plan publish its own date or current needs for Peer Support?

OUTPUT: one valid JSON object in a json code block with keys "q1" to "q8". Each value: {"status": "settled|conflict|unknown", "answer": "", "quotes": [{"text": "", "source": "", "section": "", "date": ""}], "whoCanSettle": "", "sources": [], "confidence": "high|medium|low", "verify": ""}.'''

SRC = '''Sources worth opening (add them to a notebook if you use NotebookLM):
- https://www.ncmedicaidplans.gov/en/get-answers
- https://www.ncdhhs.gov/providers/lme-mco-directory
- https://medicaid.ncdhhs.gov/about-nc-medicaid/health-plans
- https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-organizations-orchestrating-transformation-sustainability-roots-hub-leads
- https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-health-transformation-program-grant-opportunities
- https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/
- https://www.trilliumhealthresources.org/contracting-information
- https://providers.vayapartners.org/enrollment/
- https://providers.vayahealth.com/wp-content/uploads/2026/09/Joint_VP_Merger_Info_Session_9-14-26.pdf
- https://medicaid.ncdhhs.gov/providers/provider-playbook-medicaid-managed-care/fact-sheets/mandatory-closed-networks
- https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-41.pdf
- https://medicaid.ncdhhs.gov/blog/2026/04/16/post-enrollment-national-accreditation-update
- https://medicaid.ncdhhs.gov/blog/2026/09/14/recent-behavioral-health-enrollment-updates-organizations
- https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx
- https://medicaid.ncdhhs.gov/8g-peer-support-services/open
- https://medicaid.ncdhhs.gov/media/15767/download
- https://medicaid.ncdhhs.gov/media/15769/download
- https://info.ncdhhs.gov/dhsr/mhlcs/pdf/newprovider.pdf
- https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-Behavioral-Health-Provider-Enrollment.html
- https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-fingerprinting.html
- https://info.ncdhhs.gov/dhsr/abcms/pdf/Non-Criminal-Justice-Access-Agreement-Form_SB-41.pdf
- https://hiea.nc.gov/providers/what-does-law-mandate'''

out = ['# Follow-up research prompts: Tailored Plans by county, regions and hubs, and the open policy questions\n',
'''These three prompts close the gaps left by the first research pass. They work in a web-search research tool such as Perplexity. In NotebookLM, first add the sources listed at the bottom, because it answers only from sources you load.

**How to use**
1. Start a new chat for each prompt. Paste the **research rules** first, then one prompt.
2. Run **F1** first. It fixes the dashboard's region-based Tailored Plan map, which is the biggest known error.
3. Run **F2** (regions, ROOTS hub contacts and statewide numbers) and **F3** (the eight open policy questions).
4. Send me the JSON from each answer. I will rebuild the plan contacts as a county lookup, correct the region and hub cards, update the affected step text, and rerun the tests.
5. Anything marked `NOT VERIFIED` or `unknown` needs a phone call. Each answer names who to call.

**Dates to keep in mind:** NC's draft medical frailty comments are due Nov 5, 2026 and the Rural Health Innovation Fund application is due Nov 16, 2026 (both already in the app).
''',
'---\n\n## Research rules (paste first, every chat)\n\n````text\n' + RULES + '\n````\n',
'---\n\n## F1: Tailored Plans by county and plan contacts\n\n````text\n' + F1 + '\n````\n',
'---\n\n## F2: Regions, ROOTS hub leads and statewide contacts\n\n````text\n' + F2 + '\n````\n',
'---\n\n## F3: Open policy questions\n\n````text\n' + F3 + '\n````\n',
'---\n\n## Sources to add if you use NotebookLM\n\n````text\n' + SRC + '\n````\n']
open('followup_prompts.md','w').write('\n'.join(out))
import re
t=open('followup_prompts.md').read()
print('chars',len(t),'| counties listed in F1:',F1.count(',')>0,len(counties))
print([h for h in re.findall(r'^## (.*)$',t,re.M)])
