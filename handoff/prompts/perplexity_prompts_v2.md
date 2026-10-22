# Perplexity research prompts: instructions for the 104 checklist tasks (79 original + 25 H.R. 1)

## How to use these prompts

1. **Mode.** Use Perplexity **Pro Search** or **Research (Deep Research)** with web sources on. Do not use the plain quick search.
2. **Master prompt.** Paste the master prompt below at the top of EVERY new thread, immediately followed by one batch. If Perplexity cuts the message off, create a Perplexity **Space**, paste the master prompt into the Space's custom instructions, and paste only the batch into each thread.
3. **Order.** Run **Batch 0 (verify the foundations)** first. If it finds that a policy number, fee or region assignment in my app is wrong, send me those corrections before continuing so the later batches are not built on a bad premise. Then run Batches 1 to 6 (the original 79 tasks), one new thread each. After that run **Batch 0B (verify the H.R. 1 foundations)**, then Batches 7 and 8 (the 25 H.R. 1 tasks). H.R. 1 rules and NC's implementation are still moving, so expect more `NOT VERIFIED` and `low` entries there, and rerun Batch 0B whenever NC Medicaid publishes new guidance.
4. **Check the output.** Each answer should start with a JSON block. Spot-check at least two sources per batch by opening the URLs. Anything marked NOT VERIFIED or confidence "low" needs a human (ideally your healthcare attorney or the agency) before it goes in the app.
5. **Bring it back.** Paste the JSON blocks (and the CORRECTIONS list) into this chat. I will validate them, drop the sources and flags into the data, and add them to the dashboard.

Each JSON entry has the same shape as the existing instructions in the app (`instructions`, `tips`, `contacts`), plus `sources`, `confidence` and `verify` so you can see where each fact came from. The H.R. 1 batches add `basis` (required, expected or recommended) and `effective_date`, and may suggest better wording for tasks that turn out not to be provider obligations.

---

## Master prompt (paste first, every thread)

````text
You are a research analyst who specializes in North Carolina Medicaid behavioral health provider licensure, enrollment, and compliance. I am building a checklist app for a NEW provider standing up three North Carolina Medicaid services: CCP 8G (Peer Support Services), CCP 8A-12 (Substance Abuse Intensive Outpatient Program, SAIOP) and CCP 8A-13 (Substance Abuse Comprehensive Outpatient Treatment, SACOT). The checklist also has a phase for the federal H.R. 1 (Public Law 119-21, the 2025 budget reconciliation act) Medicaid changes. For each checklist task I give you, research and write practical, accurate, source-cited instructions that a first-time provider owner could follow.

TODAY'S DATE IS OCTOBER 2026. Use the policy, rule, fee and form versions in effect now. If something changed in the last 24 months (Tailored Plan launch, CCP revisions, NCTracks changes, DHSR rule or fee changes, session laws), say so and give the effective date.

SOURCES - use primary sources first, in this order:
1. NC Medicaid (medicaid.ncdhhs.gov): Clinical Coverage Policies, Provider Permission Matrix, Medicaid Bulletins, provider enrollment pages
2. NCTracks (nctracks.nc.gov): provider enrollment, credentialing, recredentialing, user guides, FAQs, fee schedule and application fee pages
3. NC DHSR Mental Health Licensure and Certification Section (ncdhhs.gov/dhsr): application packets, fees, survey and plan-of-correction guidance
4. NC Administrative Code (NC Office of Administrative Hearings, 10A NCAC 27G and any other cited rule) and NC General Statutes (ncleg.gov)
5. Federal: 42 CFR (eCFR, including 42 CFR Part 2 for substance use disorder records), CMS and Medicaid.gov (H.R. 1 guidance, informational bulletins, state health official letters, interim final rules), Congress.gov (H.R. 1 text), NPPES, IRS, US DOL, OIG exclusion list, SAM.gov
6. NC DHHS announcements on H.R. 1 implementation and on the Rural Health Transformation Program (NC ROOTS); other NC agencies: NC Secretary of State, NC Department of Labor, NC Department of Insurance, NC Department of Revenue, NC Office of State Fire Marshal and local fire marshal/health/zoning offices, NC Healthcare Personnel Registry, NC SBI / local sheriff fingerprinting
7. Tailored Plan / LME-MCO provider pages (Alliance Health, Trillium Health Resources, Vaya Health, Partners Health Management): credentialing and network participation pages
8. Accreditation bodies (CARF) and peer-certification bodies named in the task
Use blogs, consultants, forums, vendor sites and policy-research summaries (for example KFF) only to corroborate, and mark them as secondary in the sources list.

STRICT RULES ABOUT ACCURACY
- Never invent or guess phone numbers, email addresses, URLs, form numbers, fee amounts, deadlines, rule numbers or policy section numbers. Every fact needs a citation URL from a page you actually opened.
- If you cannot verify something, write NOT VERIFIED in that string and say exactly what to check and where. A clearly flagged gap is better than a confident guess.
- Quote exact rule, statute and policy section numbers when you find them (for example "10A NCAC 27G .0201").
- Where requirements differ by service line (8G vs 8A-12 vs 8A-13), say which applies. Where they differ by LME/MCO, say so.
- Where sources conflict, report both and say which is newer or more authoritative.
- The "app context" I give you may contain wrong or outdated claims (policy numbers, fees, ratios, timelines, contacts). Check them. List every correction in the CORRECTIONS section of your answer instead of silently repeating them.
- H.R. 1 rules are still being implemented. For every H.R. 1 item, separate what is statute, what CMS has issued as guidance or rule, and what NC has actually announced, and give the date of each. Do not present a proposal or a state plan as settled.
- Do not give legal advice. Write practical steps and note when a healthcare attorney, CPA or the agency itself should confirm.

HOW TO WRITE EACH ENTRY
- instructions: 3 to 5 numbered-in-order actions, each starting with a verb, each under 40 words. Name the exact portal, form, or office. Include the current fee, turnaround and deadline when a source states one.
- tips: 2 to 3 items. Focus on audit and licensing traps, common rejection reasons, documentation that surveyors or NCTracks ask for, and deadlines. Start a compliance-risk tip with "AUDIT TRAP:".
- contacts: 1 to 3 items in the form "Office or program name: phone (website)". Only contacts you verified.
- sources: the URLs that support this entry.
- confidence: "high" (primary source confirms), "medium" (primary source partly confirms or is older), or "low" (secondary source only or inferred).
- verify: what a human should double check before relying on the entry, or an empty string.
Style model (already written for another task, match this tone and length):
"step_1_sub_1": {"instructions": ["Log in to sosnc.gov and order an official Certificate of Existence (Certificate of Good Standing).", "Verify that all annual reports are current and that the entity status is Current-Active.", "Download the digital verifiable PDF with barcode and security seal."], "tips": ["DHSR requires this certificate to be dated within 6 months of your initial licensure application submission.", "Keep this document in an administrative credentials repository as LME/MCO network contracting desks will request it repeatedly."], "contacts": ["NC SOS Document Authentication: (919) 814-5400"]}

OUTPUT FORMAT - follow exactly, in this order
A) One JSON object, in a single json code block, keyed by the task keys I give you (for example "step_4_sub_0"). Include EVERY key, in the order given, and no other keys. Each value has exactly these fields, plus any extra fields the batch asks for: instructions (array of strings), tips (array of strings), contacts (array of strings), sources (array of URL strings), confidence (string), verify (string).
   JSON rules: valid JSON that parses; plain text only inside strings (no markdown, no HTML, no line breaks, no bracketed citation numbers like [1]); use straight quotes and escape any double quote inside a string; keep each string on one line.
B) SOURCES: a short table of every distinct source used (title, publisher, URL, date or version, primary or secondary).
C) CORRECTIONS: a bullet list of claims in the app context that are wrong, outdated or unverifiable, with the correct value and a citation.
D) OPEN QUESTIONS: anything you could not verify, and who to call to find out.
If you are running low on space, finish the JSON for the tasks you have done, state which keys remain, and stop. Do not abbreviate or skip a key. Do not add commentary before part A.
````

---

## Batch 0: verify the foundations (run first)

````text
BATCH 0 - VERIFY THE FOUNDATIONS (run this first)
Before I research individual tasks, check the identifiers my app is built on. Reply with a table: claim | CONFIRMED / CORRECTION / NOT VERIFIED | correct value | source URL. Then list anything important I have missed.

Claims to check (they come from my app and may contain errors):
1. NC Medicaid Clinical Coverage Policy 8G is "Peer Support Services". Billing code H0038, periodic, 15-minute unit. Qualified Professional (QP) supervision ratio 1:6. Peer caseload limit of 15.
2. "CCP 8A-12" is the policy for Substance Abuse Intensive Outpatient Program (SAIOP). Code H0015, ASAM Level 2.1, supervised by an LCAS or CCS clinical supervisor, 3 hours per day, 30-day pass-through authorization.
3. "CCP 8A-13" is the policy for Substance Abuse Comprehensive Outpatient Treatment (SACOT). Code H2036, ASAM Level 2.5, 20 or more hours per week (4 hours per day), 1:10 QP ratio, 60-day pass-through authorization.
4. Facility licensure for these services is under 10A NCAC 27G (including 27G .0201 governing body policies), issued by DHSR Mental Health Licensure and Certification Section.
5. "SL 2026-1" is a North Carolina session law relevant to these services. What is it, if it exists?
6. "APSM 45-2" is the NC documentation / records manual used for service notes. What is its current name, number and status?
7. NCTracks requires recredentialing every 5 years, and the revalidation reminders go out at 70, 50, 20 and 5 days.
8. Medicaid Tailored Plans: which LME/MCOs operate in which of NC's regions today, and which are the current provider-network contacts. (My app lists Vaya Health for Region 1, Partners for Regions 2-3, Alliance for Region 4, Trillium for Regions 5-6. Check that.)
9. "NC ROOTS" and "Rural Health Transformation" regional hubs listed in my app (Impact Health, Trillium, Vaya, UNC Health, Access East): do these exist and are they the hub leads?
10. Fees my app assumes: NC SOS filing $125; DHSR licensure base fee $350 plus $12.50 per day of capacity; NCTracks state enrollment fee $100 plus the federal application fee $709; fingerprinting $38 per person; background check $35-$75 per candidate. Give the current amounts and sources.
Also tell me whether these three services need Tailored Plan credentialing in addition to NCTracks enrollment, and in what order the steps normally happen.
````

---

## Batch 1: Step 4 to Step 7 (14 tasks)

````text
BATCH 1 - write entries for the 14 tasks below. Return the JSON keys in this exact order: step_4_sub_0, step_4_sub_1, step_4_sub_2, step_5_sub_0, step_5_sub_1, step_5_sub_2, step_5_sub_3, step_6_sub_0, step_6_sub_1, step_6_sub_2, step_7_sub_0, step_7_sub_1, step_7_sub_2, step_7_sub_3.
Step 4 - Facility Site Selection & Municipal Zoning Approval  (Phase 1: Business & Legal Foundation)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Secure commercial day/outpatient premises sized for client census. Obtain written municipal/county zoning approval explicitly authorizing an outpatient behavioral health day facility.
    Responsible: Facility Director | Typical time: 3–6 weeks | Cost shown: Varies by lease + $50–$200 zoning fee
    Main resource: Local County/City Planning & Zoning Office (https://www.ncacc.org/county-websites/)
    Depends on: Step 1 (Entity formed)
  Tasks to write instructions for:
    step_4_sub_0 = Execute lease or purchase agreement with confidentiality/counseling room partitions
    step_4_sub_1 = Request formal Zoning Determination Letter from city/county planning department
    step_4_sub_2 = Verify physical site meets ADA accessibility requirements

Step 5 - Commercial, General & Professional Liability Insurance  (Phase 1: Business & Legal Foundation)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Bind mandatory commercial general liability, professional malpractice liability, and workers compensation coverage required by DHSR and LME/MCOs.
    Responsible: Owner / Risk Manager | Typical time: 1–2 weeks | Cost shown: $1,500 – $4,500 / year (deposit)
    Main resource: Commercial Healthcare Insurance Broker (https://www.ncdoi.gov/)
    Depends on: Step 4 (Site lease secured)
  Tasks to write instructions for:
    step_5_sub_0 = Procure $1M / $3M professional malpractice liability policy
    step_5_sub_1 = Procure commercial general liability & property coverage
    step_5_sub_2 = Procure NC statutory Workers Compensation insurance
    step_5_sub_3 = Ensure certificates of insurance name the agency as primary insured

Step 6 - Dedicated Business Bank Account & EFT Setup  (Phase 1: Business & Legal Foundation)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Open a dedicated commercial bank account for Medicaid electronic fund transfers (EFT) and operational separation.
    Responsible: Owner / Treasurer | Typical time: 1–2 business days | Cost shown: $0 – $100 initial deposit
    Main resource: Commercial Banking Institution (https://www.fdic.gov/)
    Depends on: Step 1, 2, 3 (Entity, EIN, NPI)
  Tasks to write instructions for:
    step_6_sub_0 = Establish business checking account with voided check for NCTracks EFT
    step_6_sub_1 = Obtain bank letter verifying routing and account numbers
    step_6_sub_2 = Establish segregated payroll holding ledger

Step 7 - Governing Body Appointment & Key Clinical Leadership  (Phase 1: Business & Legal Foundation)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Appoint Facility Director (named on license) and Clinical Director / Supervisor meeting Qualified Professional (QP) standards under 10A NCAC 27G .0104.
    Responsible: Governing Board / Owner | Typical time: 1–3 weeks | Cost shown: $0 (Internal governance)
    Main resource: 10A NCAC 27G .0104 Definitions (https://www.oah.nc.gov/)
    Depends on: Step 1 (Corporate governance)
  Tasks to write instructions for:
    step_7_sub_0 = Document Board of Directors / Advisory Committee minutes
    step_7_sub_1 = Designate Facility Director as legal responsible party
    step_7_sub_2 = Appoint Clinical Director meeting QP requirements under 10A NCAC 27G .0104
    step_7_sub_3 = Draft organizational chart showing lines of clinical and administrative supervision
````

---

## Batch 2: Step 8 to Step 10 (12 tasks)

````text
BATCH 2 - write entries for the 12 tasks below. Return the JSON keys in this exact order: step_8_sub_0, step_8_sub_1, step_8_sub_2, step_9_sub_0, step_9_sub_1, step_9_sub_2, step_9_sub_3, step_9_sub_4, step_10_sub_0, step_10_sub_1, step_10_sub_2, step_10_sub_3.
Step 8 - LME/MCO Letter of Support (10A NCAC 27G .0406)  (Phase 1: Business & Legal Foundation)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Formally request the mandatory Letter of Support from the LME/MCO governing the facility county footprint. Mandatory attachment for the DHSR license application.
    Responsible: Facility Director | Typical time: 2–6 weeks | Cost shown: $0 (Administrative)
    Main resource: Assigned LME/MCO (Alliance, Partners, Trillium, or Vaya) (https://medicaid.ncdhhs.gov/transformation/tailored-plans)
    Depends on: Step 4 & 7 (Facility site & leadership)
  Tasks to write instructions for:
    step_8_sub_0 = Submit program summary and county location to assigned LME/MCO Provider Network desk
    step_8_sub_1 = Include intended CCP services: Peer Support, SAIOP, and/or SACOT
    step_8_sub_2 = Obtain formal signed Letter of Support citing 10A NCAC 27G .0406

Step 9 - Statutory Policies & Procedures Engineering  (Phase 2: DHSR Licensure (10A NCAC 27G))
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Draft comprehensive P&P manual cross-referenced to 10A NCAC 27G, APSM 45-2 documentation standards, modernized 42 CFR Part 2 rules, and NC IRIS 72-hour critical incident reporting.
    Responsible: Clinical Director / Compliance Consultant | Typical time: 3–6 weeks | Cost shown: $0 – $3,500 (consultant optional)
    Main resource: NC DHSR MHLCS Policy Review Tool (https://info.ncdhhs.gov/dhsr/mhlcs/establish.html)
    Depends on: Step 7 & 8 (Leadership named, Letter of Support in progress)
  Tasks to write instructions for:
    step_9_sub_0 = Draft governance, client rights & grievance procedures (10A NCAC Subchapters D & E)
    step_9_sub_1 = Integrate APSM 45-2 ten-element service note protocol
    step_9_sub_2 = Incorporate 42 CFR Part 2 modernized consent and disclosure restrictions
    step_9_sub_3 = Establish Incident Response Improvement System (IRIS) 72-hour reporting workflow (.0600)
    step_9_sub_4 = Draft Fraud, Waste & Abuse (FWA) / False Claims Act compliance plan

Step 10 - Core Clinical & Peer Support Staff Recruitment  (Phase 2: DHSR Licensure (10A NCAC 27G))
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Recruit and hire staff meeting regulatory ratios: LCAS/CCS clinical supervisor for SAIOP/SACOT, Qualified Professionals for group therapy, and NC Certified Peer Support Specialists (CPSS).
    Responsible: Clinical Director / HR | Typical time: 4–8 weeks | Cost shown: Recruitment costs / Staff payroll
    Main resource: NCASPPB / UNC NCCPSS Portal (https://pss.unc.edu/)
    Depends on: Step 7 & 9 (P&P and leadership established)
  Tasks to write instructions for:
    step_10_sub_0 = Hire LCAS (Licensed Clinical Addictions Specialist) or CCS for SUD supervision
    step_10_sub_1 = Verify SACOT 1:10 group counseling Qualified Professional ratio capacity
    step_10_sub_2 = Verify Peer Support 1:6 QP supervisory ratio and maximum 1:15 recipient caseload ratio
    step_10_sub_3 = Execute signed employment agreements with defined job descriptions
````

---

## Batch 3: Step 11 to Step 14 (15 tasks)

````text
BATCH 3 - write entries for the 15 tasks below. Return the JSON keys in this exact order: step_11_sub_0, step_11_sub_1, step_11_sub_2, step_11_sub_3, step_12_sub_0, step_12_sub_1, step_12_sub_2, step_12_sub_3, step_13_sub_0, step_13_sub_1, step_13_sub_2, step_14_sub_0, step_14_sub_1, step_14_sub_2, step_14_sub_3.
Step 11 - Mandatory Pre-Hire Screenings (HCPR & Exclusion Checks)  (Phase 2: DHSR Licensure (10A NCAC 27G))
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Perform mandatory pre-employment checks: NC Health Care Personnel Registry (HCPR) under N.C.G.S. § 131E-256, NC Sex Offender Registry, and federal OIG/SAMHSA exclusion logs.
    Responsible: HR Director / Compliance Officer | Typical time: 1–2 weeks | Cost shown: $35 – $75 per candidate (SBI background)
    Main resource: NC Health Care Personnel Registry (HCPR) (https://info.ncdhhs.gov/dhsr/hcpr/index.html)
    Depends on: Step 10 (Candidates identified)
  Tasks to write instructions for:
    step_11_sub_0 = Execute and file NC Health Care Personnel Registry (HCPR) check PRIOR to hire date
    step_11_sub_1 = Conduct state and national criminal history checks with fingerprints
    step_11_sub_2 = Screen staff and 5%+ owners against OIG LEIE, SAM.gov, and NC Exclusion database
    step_11_sub_3 = Establish recurring monthly OIG exclusion audit calendar

Step 12 - CPSS Credential & Lived-Experience Verification  (Phase 2: DHSR Licensure (10A NCAC 27G))
  Applies to: CCP 8G
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Verify all Peer Support staff hold active NCCPSS certification from UNC School of Social Work, documenting 18+ months lived recovery and ethics coursework.
    Responsible: Clinical Director / HR | Typical time: 1–2 weeks | Cost shown: $0 (Online verification)
    Main resource: UNC NCCPSS Program Office (https://pss.unc.edu/)
    Depends on: Step 10 (CPSS hired)
  Tasks to write instructions for:
    step_12_sub_0 = Verify active credential on NCCPSS registry
    step_12_sub_1 = File proof of 50-hour Foundations course + 20 hours continuing education
    step_12_sub_2 = Verify lived experience attestation in HR record
    step_12_sub_3 = Set 2-year certification renewal reminder

Step 13 - Local Fire Marshal & Sanitation Facility Clearances  (Phase 2: DHSR Licensure (10A NCAC 27G))
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Schedule and complete fire safety inspection and county health department sanitation inspections for day treatment occupancy.
    Responsible: Facility Director | Typical time: 2–4 weeks | Cost shown: $75 – $250 inspection fees
    Main resource: Local Municipal Fire Marshal & County Health Dept (https://www.ncdhhs.gov/divisions/public-health/county-health-departments)
    Depends on: Step 4 (Site secured)
  Tasks to write instructions for:
    step_13_sub_0 = Pass annual Fire Marshal inspection with stamped approval certificate
    step_13_sub_1 = Pass sanitation inspection for day facility restrooms and water supply
    step_13_sub_2 = Post approved maximum room occupancy signs in group rooms

Step 14 - DHSR MHLCS Initial Licensure Application Submission  (Phase 2: DHSR Licensure (10A NCAC 27G))
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Submit formal Initial Licensure Application packet to DHSR Mental Health Licensure and Certification Section (MHLCS) in Raleigh with all required statutory exhibits.
    Responsible: Facility Director | Typical time: 1–2 weeks to assemble | Cost shown: $350 base fee + $12.50/day client capacity fee
    Main resource: DHSR MHLCS Application Section (https://info.ncdhhs.gov/dhsr/mhlcs/establish.html)
    Depends on: Steps 4, 8, 9, 10, 11, 13
  Tasks to write instructions for:
    step_14_sub_0 = Complete DHSR Initial Licensure Application PDF
    step_14_sub_1 = Attach LME/MCO Letter of Support, Zoning Letter, and Fire/Sanitation reports
    step_14_sub_2 = Attach complete P&P manual cross-walked to 10A NCAC 27G
    step_14_sub_3 = Attach staff roster with verified credentials and fee payment
````

---

## Batch 4: Step 15 to Step 18 (13 tasks)

````text
BATCH 4 - write entries for the 13 tasks below. Return the JSON keys in this exact order: step_15_sub_0, step_15_sub_1, step_15_sub_2, step_16_sub_0, step_16_sub_1, step_16_sub_2, step_17_sub_0, step_17_sub_1, step_17_sub_2, step_18_sub_0, step_18_sub_1, step_18_sub_2, step_18_sub_3.
Step 15 - DHSR On-Site Initial Licensure Survey  (Phase 2: DHSR Licensure (10A NCAC 27G))
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Undergo comprehensive on-site survey by DHSR inspectors reviewing physical plant, HR personnel files, restrictive intervention training, and clinical policies.
    Responsible: Facility Director & Clinical Director (Mandatory on-site) | Typical time: 4–8 weeks queue wait | Cost shown: $0 (Included in filing)
    Main resource: DHSR Survey Team (https://info.ncdhhs.gov/dhsr/mhlcs/)
    Depends on: Step 14 (Application accepted by DHSR)
  Tasks to write instructions for:
    step_15_sub_0 = Host DHSR inspector walkthrough of physical day facility
    step_15_sub_1 = Provide 100% compliant personnel files with pre-hire HCPR checks
    step_15_sub_2 = Demonstrate knowledge of client rights and restrictive intervention policies (10A NCAC 27G .0209)

Step 16 - Plan of Correction (POC) & License Issuance  (Phase 2: DHSR Licensure (10A NCAC 27G))
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Respond to any Statement of Deficiencies within 10–15 calendar days with a systemic Plan of Correction. Receive official DHSR facility license.
    Responsible: Facility Director / Clinical Director | Typical time: 2–4 weeks | Cost shown: $0
    Main resource: DHSR MHLCS Licensure Desk (https://info.ncdhhs.gov/dhsr/mhlcs/)
    Depends on: Step 15 (Survey findings received)
  Tasks to write instructions for:
    step_16_sub_0 = Draft Plan of Correction identifying root cause, systemic change, and monitoring frequency
    step_16_sub_1 = Submit POC to DHSR within required deadline
    step_16_sub_2 = Receive official DHSR Mental Health / SUD Facility License with service designations

Step 17 - NC HealthConnex (HIE) Participation Agreement & Integration  (Phase 3: NCTracks & State Integration)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Execute mandatory full participation agreement with NC Health Information Exchange Authority (NC HIEA) per N.C.G.S. § 90-414.4 and configure EHR interface.
    Responsible: EHR Administrator / Compliance Officer | Typical time: 3–6 weeks | Cost shown: $0 state fee (EHR interface fee varies)
    Main resource: NC HealthConnex / NC HIEA (https://hiea.nc.gov/)
    Depends on: Step 16 (DHSR license issued)
  Tasks to write instructions for:
    step_17_sub_0 = Execute NC HealthConnex Full Participation Agreement online
    step_17_sub_1 = Select EHR certified for NC HealthConnex HL7/FHIR encounter data exchange
    step_17_sub_2 = File proof of active connection or approved HIEA extension before billing

Step 18 - NCTracks Organization Provider Enrollment Application  (Phase 3: NCTracks & State Integration)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Submit Organization Enrollment Application in NCTracks. Designate authorized Office Administrator with NCID, attach DHSR license, and assign taxonomy codes.
    Responsible: Office Administrator | Typical time: 1–2 weeks to submit | Cost shown: $100 NC state fee + $709 federal application fee
    Main resource: NCTracks Provider Portal (https://www.nctracks.nc.gov/content/public/providers/provider-enrollment.html)
    Depends on: Step 3, 16, 17 (NPI, DHSR License, HIE connection)
  Tasks to write instructions for:
    step_18_sub_0 = Obtain NCID for designated Office Administrator
    step_18_sub_1 = Complete NCTracks Organization Enrollment Application
    step_18_sub_2 = Select correct taxonomies aligned with Provider Permission Matrix (PPM)
    step_18_sub_3 = Upload DHSR license, W-9, and banking EFT documentation
````

---

## Batch 5: Step 19 to Step 22 (14 tasks)

````text
BATCH 5 - write entries for the 14 tasks below. Return the JSON keys in this exact order: step_19_sub_0, step_19_sub_1, step_19_sub_2, step_20_sub_0, step_20_sub_1, step_20_sub_2, step_21_sub_0, step_21_sub_1, step_21_sub_2, step_21_sub_3, step_22_sub_0, step_22_sub_1, step_22_sub_2, step_22_sub_3.
Step 19 - Moderate/High Risk Fingerprinting & Site Screening  (Phase 3: NCTracks & State Integration)
  Applies to: CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Complete mandatory fingerprint criminal history checks for 5%+ owners and managing employees under N.C.G.S. § 108C-3; complete NCTracks on-site review.
    Responsible: 5%+ Owners / Managing Employees | Typical time: 3–5 weeks | Cost shown: $38 per person (SBI/FBI electronic fingerprinting)
    Main resource: Local Sheriff’s Office & NCTracks Screening (https://www.nctracks.nc.gov/)
    Depends on: Step 18 (NCTracks notification received)
  Tasks to write instructions for:
    step_19_sub_0 = Schedule electronic LiveScan fingerprinting within 30-day notice window
    step_19_sub_1 = Submit Fingerprint Verification Forms to NCTracks Provider Screening Unit
    step_19_sub_2 = Pass NCTracks physical site visit verification

Step 20 - NCTracks Approval & Effective Date Alignment  (Phase 3: NCTracks & State Integration)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Receive approved NCTracks enrollment letter. Link individual rendering providers (LCAS, CCS, QP) to the organizational billing NPI.
    Responsible: Office Administrator | Typical time: 2–4 weeks | Cost shown: $0
    Main resource: NCTracks Provider Record (https://www.nctracks.nc.gov/)
    Depends on: Step 18 & 19 (Enrollment and screening approved)
  Tasks to write instructions for:
    step_20_sub_0 = Verify billing effective date aligns with credentials
    step_20_sub_1 = Submit Manage Change Request (MCR) to affiliate rendering clinicians to organizational NPI
    step_20_sub_2 = Test electronic claims submission and ERA 835 delivery

Step 21 - Regional Tailored Plan / LME-MCO Network Participation  (Phase 4: Tailored Plan Contracting)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Execute network participation agreements with assigned regional Tailored Plans (Alliance, Partners, Trillium, or Vaya) for Medicaid and State-Funded benefit packages.
    Responsible: Executive Director / Contracting Officer | Typical time: 6–12 weeks | Cost shown: $0 (Contracting)
    Main resource: Regional LME/MCO Contracting Portal (https://medicaid.ncdhhs.gov/transformation/tailored-plans)
    Depends on: Step 16 (DHSR License) & Step 18 (NCTracks submitted)
  Tasks to write instructions for:
    step_21_sub_0 = Submit network participation applications to applicable regional plans
    step_21_sub_1 = Submit roster attestation with clinician CAQH IDs and NCTracks records
    step_21_sub_2 = Establish Electronic Data Interchange (EDI) testing with plan clearinghouses
    step_21_sub_3 = Complete Utilization Management (UM) portal training for prior authorizations

Step 22 - EHR Clinical Setup & APSM 45-2 Note Scrubber  (Phase 5: Launch & Ongoing Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Configure EHR clinical note templates enforcing all 10 mandatory elements of APSM 45-2, 15-minute periodic increments for Peer Support, and same-day service exclusion checks.
    Responsible: Clinical Director & Billing Specialist | Typical time: 2–4 weeks | Cost shown: $150 – $400 / clinician / month (EHR SaaS)
    Main resource: Behavioral Health EHR Vendor (https://www.healthit.gov/)
    Depends on: Step 9 & 17 (P&P and HIE interface ready)
  Tasks to write instructions for:
    step_22_sub_0 = Configure 10-element APSM 45-2 compliant service note templates
    step_22_sub_1 = Build automated billing rules blocking concurrent SAIOP + SACOT same-day claims
    step_22_sub_2 = Configure 20-unit (5 hr) daily and 80-unit (20 hr) weekly billing limits for Peer Support
    step_22_sub_3 = Configure 3-hr daily minimum for SAIOP (H0015) and 4-hr daily minimum for SACOT (H2036)
````

---

## Batch 6: Step 23 to Step 25 (11 tasks)

````text
BATCH 6 - write entries for the 11 tasks below. Return the JSON keys in this exact order: step_23_sub_0, step_23_sub_1, step_23_sub_2, step_24_sub_0, step_24_sub_1, step_24_sub_2, step_24_sub_3, step_25_sub_0, step_25_sub_1, step_25_sub_2, step_25_sub_3.
Step 23 - 24/7/365 First-Responder Crisis Protocol & Clinical Training  (Phase 5: Launch & Ongoing Compliance)
  Applies to: CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Train all staff on mandatory 24/7/365 crisis first-responder coverage required by CCP 8A-12 and CCP 8A-13; conduct restrictive intervention & client rights training (10A NCAC 27G .0209).
    Responsible: Clinical Director | Typical time: 1–2 weeks | Cost shown: Staff training hours
    Main resource: Internal Clinical Training (https://www.oah.nc.gov/)
    Depends on: Step 10 & 22 (Staff hired & EHR ready)
  Tasks to write instructions for:
    step_23_sub_0 = Publish rotating 24/7/365 clinical crisis on-call schedule with LCAS/CCS backup
    step_23_sub_1 = Document staff training on client rights, confidentiality, and de-escalation
    step_23_sub_2 = File signed training completion certificates in personnel records

Step 24 - Intake, Assessment, PCP & Authorization Protocol  (Phase 5: Launch & Ongoing Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Standardize intake: Comprehensive Clinical Assessment (CCA) within 1 year, ASAM level-of-care determination, Service Order signed by physician/NP/PA, and 30/60-day pass-through authorization tracking.
    Responsible: Clinical Supervisor / Intake Coordinator | Typical time: 1–2 weeks | Cost shown: $0 (Clinical workflow)
    Main resource: NC Medicaid Person-Centered Plan (PCP) Manual (https://medicaid.ncdhhs.gov/)
    Depends on: Step 21 & 22 (Network contract and EHR active)
  Tasks to write instructions for:
    step_24_sub_0 = Verify CCA contains required ASAM 6-dimension assessment (Level 2.1 SAIOP / Level 2.5 SACOT)
    step_24_sub_1 = Ensure Service Order is executed prior to or on Day 1 of service
    step_24_sub_2 = Set up automated tracking for SAIOP 30-day and SACOT 60-day pass-through expiration dates
    step_24_sub_3 = Execute modernized 42 CFR Part 2 and HIPAA consent documentation at intake

Step 25 - National Accreditation (CARF) Roadmap & NCTracks 5-Yr Reverification  (Phase 5: Launch & Ongoing Compliance)
  Applies to: CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Initiate 12-month CARF / Joint Commission accreditation pathway required for sustained network standing. Establish compliance calendar for annual DHSR renewal, 2-yr CPSS renewal, and 5-yr NCTracks reverification.
    Responsible: Quality Director / CEO | Typical time: Ongoing (Survey window months 9–12) | Cost shown: $8,000 – $14,000 (CARF survey fee)
    Main resource: CARF International Behavioral Health (https://www.carf.org/)
    Depends on: Step 20 & 21 (Operational and billing Medicaid)
  Tasks to write instructions for:
    step_25_sub_0 = Select accreditation body (CARF Behavioral Health Standards)
    step_25_sub_1 = Run continuous 6-month demonstration period with QI Committee and chart peer reviews
    step_25_sub_2 = Calendar NCTracks 5-year recredentialing (70, 50, 20, 5 day alerts)
    step_25_sub_3 = Calendar monthly OIG/SAM exclusion screenings and 2-year CPSS renewals
````

---

## Batch 0B: verify the H.R. 1 foundations (run before the H.R. 1 batches)

````text
BATCH 0B - VERIFY THE H.R. 1 FOUNDATIONS (run after Batch 0, before the H.R. 1 batches)
Reply with a table: claim | CONFIRMED / CORRECTION / NOT VERIFIED | correct value | status (statute / CMS rule or guidance / NC announcement / proposal) | source URL. Then answer the questions at the end.

Claims to check (from my app; they may contain errors):
1. H.R. 1 is Public Law 119-21, the 2025 budget reconciliation act, signed July 4, 2025.
2. Community engagement (work) requirement: applies to adult Medicaid expansion enrollees roughly ages 19-64; 80 hours per month of work, community service, work program or education; states must implement by January 1, 2027, with possible good-faith extensions to the end of 2028. Confirm the exact start date, who is covered, how many hours, how compliance is verified and how often.
3. Exemptions: which groups are exempt or deemed compliant, specifically people with a substance use disorder, people in SUD treatment programs, people with a disabling mental disorder, and people who are medically frail. Quote the statutory language and CMS guidance.
4. Eligibility redeterminations every 6 months for expansion adults, for renewals beginning on or after December 31, 2026.
5. Retroactive coverage shortened (to 1 month for expansion adults and 2 months for others) for applications on or after January 1, 2027.
6. Cost-sharing for expansion adults above 100% of the federal poverty level begins October 1, 2028. Which services are excluded (primary care, mental health, substance use disorder?) and what are the limits?
7. Changes to eligibility for certain lawfully present immigrants effective October 1, 2026.
8. Provider screening and program integrity: required checks of provider enrollment data against death records (Death Master File), by what date, and who must do them (state or provider).
9. Limits on provider taxes and state directed payments, and what they mean for NC Medicaid and Tailored Plan funding of behavioral health providers.
10. Rural Health Transformation Program: $50 billion over fiscal years 2026-2030 ($10 billion per year). NC's award amounts, the name "NC ROOTS", which agency runs it, whether and how providers can apply for sub-awards, the regional hubs (my app lists Impact Health, Trillium, Vaya, UNC Health and Access East), deadlines, and reporting requirements.
11. NC specifics: NC's Medicaid expansion trigger law and its current status after H.R. 1; NC Medicaid's published implementation timeline and systems for the work requirement, six-month renewals and cost-sharing; any NC Medicaid provider bulletins on H.R. 1; how Tailored Plan members are handled.
12. 42 CFR Part 2: what consent and disclosure rules apply when a SUD treatment provider shares attendance or exemption information with NC Medicaid or a Tailored Plan to prove community engagement or an exemption.

Questions:
A. Which other H.R. 1 provisions create real to-do items for a NEW North Carolina outpatient behavioral health provider offering peer support, SAIOP and SACOT, beyond these six areas: impact review, eligibility checks and renewals, community engagement documentation, coverage and cost-sharing billing controls, program integrity and funding risk, and rural health transformation funding? Give a prioritized list with citations and effective dates.
B. Which of the six areas above are legal requirements for providers, which are requirements for the state or members only (providers just need to adapt), and which are good practice?
````

---

## Batch 7 (H.R. 1): Step 26 to Step 28 (13 tasks)

````text
BATCH 7 - write entries for the 13 tasks below. Return the JSON keys in this exact order: step_26_sub_0, step_26_sub_1, step_26_sub_2, step_26_sub_3, step_27_sub_0, step_27_sub_1, step_27_sub_2, step_27_sub_3, step_28_sub_0, step_28_sub_1, step_28_sub_2, step_28_sub_3, step_28_sub_4.
These are H.R. 1 tasks. In EACH entry add two more fields after verify: "basis" (one of: "required" = a provider legal or contract duty today; "expected" = NC has published or announced it will apply to providers; "recommended" = good practice only) and "effective_date" (the date it applies, or "unknown"). If a task is not actually a provider obligation, say so in verify and suggest a better wording of the task in the verify field.
Step 26 - H.R. 1 Impact Review & Compliance Owner  (Phase 6: H.R. 1 Medicaid Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: H.R. 1 (Public Law 119-21, the 2025 federal budget reconciliation act) changes Medicaid eligibility, renewals, cost-sharing and program-integrity rules, and created the Rural Health Transformation Program. Work out which provisions reach your service lines and name one accountable owner. Dates to confirm against current NC Medicaid guidance: Oct 2026 (immigrant eligibility), Dec 2026 (six-month renewals for expansion adults), Jan 2027 (community engagement and shorter retroactive coverage), Oct 2028 (cost-sharing).
    Responsible: Compliance Officer / Owner | Typical time: 1–2 weeks | Cost shown: $0 (Internal)
    Main resource: H.R. 1 (119th Congress) bill text (https://www.congress.gov/bill/119th-congress/house-bill/1)
    Depends on: Step 1 (Entity formed)
  Tasks to write instructions for:
    step_26_sub_0 = Read the H.R. 1 Medicaid provisions and the NC Medicaid guidance that apply to outpatient behavioral health
    step_26_sub_1 = Name an H.R. 1 compliance owner and a backup in the governing body minutes
    step_26_sub_2 = Subscribe to NC Medicaid bulletins and each Tailored Plan provider notice list for H.R. 1 updates
    step_26_sub_3 = Build a dated H.R. 1 calendar of effective dates, each with an internal deadline and an owner

Step 27 - Eligibility Verification & Six-Month Renewal Readiness  (Phase 6: H.R. 1 Medicaid Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Expansion adults are moving to eligibility renewals every six months, so more clients will lose coverage for paperwork reasons. Build intake and billing controls that check eligibility before every billing period, and help clients keep their coverage without giving legal advice.
    Responsible: Billing Manager / Intake Lead | Typical time: 2–4 weeks | Cost shown: $0 (Internal workflow)
    Main resource: NCTracks (eligibility verification) (https://www.nctracks.nc.gov/)
    Depends on: Step 18 (NCTracks enrollment) & Step 22 (EHR setup)
  Tasks to write instructions for:
    step_27_sub_0 = Add a Medicaid eligibility check to intake and again before each billing period or authorization renewal
    step_27_sub_1 = Create a claim-hold and follow-up workflow for clients whose eligibility lapses during treatment
    step_27_sub_2 = Train staff to remind clients about renewal notices and refer them to their county DSS or NC Medicaid for help
    step_27_sub_3 = Track coverage-loss reasons monthly and report trends to the governing body

Step 28 - Community Engagement Requirement & Exemption Documentation  (Phase 6: H.R. 1 Medicaid Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: H.R. 1 requires many expansion adults to show work, community service, school or a similar activity. Exemptions may cover people in substance use disorder treatment, people with a disabling mental disorder and people who are medically frail. Prepare to document treatment participation and exemptions accurately, with proper client consent, once NC Medicaid sets its process.
    Responsible: Clinical Director / Compliance Officer | Typical time: 3–4 weeks | Cost shown: $0 (Internal)
    Main resource: NC Medicaid (NC DHHS) (https://medicaid.ncdhhs.gov/)
    Depends on: Step 26 (Impact review) & Step 24 (Intake and assessment)
  Tasks to write instructions for:
    step_28_sub_0 = Confirm with NC Medicaid and each Tailored Plan who must meet the requirement, which exemptions apply and how providers submit documentation
    step_28_sub_1 = Add a client consent form for sharing treatment participation or exemption information, including the 42 CFR Part 2 rules for substance use disorder records
    step_28_sub_2 = Create a clinician-signed template letter for exemptions such as SUD treatment, disabling mental disorder or medical frailty
    step_28_sub_3 = Set up EHR reports that show each client attendance hours in SAIOP, SACOT or peer support for verification requests
    step_28_sub_4 = Train staff on what they may tell clients about the requirement and when to refer them to NC Medicaid or county DSS
````

---

## Batch 8 (H.R. 1): Step 29 to Step 31 (12 tasks)

````text
BATCH 8 - write entries for the 12 tasks below. Return the JSON keys in this exact order: step_29_sub_0, step_29_sub_1, step_29_sub_2, step_29_sub_3, step_30_sub_0, step_30_sub_1, step_30_sub_2, step_30_sub_3, step_31_sub_0, step_31_sub_1, step_31_sub_2, step_31_sub_3.
These are H.R. 1 tasks. In EACH entry add two more fields after verify: "basis" (one of: "required" = a provider legal or contract duty today; "expected" = NC has published or announced it will apply to providers; "recommended" = good practice only) and "effective_date" (the date it applies, or "unknown"). If a task is not actually a provider obligation, say so in verify and suggest a better wording of the task in the verify field.
Step 29 - Coverage Changes, Billing & Cost-Sharing Controls  (Phase 6: H.R. 1 Medicaid Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: Shorter retroactive coverage, new immigrant eligibility rules and future cost-sharing for some expansion adults change what you can bill and collect. Update intake, financial-responsibility and billing rules so you do not deliver services you cannot get paid for or collect amounts you are not allowed to charge.
    Responsible: Billing Manager / Compliance Officer | Typical time: 2–3 weeks | Cost shown: $0 (Internal policy work)
    Main resource: NC Medicaid (NC DHHS) (https://medicaid.ncdhhs.gov/)
    Depends on: Step 26 (Impact review) & Step 20 (NCTracks approval)
  Tasks to write instructions for:
    step_29_sub_0 = Update the intake and billing policy for shorter retroactive coverage: confirm eligibility before services rather than relying on back-dated approval
    step_29_sub_1 = Write a financial responsibility and sliding-fee policy, with client notices, for people who lose or do not qualify for Medicaid
    step_29_sub_2 = Ask each Tailored Plan in writing whether member cost-sharing will apply to peer support, SAIOP and SACOT, and when, then set front-desk scripts
    step_29_sub_3 = Update billing system edits for new eligibility categories and immigration-status changes, and test claims before launch

Step 30 - Program Integrity, Provider Screening & Funding Risk  (Phase 6: H.R. 1 Medicaid Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: H.R. 1 tightens Medicaid program-integrity rules, including more frequent checks of provider enrollment data against exclusion and death records, and it limits some state financing tools that help fund provider payments. Keep enrollment data clean and plan for rate or volume changes.
    Responsible: Compliance Officer / CFO | Typical time: 3–4 weeks | Cost shown: $0 (Internal)
    Main resource: OIG Exclusions Database (LEIE) (https://oig.hhs.gov/exclusions/)
    Depends on: Step 20 (NCTracks approval) & Step 25 (Compliance calendar)
  Tasks to write instructions for:
    step_30_sub_0 = Add a monthly screen of every owner, manager and rendering provider against the OIG exclusion list, SAM.gov and the death records NC Medicaid requires
    step_30_sub_1 = Calendar NCTracks updates for ownership, address, license, NPI and taxonomy changes, with the reporting deadline for each
    step_30_sub_2 = Build a reimbursement-risk budget that shows cash needs if Medicaid volume or rates fall 10 to 20 percent
    step_30_sub_3 = Set a cash reserve target and a review date tied to NC Medicaid rate and Tailored Plan contract notices

Step 31 - Rural Health Transformation (NC ROOTS) Funding  (Phase 6: H.R. 1 Medicaid Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  App context (may contain errors - verify, correct in the CORRECTIONS section):
    Description: H.R. 1 created a multi-year Rural Health Transformation Program that funds state plans, which NC runs as NC ROOTS. Providers in rural counties may be able to apply for sub-awards or join hub networks. Find out what NC has opened and whether your counties and services qualify.
    Responsible: Owner / Grants Lead | Typical time: 4–8 weeks | Cost shown: $0 (Internal)
    Main resource: NC Department of Health and Human Services (https://www.ncdhhs.gov/)
    Depends on: Step 1 (Entity formed) & county selection in Setup
  Tasks to write instructions for:
    step_31_sub_0 = Find NC rural health transformation (NC ROOTS) announcements, funding notices and eligibility rules from NC DHHS
    step_31_sub_1 = Contact the hub lead for each of your counties (see Regional contacts) and ask how providers join or apply
    step_31_sub_2 = Prepare a one-page capability statement with services, counties served, peer workforce and expected outcomes
    step_31_sub_3 = Calendar application deadlines, reporting requirements and any data or technology conditions
````
