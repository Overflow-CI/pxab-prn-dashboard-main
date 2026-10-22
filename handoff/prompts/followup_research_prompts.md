# Follow-up research prompts: Tailored Plans by county, regions and hubs, and the open policy questions

These three prompts close the gaps left by the first research pass. They work in a web-search research tool such as Perplexity. In NotebookLM, first add the sources listed at the bottom, because it answers only from sources you load.

**How to use**
1. Start a new chat for each prompt. Paste the **research rules** first, then one prompt.
2. Run **F1** first. It fixes the dashboard's region-based Tailored Plan map, which is the biggest known error.
3. Run **F2** (regions, ROOTS hub contacts and statewide numbers) and **F3** (the eight open policy questions).
4. Send me the JSON from each answer. I will rebuild the plan contacts as a county lookup, correct the region and hub cards, update the affected step text, and rerun the tests.
5. Anything marked `NOT VERIFIED` or `unknown` needs a phone call. Each answer names who to call.

**Dates to keep in mind:** NC's draft medical frailty comments are due Nov 5, 2026 and the Rural Health Innovation Fund application is due Nov 16, 2026 (both already in the app).

---

## Research rules (paste first, every chat)

````text
RESEARCH RULES (apply to every answer)
- It is late October 2026. Use official or primary sources only: NC DHHS, NC Medicaid, NCTracks, DHSR, NC General Assembly, federal agencies, and the plans' own provider pages. Open each page before citing it. Blogs, consultants and forums count only as secondary, and must be labeled that way.
- Never guess or fill a gap. Do not invent phone numbers, emails, addresses, URLs, fees, dates or section numbers. If you cannot verify something on a source you opened, write "NOT VERIFIED" and say what to check and who to call.
- Give the URL and the date shown on the page (or "undated") for every fact. Quote the key sentence, 25 words or fewer, for anything that decides a question.
- If sources conflict, report both with their dates and say which is newer and which is the policy text.
- Values labeled "APP CURRENTLY SHOWS" come from my dashboard and may be wrong. Mark each one CONFIRMED, CORRECTED (give the right value) or NOT VERIFIED.
- Return valid JSON in a json code block exactly as specified, then a short SOURCES table (title, publisher, URL, date, primary or secondary), then OPEN QUESTIONS. Plain text inside JSON strings, one line each, escaped double quotes, no citation markers like [1] inside the JSON. No commentary before the JSON.
- This is research, not legal advice.
````

---

## F1: Tailored Plans by county and plan contacts

````text
PROMPT F1 - NORTH CAROLINA TAILORED PLANS BY COUNTY, AND PLAN CONTACTS

Background: my dashboard assumes each of NC's six Medicaid regions has one Tailored Plan. That is wrong. Tailored Plans are assigned by county. Vaya Health and Partners Health Management merged on Oct 1, 2026 (Vaya Partners), so there are now three plans: Alliance Health, Trillium Health Resources and Vaya Partners.

TASK 1 - County map. For every county in the list below, name the Tailored Plan that covers it today, using the NC Medicaid Plans site (ncmedicaidplans.gov), the NC DHHS LME/MCO directory, NC Medicaid's health plans page and each plan's own county list. Where the NC DHHS directory and the NC Medicaid Plans page disagree (for example a county one omits), report the conflict and say which page is newer.
Counties (100): Alamance, Alexander, Alleghany, Anson, Ashe, Avery, Beaufort, Bertie, Bladen, Brunswick, Buncombe, Burke, Cabarrus, Caldwell, Camden, Carteret, Caswell, Catawba, Chatham, Cherokee, Chowan, Clay, Cleveland, Columbus, Craven, Cumberland, Currituck, Dare, Davidson, Davie, Duplin, Durham, Edgecombe, Forsyth, Franklin, Gaston, Gates, Graham, Granville, Greene, Guilford, Halifax, Harnett, Haywood, Henderson, Hertford, Hoke, Hyde, Iredell, Jackson, Johnston, Jones, Lee, Lenoir, Lincoln, Macon, Madison, Martin, McDowell, Mecklenburg, Mitchell, Montgomery, Moore, Nash, New Hanover, Northampton, Onslow, Orange, Pamlico, Pasquotank, Pender, Perquimans, Person, Pitt, Polk, Randolph, Richmond, Robeson, Rockingham, Rowan, Rutherford, Sampson, Scotland, Stanly, Stokes, Surry, Swain, Transylvania, Tyrrell, Union, Vance, Wake, Warren, Washington, Watauga, Wayne, Wilkes, Wilson, Yadkin, Yancey

TASK 2 - Plan contacts. For each of the three plans, give provider-facing details. APP CURRENTLY SHOWS (for comparison, includes the old Partners entry):
  Vaya Health: provider phone 1-866-990-9712; website https://providers.vayahealth.com/; address 200 Ridgefield Court, Suite 218, Asheville, NC 28806; UM phone 1-800-893-6246 (ext. 1515); UM email UM@vayahealth.com; portal Vaya Provider Portal (https://providers.vayahealth.com/provider-portal)
  Partners Health Management: provider phone 1-877-398-4145; website https://providers.partnersbhm.org/; address 901 S. New Hope Road, Gastonia, NC 28054; UM phone 1-877-398-4145; UM email BHIDDManualAuthorizations@partnersbhm.org; portal ProviderCONNECT Portal (https://providers.partnersbhm.org/provider-portal-help/)
  Partners Health / Alliance Health: provider phone Partners: 1-877-398-4145 | Alliance: 1-855-759-9700; website https://providers.partnersbhm.org/; address Serving Mecklenburg, Cabarrus, Union, Gaston & surrounding corridors; UM phone 1-877-398-4145 / 1-855-759-9700; UM email PAS@PartnersBHM.org / ACSSupport@AllianceHealthPlan.org; portal Partners & Alliance Portals (https://providers.partnersbhm.org/)
  Alliance Health: provider phone 1-855-759-9700; website https://www.alliancehealthplan.org/providers/; address 5200 W. Paramount Parkway, Suite 200, Morrisville, NC 27560; UM phone 1-855-759-9700 (Option 2); UM email ACSSupport@AllianceHealthPlan.org; portal Alliance Provider Central Portal (https://alliancehealth.okta.com/)
  Trillium Health Resources: provider phone 1-855-250-1539; website https://www.trilliumhealthresources.org/; address 1019 WH Smith Blvd, Greenville, NC 27834 (Mailing: PO Box 12797, Durham, NC 27709); UM phone 1-855-250-1539 (ext. 6875); UM email Info@TrilliumNC.org; portal Trillium Provider Portal (https://www.trilliumhealthresources.org/for-providers)

TASK 3 - New provider status. For each plan: does it currently accept new provider applications for Peer Support (CCP 8G), SAIOP (8A-12) and SACOT (8A-13)? Peer support became a closed-network service on July 7, 2026 (Alliance says July 2); quote the sentence that states the effective date and say which source governs. Link each plan's "current service needs" or network-need page if it has one.

OUTPUT (the JSON must have exactly these top-level keys):
{
  "counties": {"Alamance": "<plan name exactly as the official source writes it>", "...": "..."},
  "county_conflicts": [{"county": "", "source_a": "", "plan_a": "", "source_b": "", "plan_b": "", "newer": ""}],
  "plans": {
    "Alliance Health": {"providerPhone": "", "website": "", "centralOffice": "", "umPhone": "", "umEmail": "", "providerNetworkEmail": "", "portalLabel": "", "portalUrl": "", "newProviderPage": "", "acceptingPeerSupport": "yes|no|unknown", "acceptingSAIOP": "yes|no|unknown", "acceptingSACOT": "yes|no|unknown", "needsPageUrl": "", "asOf": "", "sources": [], "appValueChecks": [{"field": "", "appValue": "", "result": "CONFIRMED|CORRECTED|NOT VERIFIED", "correct": ""}]},
    "Trillium Health Resources": {},
    "Vaya Partners": {}
  },
  "peer_support_closed_network": {"effectiveDate": "", "governingSource": "", "quote": "", "conflict": ""}
}
Use "NOT IN SOURCES" or "unknown" instead of guessing. Every one of the 100 counties must appear as a key.
````

---

## F2: Regions, ROOTS hub leads and statewide contacts

````text
PROMPT F2 - MEDICAID REGIONS, NC ROOTS HUB LEADS AND STATEWIDE SUPPORT CONTACTS

TASK 1 - Region definitions. NC Medicaid and NC DHHS group the 100 counties into six regions (used for Standard Plans and for NC ROOTS hub leads). Verify the county list for each region against the official source. APP CURRENTLY SHOWS:
  Region 1 — Western NC: Avery, Buncombe, Burke, Caldwell, Cherokee, Clay, Graham, Haywood, Henderson, Jackson, Macon, Madison, McDowell, Mitchell, Polk, Rutherford, Swain, Transylvania, Yancey
  Region 2 — Northwest NC: Alleghany, Ashe, Davidson, Davie, Forsyth, Guilford, Randolph, Rockingham, Stokes, Surry, Watauga, Wilkes, Yadkin
  Region 3 — Southwest NC: Alexander, Anson, Cabarrus, Catawba, Cleveland, Gaston, Iredell, Lincoln, Mecklenburg, Rowan, Stanly, Union
  Region 4 — North Central NC: Alamance, Caswell, Chatham, Durham, Franklin, Granville, Johnston, Nash, Orange, Person, Vance, Wake, Warren, Wilson
  Region 5 — Sandhills / South Central NC: Bladen, Brunswick, Columbus, Cumberland, Harnett, Hoke, Lee, Montgomery, Moore, New Hanover, Pender, Richmond, Robeson, Sampson, Scotland
  Region 6 — Eastern NC: Beaufort, Bertie, Camden, Carteret, Chowan, Craven, Currituck, Dare, Duplin, Edgecombe, Gates, Greene, Halifax, Hertford, Hyde, Jones, Lenoir, Martin, Northampton, Onslow, Pamlico, Pasquotank, Perquimans, Pitt, Tyrrell, Washington, Wayne
Return which counties, if any, are in a different region from what the app shows, and the source.

TASK 2 - NC ROOTS hub leads (the Rural Health Transformation program). For each region, verify the hub lead organization, contact person and title, phone, email, address and website using the NC DHHS hub leads page and press release. APP CURRENTLY SHOWS:
  Region 1: Impact Health | contact Tamara Smith (Executive Director) | phone (828) 357-8170 / (800) 581-0182 | email t.smith@impacthealth.org | website https://impacthealth.org/ | address PO Box 8427, Asheville, NC 28814
  Region 2: Trillium Health Resources | contact Region 2 ROOTS Lead Coordinator | phone 1-855-250-1539 | email Region2NCRootsHub@trilliumnc.org | website https://www.trilliumhealthresources.org/ | address 1019 WH Smith Blvd, Greenville, NC 27834
  Region 3: Vaya Health | contact NC ROOTS Region 3 Strategy Director | phone 1-800-962-9003 | email RHTP@vayahealth.com | website https://www.vayahealth.com/ | address 200 Ridgefield Court, Suite 218, Asheville, NC 28806
  Region 4: UNC Health | contact NC ROOTS Region 4 Team | phone (984) 974-1000 / 1-800-806-1964 | email NCROOTSRegion4@unchealth.unc.edu | website https://www.unchealth.org/ | address 101 Manning Drive, Chapel Hill, NC 27514
  Region 5: Trillium Health Resources | contact Region 5 ROOTS Lead | phone 1-855-250-1539 | email Region5NCRootsHub@trilliumnc.org | website https://www.trilliumhealthresources.org/ | address 1019 WH Smith Blvd, Greenville, NC 27834
  Region 6: Access East, Inc. | contact Access East RHTP Hub Team | phone (252) 847-3027 | email Info-AccessEast@accesseast.org | website https://accesseast.org/ | address 2410 S. Charles Blvd, Greenville, NC 27858
Mark each field CONFIRMED, CORRECTED or NOT VERIFIED. Do not keep a person's name or email unless the official page shows it. Also list any regional funding opportunities that are open now (name, region, deadline, link) and the Rural Health Innovation Fund contact and deadline.

TASK 3 - Statewide support contacts. APP CURRENTLY SHOWS: NC Medicaid Provider Ombudsman 877-201-3750 (Medicaid.ProviderOmbudsman@dhhs.nc.gov); NCTracks Call Center 1-800-688-6696 (Mon-Fri 8am-5pm); NC HealthConnex HIEA Helpdesk 919-754-6912 (hiea@nc.gov). An earlier research pass gave the Provider Ombudsman as 866-304-7062 and the NC Medicaid Contact Center as 888-245-0179. Confirm the correct number, email and hours for each, and say which are for providers.

OUTPUT (exactly these top-level keys):
{
  "regionCounty": {"<county>": <region number 1-6>},
  "regionDifferences": [{"county": "", "appRegion": 0, "officialRegion": 0, "source": ""}],
  "hubs": {"1": {"organization": "", "contactPerson": "", "title": "", "phone": "", "email": "", "address": "", "website": "", "regionsServed": [], "checks": [{"field": "", "appValue": "", "result": "CONFIRMED|CORRECTED|NOT VERIFIED", "correct": ""}], "sources": []}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}},
  "openFunding": [{"name": "", "region": "", "deadline": "", "link": ""}],
  "statewide": {"providerOmbudsman": {"phone": "", "email": "", "hours": "", "sources": []}, "medicaidContactCenter": {}, "nctracksCallCenter": {}, "hiea": {}}
}
````

---

## F3: Open policy questions

````text
PROMPT F3 - OPEN POLICY QUESTIONS FROM THE FIRST RESEARCH PASS

Answer each question separately. For each, give a status: "settled" (one authoritative source decides it), "conflict" (sources disagree) or "unknown" (no source found). Quote the deciding sentences, name the policy section or page, and give the date of each source. If it is a conflict, say which source is newer, which is the policy text, and who at NC Medicaid or DHSR can settle it (office, phone, email, only if on an official page).

Q1. ACCREDITATION DEADLINE. When must each service be nationally accredited: Peer Support (CCP 8G), SAIOP (CCP 8A-12) and SACOT (CCP 8A-13)? The CCPs (effective Jan 1, 2026, section 6.1) appear to say 1 year from enrollment. The Provider Permission Matrix (Aug 16, 2026) appears to say 3 years for SAIOP and SACOT and 1 year for peer support. NC Medicaid's April 16, 2026 bulletin "post-enrollment national accreditation update" and an April 2026 NCTracks notice also address it. Also: when does the clock start (enrollment, service selection, license date)? Which bodies are accepted (COA, The Joint Commission, CARF, CQL)? Is any later notice (May to October 2026) newer than the April bulletin?

Q2. DOES A PEER-SUPPORT-ONLY PROVIDER NEED A DHSR LICENSE? The Provider Permission Matrix shows no DHSR license for Peer Support, and DHSR's new-provider presentation does not list it as a licensed service. Is peer support a "mental health, developmental disabilities or substance abuse facility" under G.S. 122C-3(14), or otherwise exempt? Does DHSR, NC Medicaid or any Tailored Plan say anything about a peer-support-only office (zoning, fire marshal, walkthrough, HCPR checks, criminal checks)?

Q3. WHO CREDENTIALS A NEW PROVIDER? One NCTracks FAQ says LME/MCOs no longer perform credentialing, but CCP 8G section 6.1 says providers must be "credentialed and contracted by" the health plan, and CCPs 8A-12 and 8A-13 say "credentialed and contracted by the DHHS designated contractor." What does each plan (Alliance, Trillium, Vaya Partners) still require after NCTracks enrollment: forms, CAQH, primary-source documents, roster forms, contract steps? What is the new NC DHHS Provider Credentialing Committee's role, and since when? Date each source.

Q4. WHAT DO THE CHECKS COST? (a) NCTracks fingerprinting for owners with 5% or more ownership: the price a provider actually pays at a sheriff's office or approved vendor, and how fees are collected. (b) The NC SBI state-only criminal check fee and the fingerprint-based national check fee for employees under G.S. 122C-80 (the SBI access form shows $38 per fingerprint card; confirm whether that is the national check). (c) How a not-yet-licensed applicant runs checks, given that DHSR's ABCMS system needs a facility license number. (d) Any DHHS Criminal Records Check Unit fee. Give amounts only if a source shows them.

Q5. VAYA PARTNERS INTAKE AFTER OCT 1, 2026. For counties formerly served by Partners, which intake page, form, email and phone should a new provider use? Is Vaya Partners accepting new contracting requests (Partners paused them on Aug 1, 2026)? Which provider portal, claims platform and payer ID apply now? Confirm the payer IDs reported earlier: Alliance 23071, Trillium 43072, Vaya Partners 13010.

Q6. NC HEALTHCONNEX FOR NEW PROVIDERS. G.S. 90-414.4 required connection by Jan 1, 2023. Does a provider that starts billing after that date get any grace period? Does NC Medicaid, NCTracks or any Tailored Plan require proof of connection before billing or credentialing? Should a SAIOP or SACOT program that holds 42 CFR Part 2 records sign the Full or the Submission-only agreement?

Q7. NCTRACKS HIGH-RISK ENROLLMENT. For taxonomy 251S00000X: who performs the pre-enrollment site visit (Public Consulting Group?), how a provider schedules or tracks it, what the visitor checks, how long enrollment typically takes, and whether the site visit and fingerprinting waiver for nationally accredited providers (Sept 14, 2026 bulletin) applies to a brand-new provider that is not yet accredited.

Q8. PEER SUPPORT CLOSED-NETWORK DATE. Quote the effective-date section of Session Law 2026-41 (Senate Bill 257) and the NC Medicaid mandatory closed networks fact sheet. Which date governs, July 2 or July 7, 2026, and does any Tailored Plan publish its own date or current needs for Peer Support?

OUTPUT: one valid JSON object in a json code block with keys "q1" to "q8". Each value: {"status": "settled|conflict|unknown", "answer": "", "quotes": [{"text": "", "source": "", "section": "", "date": ""}], "whoCanSettle": "", "sources": [], "confidence": "high|medium|low", "verify": ""}.
````

---

## Sources to add if you use NotebookLM

````text
Sources worth opening (add them to a notebook if you use NotebookLM):
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
- https://hiea.nc.gov/providers/what-does-law-mandate
````
