> From: https://www.perplexity.ai/computer/tasks/3c6167f8-0ea0-4277-afe7-d0ec1a9af035

# you asked

message time: 2026-10-18 23:35:21

RESEARCH RULES (apply to every answer)
- It is late October 2026. Use official or primary sources only: NC DHHS, NC Medicaid, NCTracks, DHSR, NC General Assembly, federal agencies, and the plans' own provider pages. Open each page before citing it. Blogs, consultants and forums count only as secondary, and must be labeled that way.
- Never guess or fill a gap. Do not invent phone numbers, emails, addresses, URLs, fees, dates or section numbers. If you cannot verify something on a source you opened, write "NOT VERIFIED" and say what to check and who to call.
- Give the URL and the date shown on the page (or "undated") for every fact. Quote the key sentence, 25 words or fewer, for anything that decides a question.
- If sources conflict, report both with their dates and say which is newer and which is the policy text.
- Values labeled "APP CURRENTLY SHOWS" come from my dashboard and may be wrong. Mark each one CONFIRMED, CORRECTED (give the right value) or NOT VERIFIED.
- Return valid JSON in a json code block exactly as specified, then a short SOURCES table (title, publisher, URL, date, primary or secondary), then OPEN QUESTIONS. Plain text inside JSON strings, one line each, escaped double quotes, no citation markers like [1] inside the JSON. No commentary before the JSON.
- This is research, not legal advice.

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
  Region 1: Impact Health | contact Tamara Smith (Executive Director) | phone (828) 357-8170 / (800) 581-0182 | email [t.smith@impacthealth.org](mailto:t.smith@impacthealth.org) | website [https://impacthealth.org/](https://impacthealth.org/) | address PO Box 8427, Asheville, NC 28814
  Region 2: Trillium Health Resources | contact Region 2 ROOTS Lead Coordinator | phone 1-855-250-1539 | email [Region2NCRootsHub@trilliumnc.org](mailto:Region2NCRootsHub@trilliumnc.org) | website [https://www.trilliumhealthresources.org/](https://www.trilliumhealthresources.org/) | address 1019 WH Smith Blvd, Greenville, NC 27834
  Region 3: Vaya Health | contact NC ROOTS Region 3 Strategy Director | phone 1-800-962-9003 | email [RHTP@vayahealth.com](mailto:RHTP@vayahealth.com) | website [https://www.vayahealth.com/](https://www.vayahealth.com/) | address 200 Ridgefield Court, Suite 218, Asheville, NC 28806
  Region 4: UNC Health | contact NC ROOTS Region 4 Team | phone (984) 974-1000 / 1-800-806-1964 | email [NCROOTSRegion4@unchealth.unc.edu](mailto:NCROOTSRegion4@unchealth.unc.edu) | website [https://www.unchealth.org/](https://www.unchealth.org/) | address 101 Manning Drive, Chapel Hill, NC 27514
  Region 5: Trillium Health Resources | contact Region 5 ROOTS Lead | phone 1-855-250-1539 | email [Region5NCRootsHub@trilliumnc.org](mailto:Region5NCRootsHub@trilliumnc.org) | website [https://www.trilliumhealthresources.org/](https://www.trilliumhealthresources.org/) | address 1019 WH Smith Blvd, Greenville, NC 27834
  Region 6: Access East, Inc. | contact Access East RHTP Hub Team | phone (252) 847-3027 | email [Info-AccessEast@accesseast.org](mailto:Info-AccessEast@accesseast.org) | website [https://accesseast.org/](https://accesseast.org/) | address 2410 S. Charles Blvd, Greenville, NC 27858
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

---

# perplexity response

```json
{
  "regionCounty": {"Alamance": 4, "Alexander": 3, "Alleghany": 2, "Anson": 3, "Ashe": 2, "Avery": 1, "Beaufort": 6, "Bertie": 6, "Bladen": 5, "Brunswick": 5, "Buncombe": 1, "Burke": 1, "Cabarrus": 3, "Caldwell": 1, "Camden": 6, "Carteret": 6, "Caswell": 4, "Catawba": 3, "Chatham": 4, "Cherokee": 1, "Chowan": 6, "Clay": 1, "Cleveland": 3, "Columbus": 5, "Craven": 6, "Cumberland": 5, "Currituck": 6, "Dare": 6, "Davidson": 2, "Davie": 2, "Duplin": 6, "Durham": 4, "Edgecombe": 6, "Forsyth": 2, "Franklin": 4, "Gaston": 3, "Gates": 6, "Graham": 1, "Granville": 4, "Greene": 6, "Guilford": 2, "Halifax": 6, "Harnett": 5, "Haywood": 1, "Henderson": 1, "Hertford": 6, "Hoke": 5, "Hyde": 6, "Iredell": 3, "Jackson": 1, "Johnston": 4, "Jones": 6, "Lee": 5, "Lenoir": 6, "Lincoln": 3, "Macon": 1, "Madison": 1, "Martin": 6, "McDowell": 1, "Mecklenburg": 3, "Mitchell": 1, "Montgomery": 5, "Moore": 5, "Nash": 4, "New Hanover": 5, "Northampton": 6, "Onslow": 6, "Orange": 4, "Pamlico": 6, "Pasquotank": 6, "Pender": 5, "Perquimans": 6, "Person": 4, "Pitt": 6, "Polk": 1, "Randolph": 2, "Richmond": 5, "Robeson": 5, "Rockingham": 2, "Rowan": 3, "Rutherford": 1, "Sampson": 5, "Scotland": 5, "Stanly": 3, "Stokes": 2, "Surry": 2, "Swain": 1, "Transylvania": 1, "Tyrrell": 6, "Union": 3, "Vance": 4, "Wake": 4, "Warren": 4, "Washington": 6, "Watauga": 2, "Wayne": 6, "Wilkes": 2, "Wilson": 4, "Yadkin": 2, "Yancey": 1},
  "regionDifferences": [],
  "hubs": {
    "1": {
      "organization": "Impact Health",
      "contactPerson": "Tamara Smith",
      "title": "Executive Assistant - Programs (title from Impact Health staff page; NCDHHS hub page lists her as point of contact with no title)",
      "phone": "828-278-9900 (Impact Health general line; no ROOTS-specific phone published)",
      "email": "t.smith@impacthealth.org",
      "address": "P.O. Box 5378, Asheville, NC 28813",
      "website": "https://impacthealth.org/rural-health/",
      "regionsServed": [ncdhhs.gov](https://www.ncdhhs.gov/news/press-releases/2026/05/01/ncdhhs-selects-nc-roots-hub-leads-strengthen-rural-health-care-across-north-carolina?share_frome=aipt),
      "checks": [
        {"field": "organization", "appValue": "Impact Health", "result": "CONFIRMED", "correct": "Impact Health"},
        {"field": "contactPerson", "appValue": "Tamara Smith", "result": "CONFIRMED", "correct": "Tamara Smith (NCDHHS hub page: Point of contact: Tamara Smith)"},
        {"field": "title", "appValue": "Executive Director", "result": "CORRECTED", "correct": "Executive Assistant - Programs per impacthealth.org/our-people/tamara-smith; NCDHHS page gives no title"},
        {"field": "phone", "appValue": "(828) 357-8170 / (800) 581-0182", "result": "CORRECTED", "correct": "828-278-9900 (Impact Health general line on contact and rural-health pages); app numbers NOT VERIFIED on any official page"},
        {"field": "email", "appValue": "t.smith@impacthealth.org", "result": "CONFIRMED", "correct": "t.smith@impacthealth.org"},
        {"field": "website", "appValue": "https://impacthealth.org/", "result": "CORRECTED", "correct": "https://impacthealth.org/rural-health/ (ROOTS page linked from NCDHHS)"},
        {"field": "address", "appValue": "PO Box 8427, Asheville, NC 28814", "result": "CORRECTED", "correct": "P.O. Box 5378, Asheville, NC 28813"}
      ],
      "sources": ["https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-organizations-orchestrating-transformation-sustainability-roots-hub-leads", "https://impacthealth.org/rural-health/", "https://impacthealth.org/contact/", "https://impacthealth.org/our-people/tamara-smith/"]
    },
    "2": {
      "organization": "Trillium Health Resources",
      "contactPerson": "NOT VERIFIED - no named person published; use hub email",
      "title": "NOT VERIFIED",
      "phone": "1-855-250-1539 (Trillium Provider Support Services; not a ROOTS-specific line)",
      "email": "Region2NCRootsHub@TrilliumNC.org",
      "address": "1019 WH Smith Blvd., Greenville, NC 27834 (mailing: PO Box 12797, Durham, NC 27709)",
      "website": "https://www.trilliumhealthresources.org/NC-ROOTS-Region-2",
      "regionsServed": [2, 5],
      "checks": [
        {"field": "organization", "appValue": "Trillium Health Resources", "result": "CONFIRMED", "correct": "Trillium Health Resources"},
        {"field": "contactPerson", "appValue": "Region 2 ROOTS Lead Coordinator", "result": "NOT VERIFIED", "correct": "No person or title shown on NCDHHS or Trillium pages; remove the title or label it a generic mailbox"},
        {"field": "phone", "appValue": "1-855-250-1539", "result": "CONFIRMED", "correct": "1-855-250-1539 is Trillium Provider Support Services, not a ROOTS line"},
        {"field": "email", "appValue": "Region2NCRootsHub@trilliumnc.org", "result": "CONFIRMED", "correct": "Region2NCRootsHub@TrilliumNC.org (Trillium page and NCDHHS display text; NCDHHS mailto link points to Region2RootsHub@trilliumnc.org)"},
        {"field": "website", "appValue": "https://www.trilliumhealthresources.org/", "result": "CORRECTED", "correct": "https://www.trilliumhealthresources.org/NC-ROOTS-Region-2"},
        {"field": "address", "appValue": "1019 WH Smith Blvd, Greenville, NC 27834", "result": "CONFIRMED", "correct": "1019 WH Smith Blvd., Greenville, NC 27834 (corporate office); mailing PO Box 12797, Durham, NC 27709"}
      ],
      "sources": ["https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-organizations-orchestrating-transformation-sustainability-roots-hub-leads", "https://www.trilliumhealthresources.org/NC-ROOTS-Region-2", "https://www.trilliumhealthresources.org/explore-trillium/contact-us/corporate-information"]
    },
    "3": {
      "organization": "Vaya Partners (formerly Vaya Health; merged with Partners Health Management effective Oct. 1, 2026)",
      "contactPerson": "NOT VERIFIED - no named person published; use hub email",
      "title": "NOT VERIFIED",
      "phone": "NOT VERIFIED - no ROOTS phone published",
      "email": "RHTP@vayahealth.com",
      "address": "200 Ridgefield Court, Suite 218, Asheville, NC 28806",
      "website": "https://rhtp.vayapartners.org/",
      "regionsServed": [ncdhhs.gov](https://www.ncdhhs.gov/public-notice-ncdhhs-requests-applicants-nc-rural-health-transformation-roots-hub-leads/open?share_frome=aipt),
      "checks": [
        {"field": "organization", "appValue": "Vaya Health", "result": "CORRECTED", "correct": "Vaya Partners since Oct. 1, 2026 merger; NCDHHS hub page still says Vaya Health"},
        {"field": "contactPerson", "appValue": "NC ROOTS Region 3 Strategy Director", "result": "NOT VERIFIED", "correct": "No person or title shown on NCDHHS or Vaya ROOTS pages"},
        {"field": "phone", "appValue": "1-800-962-9003", "result": "NOT VERIFIED", "correct": "Not found on NCDHHS hub page or Vaya ROOTS site; confirm with Vaya Partners"},
        {"field": "email", "appValue": "RHTP@vayahealth.com", "result": "CONFIRMED", "correct": "RHTP@vayahealth.com"},
        {"field": "website", "appValue": "https://www.vayahealth.com/", "result": "CORRECTED", "correct": "https://rhtp.vayapartners.org/ (Region 3 ROOTS site)"},
        {"field": "address", "appValue": "200 Ridgefield Court, Suite 218, Asheville, NC 28806", "result": "CONFIRMED", "correct": "200 Ridgefield Court, Suite 218, Asheville, NC 28806"}
      ],
      "sources": ["https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-organizations-orchestrating-transformation-sustainability-roots-hub-leads", "https://rhtp.vayapartners.org/", "https://vayapartners.org/office-locations/", "https://www.vayahealth.com/health-plans/nc-medicaid-direct/appeals/", "https://providers.vayahealth.com/wp-content/uploads/2026/09/pcb-09-10-26-issue-17.pdf"]
    },
    "4": {
      "organization": "UNC Health (press release names University of North Carolina Hospitals)",
      "contactPerson": "NOT VERIFIED - no named person published; use hub email",
      "title": "NOT VERIFIED",
      "phone": "984-974-1000 (UNC Health main line; not ROOTS-specific)",
      "email": "NCROOTSRegion4@unchealth.unc.edu",
      "address": "101 Manning Drive, Chapel Hill, NC 27514 (UNC Health main address)",
      "website": "https://www.unchealth.org/ncroots",
      "regionsServed": [ncdhhs.gov](https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/nc-rural-health-transformation-program-frequently-asked-questions?share_frome=aipt),
      "checks": [
        {"field": "organization", "appValue": "UNC Health", "result": "CONFIRMED", "correct": "UNC Health (hub page); University of North Carolina Hospitals (May 1, 2026 press release)"},
        {"field": "contactPerson", "appValue": "NC ROOTS Region 4 Team", "result": "NOT VERIFIED", "correct": "Not shown; generic label only"},
        {"field": "phone", "appValue": "(984) 974-1000 / 1-800-806-1964", "result": "CORRECTED", "correct": "984-974-1000 confirmed as UNC Health main line; 1-800-806-1964 NOT VERIFIED; neither is ROOTS-specific"},
        {"field": "email", "appValue": "NCROOTSRegion4@unchealth.unc.edu", "result": "CONFIRMED", "correct": "NCROOTSRegion4@unchealth.unc.edu"},
        {"field": "website", "appValue": "https://www.unchealth.org/", "result": "CORRECTED", "correct": "https://www.unchealth.org/ncroots"},
        {"field": "address", "appValue": "101 Manning Drive, Chapel Hill, NC 27514", "result": "CONFIRMED", "correct": "101 Manning Drive, Chapel Hill, NC 27514 (main address, not ROOTS-specific)"}
      ],
      "sources": ["https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-organizations-orchestrating-transformation-sustainability-roots-hub-leads", "https://www.ncdhhs.gov/news/press-releases/2026/05/01/ncdhhs-selects-nc-roots-hub-leads-strengthen-rural-health-care-across-north-carolina", "https://www.unchealth.org/ncroots", "https://www.unchealth.org/contact-us"]
    },
    "5": {
      "organization": "Trillium Health Resources",
      "contactPerson": "NOT VERIFIED - no named person published; use hub email",
      "title": "NOT VERIFIED",
      "phone": "1-855-250-1539 (Trillium Provider Support Services; not a ROOTS-specific line)",
      "email": "Region5NCRootsHub@TrilliumNC.org",
      "address": "1019 WH Smith Blvd., Greenville, NC 27834 (mailing: PO Box 12797, Durham, NC 27709)",
      "website": "https://www.trilliumhealthresources.org/NC-ROOTS-Region-5",
      "regionsServed": [2, 5],
      "checks": [
        {"field": "organization", "appValue": "Trillium Health Resources", "result": "CONFIRMED", "correct": "Trillium Health Resources"},
        {"field": "contactPerson", "appValue": "Region 5 ROOTS Lead", "result": "NOT VERIFIED", "correct": "No person or title shown; generic mailbox only"},
        {"field": "phone", "appValue": "1-855-250-1539", "result": "CONFIRMED", "correct": "1-855-250-1539 is Trillium Provider Support Services, not a ROOTS line"},
        {"field": "email", "appValue": "Region5NCRootsHub@trilliumnc.org", "result": "CONFIRMED", "correct": "Region5NCRootsHub@TrilliumNC.org (Trillium page and NCDHHS display text; NCDHHS mailto link points to Region5RootsHub@trilliumnc.org)"},
        {"field": "website", "appValue": "https://www.trilliumhealthresources.org/", "result": "CORRECTED", "correct": "https://www.trilliumhealthresources.org/NC-ROOTS-Region-5"},
        {"field": "address", "appValue": "1019 WH Smith Blvd, Greenville, NC 27834", "result": "CONFIRMED", "correct": "1019 WH Smith Blvd., Greenville, NC 27834"}
      ],
      "sources": ["https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-organizations-orchestrating-transformation-sustainability-roots-hub-leads", "https://www.trilliumhealthresources.org/NC-ROOTS-Region-5", "https://www.trilliumhealthresources.org/explore-trillium/contact-us/corporate-information"]
    },
    "6": {
      "organization": "Access East, Inc.",
      "contactPerson": "NOT VERIFIED - no named person published; use hub email",
      "title": "NOT VERIFIED",
      "phone": "(252) 847-6809 (Access East main line; no ROOTS-specific phone published)",
      "email": "rhtp@accesseast.org",
      "address": "PO Box 6028, 2410 Stantonsburg Road, Stanton Square, Greenville, NC 27835",
      "website": "https://accesseast.org/access-east-nc-roots-hub/",
      "regionsServed": [trilliumhealthresources.org](https://www.trilliumhealthresources.org/article/trillium-selected-nc-roots-hub?share_frome=aipt),
      "checks": [
        {"field": "organization", "appValue": "Access East, Inc.", "result": "CONFIRMED", "correct": "Access East, Inc."},
        {"field": "contactPerson", "appValue": "Access East RHTP Hub Team", "result": "NOT VERIFIED", "correct": "Not shown; generic label only"},
        {"field": "phone", "appValue": "(252) 847-3027", "result": "CORRECTED", "correct": "(252) 847-6809 main line; 847-3027 is the Certified Marketplace Navigators/ACA line"},
        {"field": "email", "appValue": "Info-AccessEast@accesseast.org", "result": "CORRECTED", "correct": "rhtp@accesseast.org (NCDHHS hub point of contact); Info-AccessEast@ is the general inbox"},
        {"field": "website", "appValue": "https://accesseast.org/", "result": "CORRECTED", "correct": "https://accesseast.org/access-east-nc-roots-hub/"},
        {"field": "address", "appValue": "2410 S. Charles Blvd, Greenville, NC 27858", "result": "CORRECTED", "correct": "PO Box 6028, 2410 Stantonsburg Road, Stanton Square, Greenville, NC 27835"}
      ],
      "sources": ["https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-organizations-orchestrating-transformation-sustainability-roots-hub-leads", "https://accesseast.org/access-east-nc-roots-hub/", "https://accesseast.org/ae-contact-us/"]
    }
  },
  "openFunding": [
    {"name": "Rural Health Innovation Fund (statewide, NCDHHS and NCDIT; about $20M per year; year 1 limited to primary care providers, FQHCs, community health centers and qualifying safety-net providers). Readiness Intake form first, then full application in NCDIT grant portal. Questions: RHIF@nc.gov; NCDIT Broadband 919-754-6733", "region": "Statewide (all 6 regions)", "deadline": "Nov. 16, 2026, 11:59 p.m.; awards expected January 2027", "link": "https://www.ncbroadband.gov/ruralhealthinnovation"},
    {"name": "Region 3 ROOTS Hub interest form (not a grant application; Vaya Partners still finalizing guidelines and funding)", "region": "3", "deadline": "None stated", "link": "https://rhtp.vayapartners.org/"},
    {"name": "Region 1 ROOTS engagement form and newsletter (no open grant posted)", "region": "1", "deadline": "None stated", "link": "https://impacthealth.org/rural-health/"}
  ],
  "statewide": {
    "providerOmbudsman": {"phone": "866-304-7062", "email": "Medicaid.ProviderOmbudsman@dhhs.nc.gov", "hours": "NOT VERIFIED - hours not stated for the provider line; 8 a.m. to 5 p.m. M-F applies to the member line 1-877-201-3750", "sources": ["https://medicaid.ncdhhs.gov/about-nc-medicaid/nc-medicaid-ombudsman", "https://medicaid.ncdhhs.gov/providers"]},
    "medicaidContactCenter": {"phone": "888-245-0179", "email": "NOT VERIFIED - none published", "hours": "Monday-Friday 8 a.m. to 5 p.m., closed State holidays", "sources": ["https://medicaid.ncdhhs.gov/providers"]},
    "nctracksCallCenter": {"phone": "800-688-6696", "email": "NCTracksprovider@nctracks.com", "hours": "8 a.m. to 5 p.m., Monday through Friday, except State-approved holidays; fax 855-710-1965", "sources": ["https://www.nctracks.nc.gov/publicPortal/provider/loadContactUs.action", "https://medicaid.ncdhhs.gov/providers"]},
    "hiea": {"phone": "919-754-6912 (HIEA business office, general inquiries); technical help desk: SAS NC HealthConnex Help Desk 919-531-2700", "email": "hiea@nc.gov (general); HIESupport@sas.com (technical)", "hours": "Business office M-F 8:30 a.m. to 5 p.m.; SAS help desk M-F 8 a.m. to 6 p.m.; after-hours emergencies by phone only", "sources": ["https://hiea.nc.gov/contact"]}
  }
}
```

## SOURCES

| Title | Publisher | URL | Date | Type |
|---|---|---|---|---|
| ROOTS Hub Leads (map and contacts) | NCDHHS | ncdhhs.gov hub leads[ncdhhs.gov](https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-organizations-orchestrating-transformation-sustainability-roots-hub-leads?share_frome=aipt) | No date on page; read Oct 18, 2026 | Primary |
| NCDHHS Selects NC ROOTS Hub Leads | NCDHHS | press release[ncdhhs.gov](https://www.ncdhhs.gov/news/press-releases/2026/05/01/ncdhhs-selects-nc-roots-hub-leads-strengthen-rural-health-care-across-north-carolina?share_frome=aipt) | May 1, 2026 | Primary |
| Medicaid Managed Care regions fact sheet | NC Medicaid | fact sheet[ncdhhs.gov](https://www.ncdhhs.gov/medicaid/medicaid-factsheets-php-2-4-19/download?share_frome=aipt) | 01/2019 | Primary |
| RHTP Grant Opportunities | NCDHHS | grant page[ncdhhs.gov](https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-health-transformation-program-grant-opportunities?share_frome=aipt) | No date on page | Primary |
| Rural Health Innovation Fund | NCDIT Broadband | ncbroadband.gov[ncbroadband.gov](https://www.ncbroadband.gov/ruralhealthinnovation?share_frome=aipt) | Sept 2026 | Primary |
| Governor Stein launches $20M fund | Office of the Governor | press release[governor.nc.gov](https://governor.nc.gov/news/press-releases/2026/09/30/governor-stein-launches-20-million-fund-increase-access-care-rural-north-carolina?share_frome=aipt) | Sept 30, 2026 | Primary |
| Impact Health Rural Health / Contact / Tamara Smith | Impact Health | rural-health[impacthealth.org](https://impacthealth.org/rural-health/?share_frome=aipt), contact[impacthealth.org](https://impacthealth.org/contact/?share_frome=aipt), staff page[impacthealth.org](https://impacthealth.org/our-people/tamara-smith/?share_frome=aipt) | 2025-2026 | Primary (hub lead) |
| Region 2 / Region 5 NC ROOTS | Trillium | Region 2[trilliumhealthresources.org](https://www.trilliumhealthresources.org/NC-ROOTS-Region-2?share_frome=aipt), Region 5[trilliumhealthresources.org](https://www.trilliumhealthresources.org/NC-ROOTS-Region-5?share_frome=aipt), corporate info[trilliumhealthresources.org](https://www.trilliumhealthresources.org/explore-trillium/contact-us/corporate-information?share_frome=aipt) | Oct 2026 | Primary (hub lead) |
| Region 3 RHTP / offices / merger notice | Vaya Partners | rhtp.vayapartners.org[rhtp.vayapartners.org](https://rhtp.vayapartners.org/?share_frome=aipt), offices[vayapartners.org](https://vayapartners.org/office-locations/?share_frome=aipt), provider bulletin[providers.vayahealth.com](https://providers.vayahealth.com/wp-content/uploads/2026/09/pcb-09-10-26-issue-17.pdf?share_frome=aipt) | Sept-Oct 2026 | Primary (hub lead) |
| NC ROOTS Region Four / Contact | UNC Health | ncroots[unchealth.org](https://www.unchealth.org/ncroots?share_frome=aipt), contact[unchealth.org](https://www.unchealth.org/contact-us?share_frome=aipt) | Oct 2026 | Primary (hub lead) |
| ROOTS Hub / Contact Us | Access East | hub page[accesseast.org](https://accesseast.org/access-east-nc-roots-hub/?share_frome=aipt), contact[accesseast.org](https://accesseast.org/ae-contact-us/?share_frome=aipt) | Oct 2026 | Primary (hub lead) |
| NC Medicaid Ombudsman | NC Medicaid | ombudsman page[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/about-nc-medicaid/nc-medicaid-ombudsman?share_frome=aipt) | Last modified 01/05/2026 | Primary |
| Provider Information | NC Medicaid | providers page[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers?share_frome=aipt) | No date on page | Primary |
| Contact Us | NCTracks | NCTracks contact[nctracks.nc.gov](https://www.nctracks.nc.gov/publicPortal/provider/loadContactUs.action?share_frome=aipt) | No date on page (still says "CSRA") | Primary |
| Contact | NC HIEA | hiea.nc.gov/contact[hiea.nc.gov](https://hiea.nc.gov/contact?share_frome=aipt) | No date on page | Primary |

## Key findings

- **Regions:** All 100 counties in the app are in the right region. The NCDHHS hub map data and the 2019 NC Medicaid fact sheet match it exactly. Counts are 19, 13, 12, 14, 15 and 27.
- **Region 3 lead renamed:** Vaya Health merged with Partners Health Management to become Vaya Partners, effective Oct. 1, 2026. The NCDHHS hub page still says "Vaya Health."[providers.vayahealth.com](https://providers.vayahealth.com/wp-content/uploads/2026/09/pcb-09-10-26-issue-17.pdf?share_frome=aipt)
- **Tamara Smith's title is wrong in the app:** Her staff page says "Executive Assistant - Programs", not Executive Director.[impacthealth.org](https://impacthealth.org/our-people/tamara-smith/?share_frome=aipt)
- **Ombudsman numbers:** 877-201-3750 is the member line. Per the NC Medicaid Ombudsman page, "For Medicaid Providers… Phone: 866-304-7062." So the earlier pass was right, and the app has the member line under a provider label. The email in the app is correct.[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/about-nc-medicaid/nc-medicaid-ombudsman?share_frome=aipt)
- **Who each line is for:** The Medicaid Contact Center (888-245-0179) is listed on the providers page. The provider lines are the Provider Ombudsman (problems with health plans) and the NCTracks Call Center (enrollment, claims, eligibility). The HIEA number 919-754-6912 is the general business office, not the help desk. The technical help desk is SAS at 919-531-2700.[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers?share_frome=aipt)
- **Regional grants:** No regional NC ROOTS grant is open right now. All five Trillium Region 2 and Region 5 applications show "Closed - Under Review," with deadlines of Aug. 24 and Aug. 31, 2026. UNC says it is "currently developing the application process." Access East has posted no opportunities. Note that the year-1 Rural Health Innovation Fund is limited to primary care, FQHCs and safety-net providers. A new SAIOP/SACOT/peer support provider likely does not qualify yet; confirm at RHIF@nc.gov.

## OPEN QUESTIONS

- **Trillium emails:** The NCDHHS page shows Region2NCRootsHub@ / Region5NCRootsHub@ as text, but the links behind them go to Region2RootsHub@ / Region5RootsHub@. Trillium's own pages use the "NCRootsHub" spelling. Ask Trillium Provider Support (1-855-250-1539) which mailbox is live.
- **Unverified phones:** Impact Health (828) 357-8170 and (800) 581-0182, Vaya 1-800-962-9003, and UNC 1-800-806-1964 were not found on any official page. Ask each hub lead by email.
- **Named contacts:** Only Region 1 lists a person. For Regions 2 through 6, ask each hub mailbox whether there is a named lead.
- **Vaya Partners email:** Ask whether RHTP@vayahealth.com will move to a vayapartners.org domain after the merger.
- **Provider Ombudsman hours:** These are not published. Call 866-304-7062 to confirm.
- **NCTracks contact page:** It still names "CSRA" as the operator. Confirm the current vendor name and that the email still works at 800-688-6696.

This is research, not legal advice.