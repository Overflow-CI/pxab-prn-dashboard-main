> From: https://www.perplexity.ai/computer/tasks/2e025509-734d-48b5-bfa8-e324d2f3c319

# you asked

message time: 2026-10-18 23:36:13

RESEARCH RULES (apply to every answer)
- It is late October 2026. Use official or primary sources only: NC DHHS, NC Medicaid, NCTracks, DHSR, NC General Assembly, federal agencies, and the plans' own provider pages. Open each page before citing it. Blogs, consultants and forums count only as secondary, and must be labeled that way.
- Never guess or fill a gap. Do not invent phone numbers, emails, addresses, URLs, fees, dates or section numbers. If you cannot verify something on a source you opened, write "NOT VERIFIED" and say what to check and who to call.
- Give the URL and the date shown on the page (or "undated") for every fact. Quote the key sentence, 25 words or fewer, for anything that decides a question.
- If sources conflict, report both with their dates and say which is newer and which is the policy text.
- Values labeled "APP CURRENTLY SHOWS" come from my dashboard and may be wrong. Mark each one CONFIRMED, CORRECTED (give the right value) or NOT VERIFIED.
- Return valid JSON in a json code block exactly as specified, then a short SOURCES table (title, publisher, URL, date, primary or secondary), then OPEN QUESTIONS. Plain text inside JSON strings, one line each, escaped double quotes, no citation markers like [1] inside the JSON. No commentary before the JSON.
- This is research, not legal advice.  PROMPT F1 - NORTH CAROLINA TAILORED PLANS BY COUNTY, AND PLAN CONTACTS

Background: my dashboard assumes each of NC's six Medicaid regions has one Tailored Plan. That is wrong. Tailored Plans are assigned by county. Vaya Health and Partners Health Management merged on Oct 1, 2026 (Vaya Partners), so there are now three plans: Alliance Health, Trillium Health Resources and Vaya Partners.

TASK 1 - County map. For every county in the list below, name the Tailored Plan that covers it today, using the NC Medicaid Plans site (ncmedicaidplans.gov), the NC DHHS LME/MCO directory, NC Medicaid's health plans page and each plan's own county list. Where the NC DHHS directory and the NC Medicaid Plans page disagree (for example a county one omits), report the conflict and say which page is newer.
Counties (100): Alamance, Alexander, Alleghany, Anson, Ashe, Avery, Beaufort, Bertie, Bladen, Brunswick, Buncombe, Burke, Cabarrus, Caldwell, Camden, Carteret, Caswell, Catawba, Chatham, Cherokee, Chowan, Clay, Cleveland, Columbus, Craven, Cumberland, Currituck, Dare, Davidson, Davie, Duplin, Durham, Edgecombe, Forsyth, Franklin, Gaston, Gates, Graham, Granville, Greene, Guilford, Halifax, Harnett, Haywood, Henderson, Hertford, Hoke, Hyde, Iredell, Jackson, Johnston, Jones, Lee, Lenoir, Lincoln, Macon, Madison, Martin, McDowell, Mecklenburg, Mitchell, Montgomery, Moore, Nash, New Hanover, Northampton, Onslow, Orange, Pamlico, Pasquotank, Pender, Perquimans, Person, Pitt, Polk, Randolph, Richmond, Robeson, Rockingham, Rowan, Rutherford, Sampson, Scotland, Stanly, Stokes, Surry, Swain, Transylvania, Tyrrell, Union, Vance, Wake, Warren, Washington, Watauga, Wayne, Wilkes, Wilson, Yadkin, Yancey

TASK 2 - Plan contacts. For each of the three plans, give provider-facing details. APP CURRENTLY SHOWS (for comparison, includes the old Partners entry):
  Vaya Health: provider phone 1-866-990-9712; website [https://providers.vayahealth.com/](https://providers.vayahealth.com/); address 200 Ridgefield Court, Suite 218, Asheville, NC 28806; UM phone 1-800-893-6246 (ext. 1515); UM email UM@vayahealth.com; portal Vaya Provider Portal (https://providers.vayahealth.com/provider-portal)
  Partners Health Management: provider phone 1-877-398-4145; website [https://providers.partnersbhm.org/](https://providers.partnersbhm.org/); address 901 S. New Hope Road, Gastonia, NC 28054; UM phone 1-877-398-4145; UM email BHIDDManualAuthorizations@partnersbhm.org; portal ProviderCONNECT Portal (https://providers.partnersbhm.org/provider-portal-help/)
  Partners Health / Alliance Health: provider phone Partners: 1-877-398-4145 | Alliance: 1-855-759-9700; website [https://providers.partnersbhm.org/](https://providers.partnersbhm.org/); address Serving Mecklenburg, Cabarrus, Union, Gaston & surrounding corridors; UM phone 1-877-398-4145 / 1-855-759-9700; UM email PAS@PartnersBHM.org / ACSSupport@AllianceHealthPlan.org; portal Partners & Alliance Portals (https://providers.partnersbhm.org/)
  Alliance Health: provider phone 1-855-759-9700; website [https://www.alliancehealthplan.org/providers/](https://www.alliancehealthplan.org/providers/); address 5200 W. Paramount Parkway, Suite 200, Morrisville, NC 27560; UM phone 1-855-759-9700 (Option 2); UM email ACSSupport@AllianceHealthPlan.org; portal Alliance Provider Central Portal (https://alliancehealth.okta.com/)
  Trillium Health Resources: provider phone 1-855-250-1539; website [https://www.trilliumhealthresources.org/](https://www.trilliumhealthresources.org/); address 1019 WH Smith Blvd, Greenville, NC 27834 (Mailing: PO Box 12797, Durham, NC 27709); UM phone 1-855-250-1539 (ext. 6875); UM email [Info@TrilliumNC.org](mailto:Info@TrilliumNC.org); portal Trillium Provider Portal (https://www.trilliumhealthresources.org/for-providers)

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

---

# perplexity response

```json
{
  "counties": {
    "Alamance": "Vaya Partners",
    "Alexander": "Vaya Partners",
    "Alleghany": "Vaya Partners",
    "Anson": "Trillium Health Resources",
    "Ashe": "Vaya Partners",
    "Avery": "Vaya Partners",
    "Beaufort": "Trillium Health Resources",
    "Bertie": "Trillium Health Resources",
    "Bladen": "Trillium Health Resources",
    "Brunswick": "Trillium Health Resources",
    "Buncombe": "Vaya Partners",
    "Burke": "Vaya Partners",
    "Cabarrus": "Vaya Partners",
    "Caldwell": "Vaya Partners",
    "Camden": "Trillium Health Resources",
    "Carteret": "Trillium Health Resources",
    "Caswell": "Vaya Partners",
    "Catawba": "Vaya Partners",
    "Chatham": "Vaya Partners",
    "Cherokee": "Vaya Partners",
    "Chowan": "Trillium Health Resources",
    "Clay": "Vaya Partners",
    "Cleveland": "Vaya Partners",
    "Columbus": "Trillium Health Resources",
    "Craven": "Trillium Health Resources",
    "Cumberland": "Alliance Health",
    "Currituck": "Trillium Health Resources",
    "Dare": "Trillium Health Resources",
    "Davidson": "Vaya Partners",
    "Davie": "Vaya Partners",
    "Duplin": "Trillium Health Resources",
    "Durham": "Alliance Health",
    "Edgecombe": "Trillium Health Resources",
    "Forsyth": "Vaya Partners",
    "Franklin": "Vaya Partners",
    "Gaston": "Vaya Partners",
    "Gates": "Trillium Health Resources",
    "Graham": "Vaya Partners",
    "Granville": "Vaya Partners",
    "Greene": "Trillium Health Resources",
    "Guilford": "Trillium Health Resources",
    "Halifax": "Trillium Health Resources",
    "Harnett": "Alliance Health",
    "Haywood": "Vaya Partners",
    "Henderson": "Vaya Partners",
    "Hertford": "Trillium Health Resources",
    "Hoke": "Trillium Health Resources",
    "Hyde": "Trillium Health Resources",
    "Iredell": "Vaya Partners",
    "Jackson": "Vaya Partners",
    "Johnston": "Alliance Health",
    "Jones": "Trillium Health Resources",
    "Lee": "Trillium Health Resources",
    "Lenoir": "Trillium Health Resources",
    "Lincoln": "Vaya Partners",
    "Macon": "Vaya Partners",
    "Madison": "Vaya Partners",
    "Martin": "Trillium Health Resources",
    "McDowell": "Vaya Partners",
    "Mecklenburg": "Alliance Health",
    "Mitchell": "Vaya Partners",
    "Montgomery": "Trillium Health Resources",
    "Moore": "Trillium Health Resources",
    "Nash": "Trillium Health Resources",
    "New Hanover": "Trillium Health Resources",
    "Northampton": "Trillium Health Resources",
    "Onslow": "Trillium Health Resources",
    "Orange": "Alliance Health",
    "Pamlico": "Trillium Health Resources",
    "Pasquotank": "Trillium Health Resources",
    "Pender": "Trillium Health Resources",
    "Perquimans": "Trillium Health Resources",
    "Person": "Vaya Partners",
    "Pitt": "Trillium Health Resources",
    "Polk": "Vaya Partners",
    "Randolph": "Trillium Health Resources",
    "Richmond": "Trillium Health Resources",
    "Robeson": "Trillium Health Resources",
    "Rockingham": "Vaya Partners",
    "Rowan": "Vaya Partners",
    "Rutherford": "Vaya Partners",
    "Sampson": "Trillium Health Resources",
    "Scotland": "Trillium Health Resources",
    "Stanly": "Vaya Partners",
    "Stokes": "Vaya Partners",
    "Surry": "Vaya Partners",
    "Swain": "Vaya Partners",
    "Transylvania": "Vaya Partners",
    "Tyrrell": "Trillium Health Resources",
    "Union": "Vaya Partners",
    "Vance": "Vaya Partners",
    "Wake": "Alliance Health",
    "Warren": "Trillium Health Resources",
    "Washington": "Trillium Health Resources",
    "Watauga": "Vaya Partners",
    "Wayne": "Trillium Health Resources",
    "Wilkes": "Vaya Partners",
    "Wilson": "Trillium Health Resources",
    "Yadkin": "Vaya Partners",
    "Yancey": "Vaya Partners"
  },
  "county_conflicts": [
    {
      "county": "Cabarrus",
      "source_a": "NC DHHS LME/MCO Directory https://www.ncdhhs.gov/providers/lme-mco-directory (undated; read Oct 18, 2026)",
      "plan_a": "Not listed under any LME/MCO (omitted)",
      "source_b": "NC Medicaid Plans FAQ https://www.ncmedicaidplans.gov/en/get-answers (undated, names Vaya Partners so it reflects the Oct 1, 2026 merger); also NC Medicaid merger notice (Sept 2026) and vayapartners.org/tailored-plan",
      "plan_b": "Vaya Partners",
      "newer": "source_b: it reflects the Oct 1, 2026 merger, and the NC Medicaid merger notice lists Cabarrus. The DHHS directory is undated and still says Partners. Use Vaya Partners."
    },
    {
      "county": "All 46 other Vaya Partners counties (Alamance through Yancey, excluding Cabarrus)",
      "source_a": "NC DHHS LME/MCO Directory https://www.ncdhhs.gov/providers/lme-mco-directory (undated)",
      "plan_a": "Partners (provider line 877-398-4145; 901 S. New Hope Road, Gastonia)",
      "source_b": "NC Medicaid Plans FAQ https://www.ncmedicaidplans.gov/en/get-answers and NC Medicaid merger notice https://medicaid.ncdhhs.gov/information-regarding-vaya-health-and-partners-health-management-merger/download?attachment (Sept 2026)",
      "plan_b": "Vaya Partners",
      "newer": "source_b: Vaya Health and Partners merged effective Oct 1, 2026. The DHHS directory has the pre-merger name but correctly lists these counties under one plan."
    },
    {
      "county": "New Hanover",
      "source_a": "NC DHHS LME/MCO Directory https://www.ncdhhs.gov/providers/lme-mco-directory (undated)",
      "plan_a": "Trillium Health Resources (printed as \"New, Hanover\", a typo that splits the county name)",
      "source_b": "NC Medicaid Plans FAQ https://www.ncmedicaidplans.gov/en/get-answers",
      "plan_b": "Trillium Health Resources",
      "newer": "No plan conflict; it is a formatting error. Match on the full name New Hanover when parsing."
    },
    {
      "county": "All 47 Vaya Partners counties",
      "source_a": "NC Medicaid Tailored Plans page https://medicaid.ncdhhs.gov/tailored-plans (last modified 11/14/2025)",
      "plan_a": "Lists Vaya Health / Vaya Total Care and Partners Health Management as separate plans (no county list)",
      "source_b": "NC Medicaid Plans FAQ https://www.ncmedicaidplans.gov/en/get-answers and NC Medicaid merger notice (Sept 2026)",
      "plan_b": "Vaya Partners",
      "newer": "source_b. The Tailored Plans page was last modified 11/14/2025, before the merger, so it is out of date."
    }
  ],
  "plans": {
    "Alliance Health": {
      "providerPhone": "855-759-9700 (Provider Support Line, Mon-Sat 7 a.m.-6 p.m.)",
      "website": "https://www.alliancehealthplan.org/providers/",
      "centralOffice": "5200 W. Paramount Parkway, Suite 200, Morrisville, NC 27560 (DHHS directory prints it without \"W.\")",
      "umPhone": "855-759-9700 (Prior Authorizations/Notifications - Clinical Resources); PA fax 919-651-8691; phone menu option NOT VERIFIED",
      "umEmail": "NOT IN SOURCES (no UM or prior authorization email is published on the Provider Quick Reference Guide)",
      "providerNetworkEmail": "NetworkRelations@AllianceHealthPlan.org (closed network and contracting questions); Enrollment@AllianceHealthPlan.org (Notice of Change submissions)",
      "portalLabel": "Alliance Health Provider Portal Single Sign-On (access through ACSSupport@AllianceHealthPlan.org)",
      "portalUrl": "https://alliancehealth.okta.com/",
      "newProviderPage": "https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/",
      "acceptingPeerSupport": "no",
      "acceptingSAIOP": "yes",
      "acceptingSACOT": "yes",
      "needsPageUrl": "https://www.alliancehealthplan.org/providers/network/service-needs/",
      "asOf": "2026-10-18",
      "sources": [
        "https://www.alliancehealthplan.org/providers/network/provider-quick-reference-guide/",
        "https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/",
        "https://www.alliancehealthplan.org/providers/network/service-needs/",
        "https://www.alliancehealthplan.org/provider-updates/mandatory-closed-network-for-select-behavioral-health-services-effective-july-2-2026/",
        "https://www.alliancehealthplan.org/provider-updates/important-alliance-updates/",
        "https://www.alliancehealthplan.org/providers/",
        "https://www.ncdhhs.gov/providers/lme-mco-directory",
        "https://www.ncmedicaidplans.gov/en/get-answers"
      ],
      "appValueChecks": [
        {"field": "providerPhone", "appValue": "1-855-759-9700", "result": "CONFIRMED", "correct": "855-759-9700"},
        {"field": "website", "appValue": "https://www.alliancehealthplan.org/providers/", "result": "CONFIRMED", "correct": "https://www.alliancehealthplan.org/providers/ (page title: Provider Central)"},
        {"field": "centralOffice", "appValue": "5200 W. Paramount Parkway, Suite 200, Morrisville, NC 27560", "result": "CONFIRMED", "correct": "5200 W. Paramount Parkway, Suite 200, Morrisville, NC 27560"},
        {"field": "umPhone", "appValue": "1-855-759-9700 (Option 2)", "result": "NOT VERIFIED", "correct": "855-759-9700 confirmed for prior authorizations; the Option 2 menu choice is not on any page reviewed. Call to confirm the menu."},
        {"field": "umEmail", "appValue": "ACSSupport@AllianceHealthPlan.org", "result": "CORRECTED", "correct": "ACSSupport@AllianceHealthPlan.org is for portal access and ACS support, not UM. No UM email is published; use 855-759-9700 or fax 919-651-8691."},
        {"field": "portalLabel", "appValue": "Alliance Provider Central Portal", "result": "CORRECTED", "correct": "Alliance Health Provider Portal Single Sign-On. Provider Central is the public website section, which says no login is needed."},
        {"field": "portalUrl", "appValue": "https://alliancehealth.okta.com/", "result": "CONFIRMED", "correct": "https://alliancehealth.okta.com/"},
        {"field": "Combined entry 'Partners Health / Alliance Health' (Mecklenburg, Cabarrus, Union, Gaston corridor)", "appValue": "Partners: 1-877-398-4145 | Alliance: 1-855-759-9700; PAS@PartnersBHM.org / ACSSupport@AllianceHealthPlan.org", "result": "CORRECTED", "correct": "Delete this entry. No plan is shared between two LME/MCOs. Mecklenburg = Alliance Health; Cabarrus, Union and Gaston = Vaya Partners. PAS@PartnersBHM.org was not found on any page reviewed (NOT VERIFIED)."}
      ]
    },
    "Trillium Health Resources": {
      "providerPhone": "1-855-250-1539 (Provider Support Services, Mon-Sat 7 a.m.-6 p.m.)",
      "website": "https://www.trilliumhealthresources.org/",
      "centralOffice": "1019 WH Smith Blvd., Greenville, NC 27834 (physical); mailing: PO Box 12797, Durham, NC 27709 (mailing address change effective July 20, 2026)",
      "umPhone": "1-855-250-1539 (Provider Support Service Line; also used for authorizations and peer-to-peer reviews); UM fax 252-215-6875",
      "umEmail": "NOT IN SOURCES (no UM-specific email published)",
      "providerNetworkEmail": "NetworkServicesSupport@TrilliumNC.org (provider support and requests to join the network)",
      "portalLabel": "Tailored Plan Provider Portal (Tailored Plan auths and claims); Provider Direct (NC Medicaid Direct and State-Funded)",
      "portalUrl": "https://www.trilliumhealthresources.org/for-providers/provider-contact-information-and-portals (portal hub; the direct login URLs are not shown in page text)",
      "newProviderPage": "https://www.trilliumhealthresources.org/contracting-information",
      "acceptingPeerSupport": "no",
      "acceptingSAIOP": "yes",
      "acceptingSACOT": "yes",
      "needsPageUrl": "https://www.trilliumhealthresources.org/current-service-needs",
      "asOf": "2026-10-18",
      "sources": [
        "https://www.trilliumhealthresources.org/current-service-needs",
        "https://www.trilliumhealthresources.org/contracting-information",
        "https://www.trilliumhealthresources.org/for-providers/provider-contact-information-and-portals",
        "https://www.trilliumhealthresources.org/explore-trillium/contact-us/corporate-information",
        "https://www.trilliumhealthresources.org/sites/default/files/docs/Provider-documents/Provider-Manual/Trillium-TP-Provider-Manual.pdf",
        "https://www.ncdhhs.gov/providers/lme-mco-directory",
        "https://www.ncmedicaidplans.gov/en/get-answers"
      ],
      "appValueChecks": [
        {"field": "providerPhone", "appValue": "1-855-250-1539", "result": "CONFIRMED", "correct": "1-855-250-1539"},
        {"field": "website", "appValue": "https://www.trilliumhealthresources.org/", "result": "CONFIRMED", "correct": "https://www.trilliumhealthresources.org/"},
        {"field": "centralOffice", "appValue": "1019 WH Smith Blvd, Greenville, NC 27834 (Mailing: PO Box 12797, Durham, NC 27709)", "result": "CONFIRMED", "correct": "1019 WH Smith Blvd., Greenville, NC 27834; mailing PO Box 12797, Durham, NC 27709"},
        {"field": "umPhone", "appValue": "1-855-250-1539 (ext. 6875)", "result": "CORRECTED", "correct": "1-855-250-1539 with no published extension. 6875 matches the UM fax number 252-215-6875, not a phone extension."},
        {"field": "umEmail", "appValue": "Info@TrilliumNC.org", "result": "CORRECTED", "correct": "Info@TrilliumNC.org is the general inquiries address, not UM. No UM email is published; use NetworkServicesSupport@TrilliumNC.org or 1-855-250-1539."},
        {"field": "portalLabel", "appValue": "Trillium Provider Portal", "result": "CORRECTED", "correct": "Tailored Plan Provider Portal (Tailored Plan) and Provider Direct (Medicaid Direct and State-Funded)"},
        {"field": "portalUrl", "appValue": "https://www.trilliumhealthresources.org/for-providers", "result": "CORRECTED", "correct": "https://www.trilliumhealthresources.org/for-providers/provider-contact-information-and-portals (portal hub). Direct login URLs: NOT VERIFIED; the Sept 2025 Quick Reference Guide lists ncinno.org for Provider Direct."}
      ]
    },
    "Vaya Partners": {
      "providerPhone": "1-866-990-9712 (ACCESS Provider Services / Provider Support Service Line, Mon-Sat 7 a.m.-6 p.m.)",
      "website": "https://providers.vayapartners.org/",
      "centralOffice": "Two addresses listed without a 'central office' label: 200 Ridgefield Court, Suite 218, Asheville, NC 28806 (mailing) and 901 S. New Hope Road, Gastonia, NC 28054",
      "umPhone": "1-800-893-6246 ext. 1515 (behavioral health); ext. 1526 (physical health)",
      "umEmail": "UM@VayaPartners.org",
      "providerNetworkEmail": "ProviderEnrollment@VayaPartners.org (Provider Enrollment Services Team, 1-855-432-9139); general: Provider.Info@VayaPartners.org",
      "portalLabel": "Vaya Partners Provider Portal (hub page; links ProviderCONNECT Portal, EviCore, NEMT, Pharmacy and Vision portals)",
      "portalUrl": "https://providers.vayapartners.org/portal/",
      "newProviderPage": "https://providers.vayapartners.org/enrollment/",
      "acceptingPeerSupport": "no",
      "acceptingSAIOP": "yes",
      "acceptingSACOT": "yes",
      "needsPageUrl": "NOT IN SOURCES (no network-need or service-needs page found; the Provider Operations Manual says needs may be posted in the Provider Communication Bulletin or on the website)",
      "asOf": "2026-10-18",
      "sources": [
        "https://providers.vayapartners.org/enrollment/",
        "https://providers.vayapartners.org/behavioral-health/",
        "https://providers.vayapartners.org/contact/",
        "https://providers.vayapartners.org/portal/",
        "https://resources.vayapartners.org/wp-content/uploads/Vaya_Partners_Provider_Operations_Manual_1.0_20261001.pdf",
        "https://resources.vayapartners.org/",
        "https://vayapartners.org/tailored-plan/",
        "https://medicaid.ncdhhs.gov/information-regarding-vaya-health-and-partners-health-management-merger/download?attachment",
        "https://www.ncmedicaidplans.gov/en/get-answers",
        "https://www.ncdhhs.gov/providers/lme-mco-directory"
      ],
      "appValueChecks": [
        {"field": "Vaya Health providerPhone", "appValue": "1-866-990-9712", "result": "CONFIRMED", "correct": "1-866-990-9712 (now Vaya Partners)"},
        {"field": "Vaya Health website", "appValue": "https://providers.vayahealth.com/", "result": "CORRECTED", "correct": "https://providers.vayapartners.org/ (providers.vayahealth.com is now a legacy site)"},
        {"field": "Vaya Health address", "appValue": "200 Ridgefield Court, Suite 218, Asheville, NC 28806", "result": "CONFIRMED", "correct": "200 Ridgefield Court, Suite 218, Asheville, NC 28806 (mailing). Vaya Partners also lists 901 S. New Hope Road, Gastonia, NC 28054."},
        {"field": "Vaya Health umPhone", "appValue": "1-800-893-6246 (ext. 1515)", "result": "CONFIRMED", "correct": "1-800-893-6246 ext. 1515 (behavioral health)"},
        {"field": "Vaya Health umEmail", "appValue": "UM@vayahealth.com", "result": "CORRECTED", "correct": "UM@VayaPartners.org"},
        {"field": "Vaya Health portal", "appValue": "Vaya Provider Portal (https://providers.vayahealth.com/provider-portal)", "result": "CORRECTED", "correct": "Vaya Partners Provider Portal (https://providers.vayapartners.org/portal/)"},
        {"field": "Partners providerPhone", "appValue": "1-877-398-4145", "result": "CORRECTED", "correct": "1-866-990-9712. 1-877-398-4145 is the pre-merger Partners line and still appears in the undated DHHS directory."},
        {"field": "Partners website", "appValue": "https://providers.partnersbhm.org/", "result": "CORRECTED", "correct": "https://providers.vayapartners.org/ (providers.partnersbhm.org is legacy)"},
        {"field": "Partners address", "appValue": "901 S. New Hope Road, Gastonia, NC 28054", "result": "CONFIRMED", "correct": "901 S. New Hope Road, Gastonia, NC 28054 (listed by Vaya Partners)"},
        {"field": "Partners umPhone", "appValue": "1-877-398-4145", "result": "CORRECTED", "correct": "1-800-893-6246 ext. 1515 (behavioral health UM)"},
        {"field": "Partners umEmail", "appValue": "BHIDDManualAuthorizations@partnersbhm.org", "result": "CORRECTED", "correct": "UM@VayaPartners.org. The Partners address was not found on any Vaya Partners page reviewed."},
        {"field": "Partners portal", "appValue": "ProviderCONNECT Portal (https://providers.partnersbhm.org/provider-portal-help/)", "result": "CORRECTED", "correct": "Vaya Partners Provider Portal hub (https://providers.vayapartners.org/portal/). It lists ProviderCONNECT Portal without a URL; whether ProviderCONNECT is still active for dates of service on or after Oct 1, 2026 is NOT VERIFIED."}
      ]
    }
  },
  "peer_support_closed_network": {
    "effectiveDate": "2026-07-07",
    "governingSource": "S.L. 2026-41 (Senate Bill 257, 2026 Appropriations Act), Section 9E.22(b), which adds G.S. 108D-22(e) Mandatory Closed Networks; Section 9E.22(d) sets the effective date. https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-41.pdf",
    "quote": "Session law: \"SECTION 9E.22.(d) This section is effective when it becomes law.\" Signature page: \"ratified this the 2nd day of July, 2026. Approved 10:30 a.m. this 7th day of July, 2026\". NC Medicaid fact sheet (modified 10/01/2026): \"These requirements are effective as of July 7, 2026.\"",
    "conflict": "Alliance Health (notice dated 07/02/2026 and its Provider Enrollment page) says \"effective July 2, 2026\". July 2 is when the General Assembly ratified the bill. The section took effect when it became law, July 7, 2026 (Governor's approval). NC Medicaid, Vaya Partners and legacy Vaya all use July 7. The session law governs, so use July 7, 2026. Also: the ncleg.gov G.S. 108D-22 web page does not yet show subsection (e) (its history ends at S.L. 2026-1), so cite the session law. The NCGA bill summary says community support team is closed for all PHPs, but the enacted text closes CST only for the Children and Families Specialty Plan (G.S. 108D-24(b)(5))."
  }
}
```

## Sources

| Title | Publisher | URL | Date | Type |
|---|---|---|---|---|
| Session Law 2026-41 (SB 257), Sec. 9E.22 | NC General Assembly | SL2026-41.pdf[ncleg.gov](https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-41.pdf?share_frome=aipt) | Ratified Jul 2, 2026; approved Jul 7, 2026 | Primary |
| 2026 Appropriations Act bill summary | NC General Assembly | [Bill summary](https://dashboard.ncleg.gov/api/Services/BillSummary/2025/S257-SMTR-65(sl)-v-4) | 2026 | Primary (summary, not law) |
| G.S. 108D-22 and 108D-23 | NC General Assembly | 108D-22[ncleg.gov](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108D/GS_108D-22.html?share_frome=aipt), 108D-23[ncleg.gov](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108D/GS_108D-23.html?share_frome=aipt) | Not yet updated for S.L. 2026-41 | Primary |
| Mandatory Closed Networks fact sheet | NC Medicaid | Fact sheet[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers/provider-playbook-medicaid-managed-care/fact-sheets/mandatory-closed-networks?share_frome=aipt) | Modified 10/01/2026 | Primary |
| Vaya/Partners merger notice | NC Medicaid | Merger notice[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/information-regarding-vaya-health-and-partners-health-management-merger/download?attachment=&share_frome=aipt) | Sept 2026 | Primary |
| Tailored Plans page | NC Medicaid | Tailored Plans[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/tailored-plans?share_frome=aipt) | Modified 11/14/2025 (out of date) | Primary |
| Frequently asked questions (county lists) | NC Medicaid Managed Care | Get answers[ncmedicaidplans.gov](https://www.ncmedicaidplans.gov/en/get-answers?share_frome=aipt) | Undated (post-merger) | Primary |
| LME/MCO Directory | NC DHHS | Directory[ncdhhs.gov](https://www.ncdhhs.gov/providers/lme-mco-directory?share_frome=aipt) | Undated | Primary |
| Provider Enrollment; Current Service Needs; Quick Reference Guide; Closed Network notice; Provider Central | Alliance Health | Enrollment[alliancehealthplan.org](https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/?share_frome=aipt), Needs[alliancehealthplan.org](https://www.alliancehealthplan.org/providers/network/service-needs/?share_frome=aipt), QRG[alliancehealthplan.org](https://www.alliancehealthplan.org/providers/network/provider-quick-reference-guide/?share_frome=aipt), Notice[alliancehealthplan.org](https://www.alliancehealthplan.org/provider-updates/mandatory-closed-network-for-select-behavioral-health-services-effective-july-2-2026/?share_frome=aipt), Provider Central[alliancehealthplan.org](https://www.alliancehealthplan.org/providers/?share_frome=aipt) | Notice 07/02/2026; others undated | Primary (plan) |
| Current Service Needs; Contracting; Contacts and Portals; Corporate Info; Provider Manual | Trillium | Needs[trilliumhealthresources.org](https://www.trilliumhealthresources.org/current-service-needs?share_frome=aipt), Contracting[trilliumhealthresources.org](https://www.trilliumhealthresources.org/contracting-information?share_frome=aipt), Portals[trilliumhealthresources.org](https://www.trilliumhealthresources.org/for-providers/provider-contact-information-and-portals?share_frome=aipt), Corporate[trilliumhealthresources.org](https://www.trilliumhealthresources.org/explore-trillium/contact-us/corporate-information?share_frome=aipt), Manual[trilliumhealthresources.org](https://www.trilliumhealthresources.org/sites/default/files/docs/Provider-documents/Provider-Manual/Trillium-TP-Provider-Manual.pdf?share_frome=aipt) | Verified Oct 5 and Oct 8, 2026; Jul 6, 2026 | Primary (plan) |
| Enrollment; BH Network; Contact; Portal; Tailored Plan | Vaya Partners | Enrollment[providers.vayapartners.org](https://providers.vayapartners.org/enrollment/?share_frome=aipt), BH Network[providers.vayapartners.org](https://providers.vayapartners.org/behavioral-health/?share_frome=aipt), Contact[providers.vayapartners.org](https://providers.vayapartners.org/contact/?share_frome=aipt), Portal[providers.vayapartners.org](https://providers.vayapartners.org/portal/?share_frome=aipt), Counties[vayapartners.org](https://vayapartners.org/tailored-plan/?share_frome=aipt) | Undated | Primary (plan) |
| Provider Operations Manual v1.0 | Vaya Partners | POM[resources.vayapartners.org](https://resources.vayapartners.org/wp-content/uploads/Vaya_Partners_Provider_Operations_Manual_1.0_20261001.pdf?share_frome=aipt) | Oct 1, 2026 | Primary (plan) |
| Provider Communication Bulletin Issue 3 | Vaya Health (legacy) | PCB[providers.vayahealth.com](https://providers.vayahealth.com/wp-content/uploads/2026/07/PCB_Issue_3_20260708.pdf?share_frome=aipt) | Jul 8, 2026 | Primary (plan, legacy) |
| Changes to RB-BHT and Peer Support | Partners (legacy) | Notice[providers.partnersbhm.org](https://providers.partnersbhm.org/changes-to-rb-bht-and-peer-support-services/?share_frome=aipt) | Jul 8, 2026; updated Jul 13 | Primary (plan, legacy) |
| Better Together merger page | Vaya Partners | Merger hub[resources.vayapartners.org](https://resources.vayapartners.org/?share_frome=aipt) | Merger effective Oct 1, 2026 | Primary (plan) |

## Open questions

- **"Yes" for SAIOP and SACOT means the network is open to applications.** It does not guarantee a contract. Alliance reviews each application "for specific network need and eligibility" and replies within five business days. Trillium lists SAIOP and SACOT needs only in Dare and Hyde. Ask each plan's network team before you sign a lease.[alliancehealthplan.org](https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/?share_frome=aipt)[trilliumhealthresources.org](https://www.trilliumhealthresources.org/current-service-needs?share_frome=aipt)
- **Peer support "no" is not an absolute ban.** All three plans say they consider new peer support requests case by case, based on network need. Trillium says it is "not accepting applications to expand the network for this service at this time". Contacts: NetworkRelations@AllianceHealthPlan.org, NetworkServicesSupport@TrilliumNC.org, and ProviderEnrollment@VayaPartners.org / 1-855-432-9139.[trilliumhealthresources.org](https://www.trilliumhealthresources.org/current-service-needs?share_frome=aipt)
- **Alliance UM details.** Call 855-759-9700 to confirm whether "Option 2" is the authorization menu choice and whether there is a UM email.
- **Portal login URLs.** Trillium's Tailored Plan Provider Portal and Provider Direct, and Vaya Partners' ProviderCONNECT, are linked without a visible URL. Confirm them with Trillium (1-855-250-1539) and Vaya Partners (1-866-990-9712).
- **Vaya Partners service-needs page.** None was found. Ask Vaya Partners Provider Enrollment where it posts closed-network needs.
- **Undated DHHS directory.** It still says "Partners" and leaves out Cabarrus. The NC Medicaid Ombudsman (1-866-304-7062, as listed by Trillium) or NC DHHS can confirm when it will be updated.[trilliumhealthresources.org](https://www.trilliumhealthresources.org/for-providers/provider-contact-information-and-portals?share_frome=aipt)
- **Combined app entry.** "PAS@PartnersBHM.org" from the "Partners Health / Alliance Health" entry did not appear on any page I opened.

This is research, not legal advice. Have a healthcare attorney confirm how closed-network rules affect your contracting plans.