> From: https://www.perplexity.ai/computer/tasks/bcd56cc6-b6f3-4759-bbf4-51fdcd397a03

# you asked

message time: 2026-10-18 20:11:37

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

---

# perplexity response

Ran cd  && grep -n "Requirements for Day" mhiapp.txt; awk 'NR>=215 && NR<=262' mhiapp.txt | cut -c1-250 | grep -v '^\s*$'

---

# perplexity response

```json
{
  "step_11_sub_0": {
    "instructions": [
      "Open the NC Health Care Personnel Registry (HCPR) Verify Registry Listings page and search each finalist by full legal name, plus any prior or maiden names, before an offer becomes a hire.",
      "Save or print each result showing the date-specific confirmation number, and write the search date and planned hire date on the printout.",
      "File the printout in the personnel record and a central business file. G.S. 131E-256 and DHSR require you to note each incident of registry access in your business files.",
      "Stop the hire if the registry shows a substantiated finding of abuse or neglect. 10A NCAC 27G .0202(b)(4) bars employing staff with such a listing.",
      "Repeat the search for every direct-care contractor, volunteer who serves clients, and rehire before first client contact."
    ],
    "tips": [
      "AUDIT TRAP: The confirmation date must be earlier than the hire date. A search run after the first shift does not satisfy the pre-hire requirement in G.S. 131E-256 or 10A NCAC 27G .0202(b)(4).",
      "For the initial licensure review, MHLCS lists HCPR verification for all staff, including the licensee, completed within 90 days of the licensure review. Re-run any older checks.",
      "The statute defines health care personnel as unlicensed staff, but the licensing rule covers every person who provides services. Check licensed clinicians and owners too, so no one is missed."
    ],
    "contacts": [
      "NC HCPR Registry Office: 919-855-3969, Mon-Fri 8:00am-12:00pm and 1:00pm-3:00pm (https://info.ncdhhs.gov/dhsr/hcpr/index.html)",
      "Health Care Personnel Investigations: 919-855-3968 (https://info.ncdhhs.gov/dhsr/ciu/provider.html)"
    ],
    "sources": [
      "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_131E/GS_131E-256.html",
      "https://info.ncdhhs.gov/dhsr/ciu/provider.html",
      "https://info.ncdhhs.gov/dhsr/hcpr/index.html",
      "https://ncnar.ncdhhs.gov/verify_listings1.jsp",
      "http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/subchapter%20g%20rules.html",
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/listmaterials.pdf"
    ],
    "confidence": "high",
    "verify": "Confirm with your MHLCS Licensure and Training consultant how they want HCPR proof presented. Confirm that the 90-day window is still in the current List of Required Materials (rev. 09/30/24)."
  },
  "step_11_sub_1": {
    "instructions": [
      "Make every job offer conditional on the applicant's written consent to a criminal history check and on a satisfactory result. Do not employ anyone who refuses consent (G.S. 122C-80).",
      "Request the check within five business days of the conditional offer. Applicants who have lived in NC under five years need State plus fingerprint-based national checks. Longer residents need the State check.",
      "After you receive a DHSR facility license number, activate the DHSR Criminal Background Check system (ABCMS) and use it to submit fingerprint checks. Before licensure, ask your MHLCS consultant how to run them.",
      "Wait for the DHHS Criminal Records Check Unit to tell you whether a result affects employability. Providers do not receive the national report itself.",
      "Weigh the statutory factors for any relevant conviction, and document the hire or no-hire decision in the personnel file."
    ],
    "tips": [
      "AUDIT TRAP: MHLCS expects State and national criminal check documentation dated within 180 days of the initial licensure review. Stale checks must be redone.",
      "ABCMS requires a facility license number, so it cannot be activated before licensure. Pre-licensure fingerprinting logistics are NOT VERIFIED, so ask MHLCS before you pay any vendor.",
      "G.S. 122C-80 covers positions that do not require an occupational license. Licensed clinicians (LCAS, LCSW, LCMHC) fall outside it, but your own policy should still require checks for them. The NC Sex Offender Registry search is optional good practice, not a rule requirement."
    ],
    "contacts": [
      "NC SBI (fingerprint and access agreement questions): 919-582-8639 (https://info.ncdhhs.gov/dhsr/abcms/index.html)",
      "DHSR Mental Health Licensure and Certification Section: 919-855-3795 (https://info.ncdhhs.gov/dhsr/mhlcs/establish.html)"
    ],
    "sources": [
      "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_122C/GS_122C-80.html",
      "https://info.ncdhhs.gov/dhsr/abcms/index.html",
      "https://info.ncdhhs.gov/dhsr/abcms/pdf/Non-Criminal-Justice-Access-Agreement-Form_SB-41.pdf",
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/listmaterials.pdf",
      "https://sexoffender.ncsbi.gov/"
    ],
    "confidence": "medium",
    "verify": "NOT VERIFIED: the State-only check fee, and how a not-yet-licensed applicant runs fingerprint checks. The SBI access agreement form lists $38 per fingerprint card for the national check. Ask MHLCS and the DHHS Criminal Records Check Unit. Also confirm whether G.S. 122C-80 applies to a peer-support-only agency that holds no DHSR license."
  },
  "step_11_sub_2": {
    "instructions": [
      "Search every employee, contractor, owner with 5% or more ownership, and managing employee in the OIG List of Excluded Individuals/Entities (LEIE) online search. Resolve any possible match before hire.",
      "Search the same names in SAM.gov exclusion records (federal debarment).",
      "Check each name against the NC Medicaid Provider Termination and Exclusion list (State Excluded Provider List). NC Medicaid updates it monthly, and its last publication was Sept. 24, 2026.",
      "Save dated screenshots or reports for each person, and keep a separate ownership screening record. Disclose 5%+ owners at enrollment as 42 CFR 455.104 requires.",
      "Do not employ, contract with, or bill for anyone who matches. Call a healthcare attorney and the NC Medicaid Contact Center to confirm next steps."
    ],
    "tips": [
      "AUDIT TRAP: Medicaid will not pay for items or services furnished, ordered or prescribed by an excluded person. OIG's 2013 bulletin cites civil monetary penalties of up to $10,000 per item or service, so one unscreened hire can create overpayment liability.",
      "Screen owners, board members, contractors, billing companies and staffing agencies as well as W-2 staff. Keep evidence for each.",
      "SAMHSA does not appear as an exclusion list in the sources reviewed. The three lists to use are LEIE, SAM.gov and the NC Medicaid exclusion list."
    ],
    "contacts": [
      "NC Medicaid Contact Center: 888-245-0179, Mon-Fri 8am-5pm (https://medicaid.ncdhhs.gov/providers/excluded-providers)"
    ],
    "sources": [
      "https://oig.hhs.gov/exclusions/background.asp",
      "https://medicaid.ncdhhs.gov/providers/excluded-providers",
      "https://sam.gov/content/exclusions",
      "https://www.law.cornell.edu/cfr/text/42/455.104"
    ],
    "confidence": "medium",
    "verify": "Confirm the current civil monetary penalty amounts with your healthcare attorney, since they are adjusted for inflation. Confirm whether your LME/MCO contract adds screening duties. The Cornell page for 42 CFR 455.104 is a secondary reproduction of the eCFR."
  },
  "step_11_sub_3": {
    "instructions": [
      "Create a recurring calendar task for the 11th of each month. OIG posts its LEIE updates by the 10th.",
      "Re-screen every employee, contractor and 5%+ owner against the LEIE. For rosters over about 25 people, download the LEIE database file and match it against your HR roster.",
      "In the same sitting, check the NC Medicaid State Excluded Provider List and SAM.gov.",
      "Save a dated report with the reviewer name and sign-off, and log months with no matches as well.",
      "If you find a match, remove the person from client-related work and billing that day. Then call your healthcare attorney and the NC Medicaid Contact Center."
    ],
    "tips": [
      "AUDIT TRAP: OIG says it has no required check frequency but advises routine checks. CMS guidance recommends monthly checks, and auditors and MCOs treat monthly as the norm. A missing month is a gap you must explain.",
      "Add new hires and terminations to the screening roster the same day, so no one is left unscreened between monthly runs.",
      "Your LME/MCO contract or provider manual may set its own screening frequency and reporting duty. Read it before signing."
    ],
    "contacts": [
      "NC Medicaid Contact Center: 888-245-0179, Mon-Fri 8am-5pm (https://medicaid.ncdhhs.gov/providers/excluded-providers)"
    ],
    "sources": [
      "https://oig.hhs.gov/exclusions/background.asp",
      "https://medicaid.ncdhhs.gov/providers/excluded-providers",
      "https://sam.gov/content/exclusions"
    ],
    "confidence": "medium",
    "verify": "Confirm the exact monthly cadence required by each LME/MCO you contract with. Confirm the LEIE posting schedule on the OIG exclusions page."
  },
  "step_12_sub_0": {
    "instructions": [
      "Open the NC Peer Support Specialist Certification Program Credential Verification page and search each hire by first and last name. A partial name works but may return several people.",
      "Confirm the result shows the initial certification date, most recent recertification date and Renew by date. Screenshot it with the date visible.",
      "Ask the CPSS for a copy of the current certificate. The program encourages employers to request one to confirm status.",
      "Add the person to your NC CPSS roster: name, date of hire, initial certification date, recertification date and separation date, as CCP 8G requires.",
      "Do not schedule billable peer support until the verification is on file."
    ],
    "tips": [
      "AUDIT TRAP: CCP 8G (amended effective Sept. 1, 2026) requires a roster of NC CPSS staff with certification and hire dates. Build it now, because payers and DHHS can ask for it.",
      "A certificate lapses on its expiration date, even if the CPSS later renews inside the 30-day late window. Check the Renew by date for every hire.",
      "Certificates arrive 10-14 business days after approval. A new CPSS who is still waiting for a certificate cannot be verified yet."
    ],
    "contacts": [
      "NC Peer Support Specialist Certification Program: nccpssprogram@unc.edu (no phone verified) (https://pss.unc.edu/verification)"
    ],
    "sources": [
      "https://pss.unc.edu/verification",
      "https://medicaid.ncdhhs.gov/blog/2026/10/02/amendment-clinical-coverage-policy-8g-peer-support-services",
      "https://medicaid.ncdhhs.gov/8g-peer-support-services/download?attachment"
    ],
    "confidence": "high",
    "verify": "Confirm the exact CCP 8G section number for the roster requirement in the current policy PDF. Confirm the program's institutional home. The App context says UNC School of Social Work, which the pages opened did not state."
  },
  "step_12_sub_1": {
    "instructions": [
      "Collect each CPSS's training proof. For Track A, that is the Foundations of Peer Support certificate (60 hours: 20 online plus 40 in person). For Track B, it is the approved 50-hour course certificate.",
      "Collect the certificates for the 20-hour prerequisite training (3 hours of ethics plus 17 hours of related training). These are separate from the Foundations or 50-hour course.",
      "For any CPSS past their first renewal, file recertification proof: 3 hours of ethics plus 17 additional hours (20 total) and the new certificate.",
      "Record course names, providers, hours and completion dates in a training log, and file copies in the personnel record."
    ],
    "tips": [
      "The App context is wrong here. Foundations is 60 hours on Track A, and the 50-hour course is Track B. The 20 hours are prerequisite training for certification, not general continuing education.",
      "AUDIT TRAP: Surveyors and payers ask for training documents in the personnel file. A certification number alone does not prove the hours.",
      "The program certifies the hours when it issues the credential, but your own file is what you produce in an audit."
    ],
    "contacts": [
      "NC Peer Support Specialist Certification Program: nccpssprogram@unc.edu (https://pss.unc.edu/certification)"
    ],
    "sources": [
      "https://pss.unc.edu/certification",
      "https://pss.unc.edu/training",
      "https://pss.unc.edu/certification/recertification"
    ],
    "confidence": "high",
    "verify": "Confirm current Track A and Track B requirements on pss.unc.edu before onboarding, since the program may change them (Track B approved courses are being phased out). Confirm who pays certification and recertification fees."
  },
  "step_12_sub_2": {
    "instructions": [
      "Collect a signed, dated statement from each CPSS confirming personal lived experience of a mental health condition, a substance use disorder, or both.",
      "Record which lived experience each CPSS has, so supervisors can match CPSS to beneficiaries with similar lived experiences as CCP 8G requires.",
      "Check that certification is active (step 12 sub 0). Certification requires at least 18 months in recovery before training, so it is the program's proof of that requirement.",
      "Store the statement in a restricted-access HR file. Do not ask for treatment records, and have your attorney review the form."
    ],
    "tips": [
      "No state-issued employer attestation form was found. The form is your own document. NOT VERIFIED whether an LME/MCO requires a specific format.",
      "AUDIT TRAP: Assigning a CPSS to a beneficiary without similar lived experience, such as a substance-use-only CPSS for a mental-health-only client, conflicts with CCP 8G.",
      "The 18 months of recovery is verified on the program's certification page. Earlier policy documents referenced 1 year, so rely on the current page."
    ],
    "contacts": [
      "NC Peer Support Specialist Certification Program: nccpssprogram@unc.edu (https://pss.unc.edu/certification)"
    ],
    "sources": [
      "https://pss.unc.edu/certification",
      "https://medicaid.ncdhhs.gov/8g-peer-support-services/download?attachment",
      "https://medicaid.ncdhhs.gov/blog/2026/10/02/amendment-clinical-coverage-policy-8g-peer-support-services"
    ],
    "confidence": "medium",
    "verify": "Have a healthcare or employment attorney review how to collect and store the attestation (ADA and confidentiality). Confirm the exact CCP 8G wording on similar lived experience."
  },
  "step_12_sub_3": {
    "instructions": [
      "At hire, enter each CPSS's Renew by date from the verification page in a shared calendar. Certification renews every two years from the initial certification date.",
      "Set reminders at 120, 90 and 60 days before the Renew by date, and tell the CPSS in writing.",
      "Make sure the CPSS completes the online recertification application with the 20 training hours (3 ethics plus 17) and the reference letters.",
      "Re-verify on the program's verification page after renewal and update the roster's recertification date.",
      "Remove the CPSS from billable work if the date passes without renewal. A late application is allowed within 30 days, with an extra $20 late fee."
    ],
    "tips": [
      "AUDIT TRAP: The program says the certificate expiration date is the official deadline, and certification is considered lapsed after it. Billing in a gap between expiration and late renewal is a risk.",
      "Certificates arrive 10-14 business days after approval, so submit renewals early.",
      "The renewal clock runs from the initial certification date, not the hire date."
    ],
    "contacts": [
      "NC Peer Support Specialist Certification Program: nccpssprogram@unc.edu (https://pss.unc.edu/certification/recertification)"
    ],
    "sources": [
      "https://pss.unc.edu/verification",
      "https://pss.unc.edu/certification/recertification",
      "https://pss.unc.edu/certification"
    ],
    "confidence": "high",
    "verify": "Confirm the regular recertification fee and the reference-letter requirements on the recertification page. Only the $20 late fee was confirmed here."
  },
  "step_13_sub_0": {
    "instructions": [
      "Call the fire marshal's office for the city or county where the site sits. Request an inspection for the proposed use as a business-type outpatient day program, and ask about fees and wait time.",
      "Give the inspector the program types (SAIOP under 10A NCAC 27G .4400, SACOT under .4500), the floor plan and the planned maximum client count.",
      "Correct every deficiency and obtain a dated, signed inspection report from the fire code official. Save a clear copy of the original.",
      "Include the report in the DHSR application. Put the next inspection on a 12-month calendar, because 10A NCAC 27G .0402(d)(3) requires annual fire and safety compliance for licensure."
    ],
    "tips": [
      "AUDIT TRAP: The NC Fire Code's statewide minimum frequency for business occupancies is every three years, but DHSR's rule requires annual fire and safety compliance. Follow the stricter DHSR rule.",
      "Programs serving children or adolescents may not be classed as business occupancy. Confirm the occupancy classification with the building official before leasing.",
      "Fire inspection fees were not found on any state page. They vary by jurisdiction."
    ],
    "contacts": [
      "DHSR Mental Health Licensure and Certification Section: 919-855-3795 (https://info.ncdhhs.gov/dhsr/mhlcs/establish.html)"
    ],
    "sources": [
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf",
      "https://info.ncdhhs.gov/dhsr/mhlcs/faq.html",
      "http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/subchapter%20g%20rules.html",
      "https://www.ncosfm.gov/codes/codes-current-and-past"
    ],
    "confidence": "medium",
    "verify": "NOT VERIFIED: the fire inspection fee, the local lead time and the current NC Fire Code edition. OSFM's page lists the 2018 code but also mentions a 2024 code update. Ask your local fire marshal which code applies. Also ask whether a peer-support-only site needs an inspection."
  },
  "step_13_sub_1": {
    "instructions": [
      "Find your county health department's environmental health section in the DHHS local health department directory, and ask whether your site needs a sanitation inspection.",
      "If you serve any food, request the sanitation inspection. DHSR requires a current report for day programs that serve any food, and food prepared for a fee requires a permit.",
      "Ask the health department to confirm the water supply and sewage disposal are approved. 10A NCAC 27G .0303 requires local health department approval of water and sewage.",
      "Check that restrooms are clean, working and private, then attach the written report to your DHSR application. If you serve no food, say so in your cover letter."
    ],
    "tips": [
      "The App context says every day facility needs a sanitation inspection. For day programs, DHSR requires a report only if you serve any food. Portioning counts as food preparation.",
      "AUDIT TRAP: Do not start a snack or lunch service after licensure without a sanitation report and a health department permit if required.",
      "Sanitation fees were not found on any state page and vary by county."
    ],
    "contacts": [
      "County health department environmental health section: phone listed per county in the DHHS directory (https://www.ncdhhs.gov/divisions/public-health/county-health-departments)"
    ],
    "sources": [
      "https://info.ncdhhs.gov/dhsr/mhlcs/faq.html",
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf",
      "https://www.ncdhhs.gov/divisions/public-health/county-health-departments",
      "http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/subchapter%20g%20rules.html"
    ],
    "confidence": "medium",
    "verify": "Ask your county environmental health office what it inspects for a clinic with no food service, and what it charges. If the site uses a private well or septic, ask about approval. Check whether SACOT meals or snacks trigger the food rule."
  },
  "step_13_sub_2": {
    "instructions": [
      "Ask the fire code official to state in writing the maximum occupant load for each group room, waiting area and office during or right after the inspection.",
      "Ask whether the fire official requires posted signs. If so, order durable signs with the approved number and post them in a conspicuous place near each room's main exit.",
      "Cap group sizes in your policies at the posted number. Check that your staffing meets the ratios in 10A NCAC 27G .4402 for SAIOP and .4502 for SACOT.",
      "Photograph the posted signs and file the photos with the fire report for the DHSR visit."
    ],
    "tips": [
      "NOT VERIFIED: whether the NC Fire Code requires posting in your group rooms. Posting rules tend to apply to assembly-type rooms, and the fire official decides the classification.",
      "AUDIT TRAP: A group larger than the occupant load the fire official sets is an overcrowding risk, so keep sign-in sheets that show attendance by group.",
      "Rooms often get rearranged. Re-measure and re-check the posted load whenever furniture or walls change."
    ],
    "contacts": [
      "DHSR Mental Health Licensure and Certification Section: 919-855-3795 (https://info.ncdhhs.gov/dhsr/mhlcs/establish.html)"
    ],
    "sources": [
      "https://www.oah.nc.gov/bcc-fire-code-final-revised-rule/open",
      "https://www.ncosfm.gov/codes/codes-current-and-past",
      "http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/subchapter%20g%20rules.html"
    ],
    "confidence": "low",
    "verify": "Ask the local fire code official whether posting is required for each room type and what the exact wording must be. No DHSR rule requiring posted occupancy signs was found."
  },
  "step_14_sub_0": {
    "instructions": [
      "Download the Initial Licensure Application Packet from the DHSR MHLCS Forms and Applications page (form DHHS/DHSR-MHL/5001, Rev 10-01-25), and follow the Day Program Checklist.",
      "Complete the application pages with facility name, site address, contact, facility director and licensure categories (.4400 SAIOP and .4500 SACOT). Disclose owners with 5% or more, as 10A NCAC 27G .0402 requires.",
      "Write the cover letter briefly describing the services you will offer, as the packet instructs.",
      "Sign with an original signature, and enclose a check or money order for the non-residential fee of $265.00.",
      "Mail the complete packet to DHSR MHLCS, 2718 Mail Service Center, Raleigh, NC 27699-2718. Submit at least 30 days before your planned start date."
    ],
    "tips": [
      "The App context fee of $350 base plus $12.50 per day is wrong. The $350 is the fee for residential facilities of 6 beds or fewer. Non-residential facilities pay $265.00, with no per-capacity charge.",
      "AUDIT TRAP: Incomplete packets are not processed, and day programs need original zoning approval for the application to move forward. Staff must be in place and the site furnished before a license is issued.",
      "CCP 8G peer support does not need a DHSR license, so this step applies only if you provide SAIOP or SACOT. The Jan. 1, 2026 CCP 8A-12 and 8A-13 also tie Medicaid enrollment to the licensure rule waiver process, so ask your consultant about timing."
    ],
    "contacts": [
      "DHSR Mental Health Licensure and Certification Section: 919-855-3795, fax 919-715-8078 (https://info.ncdhhs.gov/dhsr/mhlcs/establish.html)"
    ],
    "sources": [
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf",
      "https://info.ncdhhs.gov/dhsr/mhlcs/faq.html",
      "https://info.ncdhhs.gov/dhsr/mhlcs/establish.html",
      "https://info.ncdhhs.gov/dhsr/mhlcs/mhforms.html",
      "https://info.ncdhhs.gov/dhsr/mhlcs/lrwaiver.html",
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/newprovider.pdf",
      "https://medicaid.ncdhhs.gov/blog/2026/01/07/behavioral-health-clinical-coverage-policy-updates"
    ],
    "confidence": "high",
    "verify": "Confirm with MHLCS whether one application covers both .4400 and .4500 or each needs its own. Confirm the check payee name on the current packet. Confirm the waiver process timing, since the waiver request page was not fully read."
  },
  "step_14_sub_1": {
    "instructions": [
      "Obtain the original zoning approval from the local zoning office and attach the original. DHSR will not move the application forward without it.",
      "Attach a clear copy of the current local Fire Marshal inspection report from step 13.",
      "Attach a current sanitation inspection report only if you serve any food. Otherwise, state in your cover letter that no food is served.",
      "Add the Secretary of State report showing Active status, a floor plan with dimensions, interior and exterior photographs, and directions if the site cannot be found on Google Maps.",
      "Leave out the LME/MCO Letter of Support unless MHLCS asks for it. Add a local Building Official approval only for new construction or renovation."
    ],
    "tips": [
      "The App context is wrong that an LME/MCO Letter of Support is attached for these services. 10A NCAC 27G .0406 and the packet require it for 24-hour residential facilities only.",
      "An existing business-occupancy building with only a change of tenant may not need building official documentation. Ask the local Building Official and show them your application.",
      "AUDIT TRAP: The 24-hour residential checklist lists LME/MCO letters and inspection appointments, while the Day Program Checklist (Rev 10-01-25) asks for actual reports. Use the Day Program Checklist."
    ],
    "contacts": [
      "DHSR Mental Health Licensure and Certification Section: 919-855-3795 (https://info.ncdhhs.gov/dhsr/mhlcs/establish.html)"
    ],
    "sources": [
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf",
      "https://info.ncdhhs.gov/dhsr/mhlcs/faq.html",
      "http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/subchapter%20g%20rules.html"
    ],
    "confidence": "high",
    "verify": "The LME/MCO letter of support may still matter for the licensure rule waiver request. Confirm the current waiver requirements. Confirm local zoning wording with your zoning office."
  },
  "step_14_sub_2": {
    "instructions": [
      "Download the MH Licensure Policies and Procedures Worksheets from the packet and cross-walk each policy to the worksheet and the matching 10A NCAC 27G rule, including .4400 for SAIOP and .4500 for SACOT.",
      "Write procedures for every required area, including personnel, client rights, confidentiality, restrictive interventions and emergency plans, using the packet's rule references.",
      "Keep the manual ready but do not enclose it. The packet says to send policies later, and the FAQ says to submit the manual to your Licensure and Training Consultant at the first review.",
      "Include a disaster plan reviewed by county emergency management.",
      "Plan for the six-month program review window that starts once the consultant is assigned."
    ],
    "tips": [
      "The packet and FAQ conflict on timing. The packet says do not send policies with the application, and the FAQ says submit them at first review. Both are consistent with holding the manual for the consultant.",
      "AUDIT TRAP: The consultant checks that policies match the rules and that staff are trained on them. Generic manuals bought online often fail.",
      "DHSR construction does not do a plant review of day programs. The consultant assignment follows within about 5-10 days, and DHSR gives six months to finish."
    ],
    "contacts": [
      "DHSR Mental Health Licensure and Certification Section: 919-855-3795 (https://info.ncdhhs.gov/dhsr/mhlcs/establish.html)"
    ],
    "sources": [
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf",
      "https://info.ncdhhs.gov/dhsr/mhlcs/faq.html",
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/listmaterials.pdf",
      "http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/subchapter%20g%20rules.html"
    ],
    "confidence": "medium",
    "verify": "Ask your MHLCS consultant whether they want the manual before the first meeting, and in what format. Confirm the worksheet version in the current packet."
  },
  "step_14_sub_3": {
    "instructions": [
      "Build a staff roster of everyone who will work at the site, with name, role, hire date and credential or license number and expiration date.",
      "Verify each credential at its source board and record the date. SAIOP needs an LCAS or Certified Clinical Supervisor on site 50% of hours, SACOT 90% (10A NCAC 27G .4402 and .4502).",
      "Assemble a personnel record per person with the documents on the List of Required Materials, including HCPR proof within 90 days and criminal check within 180 days of the licensure review.",
      "Hold records for the consultant. The packet does not list a roster or personnel files as attachments.",
      "Enclose the $265.00 fee with the application."
    ],
    "tips": [
      "The App context says to attach a roster to the application. The packet checklist does not list one, and DHSR reviews personnel records at the program review. Confirm with your consultant.",
      "AUDIT TRAP: Check qualified professional ratios in the rules. SAIOP needs one QP per 12 adults or 6 adolescents, and SACOT one per 10 clients.",
      "CCP 8A-12 and 8A-13 (effective Jan. 1, 2026) list their own staff types, so check Medicaid qualifications as well as licensure rules."
    ],
    "contacts": [
      "DHSR Mental Health Licensure and Certification Section: 919-855-3795 (https://info.ncdhhs.gov/dhsr/mhlcs/establish.html)"
    ],
    "sources": [
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/listmaterials.pdf",
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf",
      "https://info.ncdhhs.gov/dhsr/mhlcs/faq.html",
      "http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/subchapter%20g%20rules.html",
      "https://medicaid.ncdhhs.gov/media/15767/download"
    ],
    "confidence": "medium",
    "verify": "Confirm with MHLCS what staff documents they want and when. Confirm whether the OAH rule text for .4400 and .4500 has changed since the OAH copy I read."
  }
}
```

## SOURCES

| Title | Publisher | URL | Date or version | Type |
|---|---|---|---|---|
| Initial Licensure Application Packet | NC DHSR MHLCS | [https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf](https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf) | Rev 10-01-25 | Primary |
| Establishing a new provider | NC DHSR MHLCS | [https://info.ncdhhs.gov/dhsr/mhlcs/establish.html](https://info.ncdhhs.gov/dhsr/mhlcs/establish.html) | Page dated 2026-10-03 | Primary |
| MHLCS FAQ | NC DHSR MHLCS | [https://info.ncdhhs.gov/dhsr/mhlcs/faq.html](https://info.ncdhhs.gov/dhsr/mhlcs/faq.html) | Page dated 2026-10-03 | Primary |
| New provider presentation | NC DHSR MHLCS | [https://info.ncdhhs.gov/dhsr/mhlcs/pdf/newprovider.pdf](https://info.ncdhhs.gov/dhsr/mhlcs/pdf/newprovider.pdf) | Undated | Primary |
| List of Required Materials | NC DHSR MHLCS | [https://info.ncdhhs.gov/dhsr/mhlcs/pdf/listmaterials.pdf](https://info.ncdhhs.gov/dhsr/mhlcs/pdf/listmaterials.pdf) | Rev 09/30/24 | Primary |
| Forms and Applications | NC DHSR MHLCS | [https://info.ncdhhs.gov/dhsr/mhlcs/mhforms.html](https://info.ncdhhs.gov/dhsr/mhlcs/mhforms.html) | Page dated 2026-09-23 | Primary |
| How to Request a Waiver of Licensure Rule | NC DHSR MHLCS | https://info.ncdhhs.gov/dhsr/mhlcs/lrwaiver.html[info.ncdhhs.gov](https://info.ncdhhs.gov/dhsr/mhlcs/lrwaiver.html?share_frome=aipt) | Page dated 2026-09-25 | Primary |
| 10A NCAC Subchapter 27G rules | NC OAH | http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/subchapter%20g%20rules.html | Current OAH copy; check for later amendments | Primary |
| G.S. 131E-256 | NC General Assembly | [https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_131E/GS_131E-256.html](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_131E/GS_131E-256.html) | Current | Primary |
| G.S. 122C-80 | NC General Assembly | [https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_122C/GS_122C-80.html](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_122C/GS_122C-80.html) | Current | Primary |
| Health Care Personnel Registry | NC DHSR | [https://info.ncdhhs.gov/dhsr/hcpr/index.html](https://info.ncdhhs.gov/dhsr/hcpr/index.html) | Current | Primary |
| CIHCPIS Provider Information | NC DHSR | [https://info.ncdhhs.gov/dhsr/ciu/provider.html](https://info.ncdhhs.gov/dhsr/ciu/provider.html) | Current | Primary |
| Verify Registry Listings | NC DHHS | [https://ncnar.ncdhhs.gov/verify_listings1.jsp](https://ncnar.ncdhhs.gov/verify_listings1.jsp) | Current | Primary |
| ABCMS | NC DHSR | [https://info.ncdhhs.gov/dhsr/abcms/index.html](https://info.ncdhhs.gov/dhsr/abcms/index.html) | Current | Primary |
| Non-Criminal Justice Access Agreement (SB-41) | NC SBI via DHSR | [https://info.ncdhhs.gov/dhsr/abcms/pdf/Non-Criminal-Justice-Access-Agreement-Form_SB-41.pdf](https://info.ncdhhs.gov/dhsr/abcms/pdf/Non-Criminal-Justice-Access-Agreement-Form_SB-41.pdf) | Undated form | Primary |
| NC Sex Offender Registry | NC SBI | https://sexoffender.ncsbi.gov/[sexoffender.ncsbi.gov](https://sexoffender.ncsbi.gov/?share_frome=aipt) | Current | Primary |
| LEIE background information | HHS OIG | https://oig.hhs.gov/exclusions/background.asp[oig.hhs.gov](https://oig.hhs.gov/exclusions/background.asp?share_frome=aipt) | Page dated 2026-04-10 | Primary |
| SAM.gov exclusions | GSA | https://sam.gov/content/exclusions[sam.gov](https://sam.gov/content/exclusions?share_frome=aipt) | Current | Primary |
| Excluded Providers | NC Medicaid | [https://medicaid.ncdhhs.gov/providers/excluded-providers](https://medicaid.ncdhhs.gov/providers/excluded-providers) | Page dated 2026-09-25; list published Sept. 24, 2026 | Primary |
| 42 CFR 455.104 | Cornell LII (copy of eCFR) | https://www.law.cornell.edu/cfr/text/42/455.104[law.cornell.edu](https://www.law.cornell.edu/cfr/text/42/455.104?share_frome=aipt) | Current | Secondary |
| NC Peer Support Specialist Certification | NC CPSS Program | [https://pss.unc.edu/certification](https://pss.unc.edu/certification) | Current | Primary |
| Training | NC CPSS Program | [https://pss.unc.edu/training](https://pss.unc.edu/training) | Current | Primary |
| Recertification | NC CPSS Program | [https://pss.unc.edu/certification/recertification](https://pss.unc.edu/certification/recertification) | Current | Primary |
| Credential Verification | NC CPSS Program | [https://pss.unc.edu/verification](https://pss.unc.edu/verification) | Current | Primary |
| CCP 8G Peer Support Services | NC Medicaid | [https://medicaid.ncdhhs.gov/8g-peer-support-services/download?attachment](https://medicaid.ncdhhs.gov/8g-peer-support-services/download?attachment) | Amended effective Sept. 1, 2026 | Primary |
| Amendment to CCP 8G | NC Medicaid | https://medicaid.ncdhhs.gov/blog/2026/10/02/amendment-clinical-coverage-policy-8g-peer-support-services[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/blog/2026/10/02/amendment-clinical-coverage-policy-8g-peer-support-services?share_frome=aipt) | Oct. 2, 2026 | Primary |
| Behavioral health CCP updates | NC Medicaid | https://medicaid.ncdhhs.gov/blog/2026/01/07/behavioral-health-clinical-coverage-policy-updates[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/blog/2026/01/07/behavioral-health-clinical-coverage-policy-updates?share_frome=aipt) | Jan. 7, 2026 | Primary |
| CCP 8A-12 SAIOP | NC Medicaid | https://medicaid.ncdhhs.gov/media/15767/download[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/media/15767/download?share_frome=aipt) | Effective Jan. 1, 2026 | Primary |
| Find Your Local Health Department | NC DHHS Division of Public Health | https://www.ncdhhs.gov/divisions/public-health/county-health-departments[ncdhhs.gov](https://www.ncdhhs.gov/divisions/public-health/county-health-departments?share_frome=aipt) | Page dated 2026-09-10 | Primary |
| NC Fire Code rule document | NC OAH | https://www.oah.nc.gov/bcc-fire-code-final-revised-rule/open[oah.nc.gov](https://www.oah.nc.gov/bcc-fire-code-final-revised-rule/open?share_frome=aipt) | Edition and date unclear | Primary |
| Codes - Current and Past | NC OSFM | https://www.ncosfm.gov/codes/codes-current-and-past[ncosfm.gov](https://www.ncosfm.gov/codes/codes-current-and-past?share_frome=aipt) | Current | Primary |

## CORRECTIONS

- Licensing fee: the App context says "$350 base fee + $12.50/day client capacity fee". Non-residential facilities pay a flat $265.00 with no capacity fee, per the [DHSR FAQ](https://info.ncdhhs.gov/dhsr/mhlcs/faq.html) and the [application packet](https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf). The $350 is the residential fee for 6 beds or fewer.
- LME/MCO Letter of Support: the App context lists it as an application attachment. It is required for 24-hour residential programs only, per [10A NCAC 27G .0406 and the packet](https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf). It does not appear on the Day Program Checklist.
- Policies and staff roster: the packet says policies are not sent with the application, and the checklist has no roster. The [FAQ](https://info.ncdhhs.gov/dhsr/mhlcs/faq.html) says the manual goes to the consultant at first review.
- CCP 8G licensure: DHSR does not license Peer Support Services, per the [new provider presentation](https://info.ncdhhs.gov/dhsr/mhlcs/pdf/newprovider.pdf). Step 14 applies to SAIOP and SACOT only. Steps 13 and 11 apply to a peer-support-only site only as good practice, and that is NOT VERIFIED.
- "SAMHSA exclusion logs": no SAMHSA exclusion list was found. Use OIG LEIE, SAM.gov and the [NC Medicaid exclusion list](https://medicaid.ncdhhs.gov/providers/excluded-providers).[oig.hhs.gov](https://oig.hhs.gov/exclusions/background.asp?share_frome=aipt)[sam.gov](https://sam.gov/content/exclusions?share_frome=aipt)
- HCPR scope: the statute defines health care personnel as unlicensed staff, but 10A NCAC 27G .0202(b)(4) applies to all service providers. The App context's "Sex Offender Registry" check is not required by any source found.
- SBI cost "$35 - $75": the [SBI access agreement form](https://info.ncdhhs.gov/dhsr/abcms/pdf/Non-Criminal-Justice-Access-Agreement-Form_SB-41.pdf) lists $38 per fingerprint card for the national check. The State-only fee is NOT VERIFIED.
- CPSS training: Foundations is 60 hours on Track A, and 50 hours is the Track B approved course, per the [program certification page](https://pss.unc.edu/certification). The 20 hours are prerequisite training, not continuing education. The 18 months of recovery is correct. Recertification is every two years and needs 20 hours.
- CPSS program affiliation: "UNC School of Social Work" was not stated on the pages opened. The program site is pss.unc.edu.
- Fire and sanitation: "$75-$250" fees are NOT VERIFIED. The OAH fire code document shows a three-year state minimum for business occupancies, but 10A NCAC 27G .0402(d)(3) requires annual compliance. Sanitation is required for day programs only if you serve food.[oah.nc.gov](https://www.oah.nc.gov/bcc-fire-code-final-revised-rule/open?share_frome=aipt)

## OPEN QUESTIONS

- Fingerprinting before licensure: ask the DHSR MHLCS consultant at 919-855-3795, and the DHHS Criminal Records Check Unit, how a not-yet-licensed applicant runs State and national checks, and the State-only fee.
- Licensure rule waiver timing: CCP 8A-12 and 8A-13 (effective Jan. 1, 2026) link Medicaid enrollment to a DHSR waiver request. Ask MHLCS (919-855-3795) when to file it, and whether an LME/MCO letter is needed.
- One application or two for SAIOP (.4400) and SACOT (.4500): ask MHLCS.
- Fire code edition and occupant-load sign rules: ask your local fire marshal. OSFM lists the 2018 code but mentions a 2024 update.
- Fire and sanitation fees and lead times: ask the local fire marshal's office and county environmental health.
- LME/MCO monthly screening and roster requirements: check each LME/MCO's provider contract and manual (Alliance, Trillium, Vaya, Partners).
- CPSS recertification fee and employer attestation format: ask nccpssprogram@unc.edu and your LME/MCO credentialing desk.