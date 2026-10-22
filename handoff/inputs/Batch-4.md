> From: https://www.perplexity.ai/computer/tasks/5307492b-c35b-4169-bac2-1bd55eebe177

# you asked

message time: 2026-10-18 20:13:23

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

---

# perplexity response

Searching: NC HealthConnex participation agreement 6-8 weeks no cost providers submit executed agreement email

---

# perplexity response

```json
{
  "step_15_sub_0": {
    "instructions": [
      "Call your Licensure and Training consultant at the DHSR Mental Health Licensure and Certification Section (MHLCS) to confirm the review date. DHSR allows six months from first contact to meet all requirements.",
      "Download the DHSR Facility Walk-Through form (rev. 12-17-25) from the MHLCS Forms page. Self-inspect every room you will use for SAIOP or SACOT before DHSR arrives.",
      "Furnish and equip the site fully before the visit, including a visible, working on-site facility telephone. Have your local fire, building and sanitation approvals available (10A NCAC 27G .0301).",
      "Keep the Facility Director and Clinical Director on site to lead the walkthrough and answer questions. Write down every item the consultant asks you to fix or show again."
    ],
    "tips": [
      "AUDIT TRAP: SAIOP and SACOT require a DHSR Mental Health License on the Provider Permission Matrix. Do not admit clients or bill before the license is issued. DHSR says issuing a license or MHL number may take up to three weeks after compliance.",
      "There is no separate survey fee. The only DHSR charge is the $265 non-residential initial license fee, which goes in with the application. G.S. 122C-23 bars license issuance until it is paid.",
      "The Provider Permission Matrix lists no DHSR license for Peer Support (CCP 8G). If you only offer 8G at a site, ask MHLCS in writing whether a walkthrough applies to that site."
    ],
    "contacts": [
      "DHSR Mental Health Licensure and Certification Section: 919-855-3795 (https://info.ncdhhs.gov/dhsr/mhlcs/)"
    ],
    "sources": [
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/FacilityWalk-Through.pdf",
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf",
      "https://info.ncdhhs.gov/dhsr/mhlcs/establish.html",
      "http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/10a%20ncac%2027g%20.0301.pdf",
      "https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx",
      "https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/BySection/Chapter_122C/GS_122C-23.pdf"
    ],
    "confidence": "medium",
    "verify": "NOT VERIFIED: the 4-8 week wait for the on-site visit. Ask your MHLCS consultant for the actual date. Also confirm whether a site offering only 8G Peer Support needs any DHSR walkthrough, and check the .0301 approval list against the rule text."
  },
  "step_15_sub_1": {
    "instructions": [
      "Run a Health Care Personnel Registry (HCPR) check on every employee before hire, at hcp.ncdhhs.gov/hcpr. Save a dated printout. 10A NCAC 27G .0202(b)(4) requires no substantiated findings.",
      "Complete a state and national criminal background check with fingerprints for each hire under G.S. 122C-80. DHSR asks for a check dated within 180 days and an HCPR check dated within 90 days.",
      "Build each personnel file from the DHSR Required Materials for Licensure Review list. Include credentials, client rights training, hands-on CPR, first aid, and restrictive intervention or de-escalation training certificates.",
      "Add trainer certificates for CPR, first aid and restrictive intervention instructors. Tab every file in the same order, then hand them to the consultant in one set at the review."
    ],
    "tips": [
      "AUDIT TRAP: An HCPR check dated after the hire date, or older than DHSR's 90-day window, is a common citation under 10A NCAC 27G .0202(b)(4). Run it before the offer letter and re-run it if the review slips.",
      "AUDIT TRAP: DHSR does not accept online-only CPR. Keep proof of the hands-on skills component with the certificate.",
      "Use the DHSR Staff Record Review worksheet and the Required Materials list as your internal audit sheet, and sample-check 100 percent of files one week before the visit."
    ],
    "contacts": [
      "DHSR Health Care Personnel Registry Office: 919-855-3969 (https://info.ncdhhs.gov/dhsr/hcpr/)",
      "DHSR Mental Health Licensure and Certification Section: 919-855-3795 (https://info.ncdhhs.gov/dhsr/mhlcs/)"
    ],
    "sources": [
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/listmaterials.pdf",
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/train/resource.pdf",
      "https://info.ncdhhs.gov/dhsr/hcpr/",
      "https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/BySection/Chapter_122C/GS_122C-80.pdf"
    ],
    "confidence": "high",
    "verify": "Confirm with your consultant whether the 90-day HCPR and 180-day criminal-check windows are measured from the review date or the application date. Confirm which national background-check and fingerprint vendor DHSR accepts."
  },
  "step_15_sub_2": {
    "instructions": [
      "Use the correct rules. 10A NCAC 27G .0209 is Medication Requirements. Restrictive intervention rules are 10A NCAC 27E .0101 through .0108, including .0104 (seclusion, restraint, time-out) and .0107 and .0108 (training).",
      "Complete the DHSR MH Licensure Policies and Procedures Worksheet. Map each client rights and intervention rule to a page in your policy manual before the review.",
      "Write a restrictive intervention policy stating which interventions, if any, you permit. Ask your consultant what training is still required if you permit none. Train every staff member using a DHHS-approved de-escalation curriculum.",
      "Rehearse interview answers with the Facility Director and Clinical Director on client rights, grievances, least restrictive alternatives (27E .0101) and incident reporting. Keep training rosters and certificates ready."
    ],
    "tips": [
      "AUDIT TRAP: Citing 27G .0209 as the restraint rule in your manual signals that policies were not checked against the rule text. Cite 27E in the policy and on the DHSR worksheet.",
      "AUDIT TRAP: DHSR asks for the approved curriculum name and instructor certification for de-escalation and restrictive intervention training. Training without a listed curriculum or certified instructor is a common finding.",
      "SAIOP rules are 10A NCAC 27G .4400 and SACOT rules are 10A NCAC 27G .4500. Check your service descriptions and staffing patterns against those rule sections as well as the CCP."
    ],
    "contacts": [
      "DHSR Mental Health Licensure and Certification Section: 919-855-3795 (https://info.ncdhhs.gov/dhsr/mhlcs/)"
    ],
    "sources": [
      "http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/10a%20ncac%2027g%20.0209.pdf",
      "http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20e/10a%20ncac%2027e%20.0104.pdf",
      "http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20e/10a%20ncac%2027e%20.0107.pdf",
      "http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20e/10a%20ncac%2027e%20.0108.pdf",
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/listmaterials.pdf",
      "https://www.ncdhhs.gov/divisions/mental-health-developmental-disabilities-and-substance-use-services/involuntary-commitment/training-requirements-use-non-restrictive-and-restrictive-intervention-strategies"
    ],
    "confidence": "medium",
    "verify": "Confirm the current text of 10A NCAC 27E .0101 to .0108 and the client rights rules on the OAH site. Ask your consultant whether a no-restraint facility still needs the 27E .0107 and .0108 training. The client rights rule citations beyond 27E were not opened, so confirm them in the DHSR worksheet."
  },
  "step_16_sub_0": {
    "instructions": [
      "Read the Statement of Deficiencies (SOD) and list every cited rule. Write one plan entry per citation, using the example format in the DHSR Provider Resource Manual.",
      "State the root cause for each citation, such as a missing policy, untrained staff or no tracking system. Do not blame an individual.",
      "Describe a systemic change that covers all clients and staff, not just the cited record. Examples are a rewritten policy, retraining with sign-in sheets, or a new checklist.",
      "Name the responsible person, completion date and monitoring frequency, such as a monthly audit of a set number of records reviewed by the Clinical Director. Keep evidence for the follow-up visit."
    ],
    "tips": [
      "AUDIT TRAP: A plan that fixes only the cited example is the usual reason DHSR rejects a POC. Show that the same gap cannot recur in other files, staff or sites.",
      "AUDIT TRAP: Correction dates count from the survey exit date, not the SOD receipt date. Type A1/A2 is 23 days, Type B is 45 days, standard level is 60 days, and re-cited standard level is 30 days. A follow-up visit verifies the fix.",
      "The DHSR Provider Resource Manual is revised 9/4/2019, so older than other sources. Use the deadlines and state form named in your own SOD letter if they differ."
    ],
    "contacts": [
      "DHSR Mental Health Licensure and Certification Section: 919-855-3795 (https://info.ncdhhs.gov/dhsr/mhlcs/)"
    ],
    "sources": [
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/train/resource.pdf",
      "https://info.ncdhhs.gov/dhsr/mhlcs/establish.html"
    ],
    "confidence": "medium",
    "verify": "NOT VERIFIED: how DHSR communicates findings on an initial licensure review (a formal SOD or a correction request before licensing). Ask your consultant. Confirm current POC deadlines and the form against the SOD letter you receive."
  },
  "step_16_sub_1": {
    "instructions": [
      "Find the return deadline in the DHSR letter that came with the SOD. The Provider Resource Manual letter template says to return the signed form within 10 days of receipt of the SOD.",
      "Complete the POC on the state form DHSR attached to the letter. Have the authorized owner or director sign and date it.",
      "Return the original to MHLCS at 2718 Mail Service Center, Raleigh, NC 27699-2718, using tracked delivery. Ask your consultant whether email submission is accepted before relying on it.",
      "Call your consultant to confirm receipt. Then complete every correction inside the 23, 30, 45 or 60-day window counted from the exit date."
    ],
    "tips": [
      "AUDIT TRAP: Missing the 10-day return or the exit-date correction window can lead to enforcement. Administrative penalties for uncorrected deficiencies are described in the DHSR resource manual. Calendar both dates on the day the SOD arrives.",
      "Send documents DHSR requested with the POC, such as revised policies and training rosters, and keep a duplicate set. DHSR notes that a follow-up visit verifies all corrections."
    ],
    "contacts": [
      "DHSR Mental Health Licensure and Certification Section: 919-855-3795 (https://info.ncdhhs.gov/dhsr/mhlcs/)"
    ],
    "sources": [
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/train/resource.pdf"
    ],
    "confidence": "medium",
    "verify": "The 10-day return and mailing address come from a 2019 template letter. Confirm the due date, form and submission method (mail, fax or email) in the SOD you actually receive."
  },
  "step_16_sub_2": {
    "instructions": [
      "Confirm DHSR has your initial license fee and has cleared all corrections. Allow up to three weeks for DHSR to issue the license or MHL number after the review is complete.",
      "Check the license for exact legal name, site address, license number and effective date. Confirm the licensed service categories include SAIOP (10A NCAC 27G .4400) and SACOT (10A NCAC 27G .4500).",
      "Save a PDF and file the original in your credentials repository. NCTracks, Tailored Plans and CARF or other accreditors will ask for it repeatedly.",
      "Calendar the annual renewal. Licenses expire at the end of the calendar year and must be renewed annually under G.S. 122C-23."
    ],
    "tips": [
      "AUDIT TRAP: If the service categories on the license do not match the services you enroll in NCTracks, the claim or enrollment can be denied. Ask DHSR for a corrected license before you submit the NCTracks application.",
      "Any change of address, service or ownership requires a change application to DHSR before it takes effect, so do not move or add a service without checking with MHLCS first.",
      "Peer Support alone has no DHSR license requirement on the Provider Permission Matrix, so your 8G service will not appear as a separate licensed category. Do not expect it on the license."
    ],
    "contacts": [
      "DHSR Mental Health Licensure and Certification Section: 919-855-3795 (https://info.ncdhhs.gov/dhsr/mhlcs/)"
    ],
    "sources": [
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/FacilityWalk-Through.pdf",
      "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf",
      "https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/BySection/Chapter_122C/GS_122C-23.pdf",
      "https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx"
    ],
    "confidence": "medium",
    "verify": "NOT VERIFIED: the exact wording of service designations printed on the license. Ask MHLCS for a sample or confirm after issuance. The three-week figure comes from DHSR's walk-through form acknowledgment, not a guaranteed timeline."
  },
  "step_17_sub_0": {
    "instructions": [
      "Download the Full Participation Agreement for traditional health care providers from the NC HIEA Participation Agreement page. It is a PDF, not an online signing portal.",
      "Fill in your legal entity name, formal notice contact (attachment 1), and three contacts: participant account administrator, contract administrator and technical resource (attachment 2). Add participating entities if any (attachment 4).",
      "Complete the Business Associate Agreement (attachment 5) with your entity name and sign under Covered Entity. Have an authorized officer sign, ideally after healthcare attorney review.",
      "Email the completed PDF to hiea@nc.gov (preferred) or mail it to N.C. Health Information Exchange Authority, Mail Service Center 4101, Raleigh, NC 27699-4101. Allow 6 to 8 weeks for the executed copy."
    ],
    "tips": [
      "There is no fee to connect now. Start this step as soon as you have a legal entity, because processing is 6 to 8 weeks. Waiting for the DHSR license is not required by the HIEA.",
      "AUDIT TRAP: Missing or inaccurate information delays processing. A new agreement replaces any earlier one, so do not sign duplicates.",
      "SAIOP and SACOT records covered by 42 CFR Part 2 are exempt from submission under G.S. 90-414.4(c), and HIEA says it does not currently receive Part 2 data. Document how your EHR filters those records."
    ],
    "contacts": [
      "N.C. Health Information Exchange Authority: 919-754-6912 (https://hiea.nc.gov/)"
    ],
    "sources": [
      "https://hiea.nc.gov/providers/how-connect/nc-healthconnex-participation-agreement",
      "https://hiea.nc.gov/providers/what-does-law-mandate",
      "https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/BySection/Chapter_90/GS_90-414.4.pdf"
    ],
    "confidence": "high",
    "verify": "Attachment and page numbers are from the HIEA page and may shift when the agreement is updated. Ask HIEA whether a Part 2 program should sign Full or Submission-only, and have a healthcare attorney review the business associate terms."
  },
  "step_17_sub_1": {
    "instructions": [
      "Ask each EHR vendor in writing whether it can send HL7 version 2.0 or higher messages and has connected other providers to NC HealthConnex.",
      "Ask for ADT messages sent in real time and/or CCD documents within 24 hours of the encounter close, per the HIEA onboarding packet. Ask about sFTP or TLS connection options.",
      "Confirm in writing that the EHR can filter or withhold 42 CFR Part 2 substance use disorder records and non-state-funded data, as the HIEA expects of submission-only participants.",
      "Get the vendor's interface fee and timeline in writing before you sign. State fees are zero, but vendor fees vary. Share the technical contact with HIEA."
    ],
    "tips": [
      "The HIEA asks only that your EHR can send HL7 v2.0 or higher. ONC-certified products are preferred. No HIEA vendor certification program was found, and FHIR is used for health plan access, so do not require FHIR of your vendor.",
      "AUDIT TRAP: If you pick an EHR that cannot filter Part 2 records, you risk disclosing SUD records without consent. Test Part 2 filtering before go-live.",
      "The onboarding packet found is a 2021 edition. Request the current packet from HIEA before you finalize specs with your vendor."
    ],
    "contacts": [
      "N.C. Health Information Exchange Authority: 919-754-6912 (https://hiea.nc.gov/)"
    ],
    "sources": [
      "https://hiea.nc.gov/providers/how-connect/nc-healthconnex-participation-agreement",
      "https://hiea.nc.gov/nc-healthconnex-onboarding-packet-and-technical-specifications/download?attachment",
      "https://hiea.nc.gov/faqs/health-care-provider-faqs",
      "https://hiea.nc.gov/providers/what-does-law-mandate"
    ],
    "confidence": "medium",
    "verify": "Request the current onboarding packet and message-type requirements from HIEA, because the packet found is a 2021 edition. Ask whether SUD or peer-support-only providers have a reduced data set."
  },
  "step_17_sub_2": {
    "instructions": [
      "Work through onboarding with HIEA and your EHR vendor after the agreement is executed. Run test messages and go live. Data on state-funded services must flow at least twice daily.",
      "Request written confirmation of connection status from HIEA at hiea@nc.gov. Save it, with the executed agreement, in your compliance file.",
      "Ask each Tailored Plan or LME/MCO you contract with, and NC Medicaid enrollment, whether they require proof of HIE connection before billing. Document the answer.",
      "Do not plan on an extension. The hardship process in G.S. 90-414.4(a3) exists, but it cannot extend beyond the statutory connection date of January 1, 2023. Contact HIEA if you cannot connect."
    ],
    "tips": [
      "AUDIT TRAP: No source found requires filing proof of connection with NCTracks before billing. Do not tell staff that billing is blocked or allowed on this basis until you confirm with HIEA, NC Medicaid and your Tailored Plan.",
      "Keep records of what you sent, what you withheld under 42 CFR Part 2, and the dates, so you can show good-faith compliance with the HIE Act if asked."
    ],
    "contacts": [
      "N.C. Health Information Exchange Authority: 919-754-6912 (https://hiea.nc.gov/)"
    ],
    "sources": [
      "https://hiea.nc.gov/providers/what-does-law-mandate",
      "https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/BySection/Chapter_90/GS_90-414.4.pdf",
      "https://hiea.nc.gov/providers/how-connect/nc-healthconnex-participation-agreement"
    ],
    "confidence": "medium",
    "verify": "NOT VERIFIED: whether a new provider that began billing after January 1, 2023 has a grace period, and whether any payer or NCTracks requires proof of connection. Ask HIEA, NC Medicaid Provider Ombudsman and your Tailored Plan contracting desk."
  },
  "step_18_sub_0": {
    "instructions": [
      "Pick the Office Administrator (OA). The OA must be listed in the application as an owner or managing employee, such as a director, administrator or general manager.",
      "Have the OA register at the Register Now link on the NCTracks Provider Portal login page, which leads to the NCID home page. Use a personal NCID, not a shared login.",
      "Set up multi-factor authentication (MFA), which NCTracks requires, using phone or mobile app. Test login on the portal before starting the application.",
      "Record the NCID username. You will enter it on the Organization Basic Information page, and add a second managing employee to the record as a backup."
    ],
    "tips": [
      "NCTracks warns that three failed password attempts lock the account. Practice logging in once before the application session.",
      "AUDIT TRAP: If the OA leaves, only an owner or managing employee on file can replace the OA. Adding a second managing employee now prevents a stuck account."
    ],
    "contacts": [
      "NCTracks CSRA Call Center: 800-688-6696 (https://www.nctracks.nc.gov/content/public/providers/provider-enrollment.html)"
    ],
    "sources": [
      "https://www.nctracks.nc.gov/content/dam/jcr:8d0d2b03-b987-41b2-855c-cb5d1ad4980f/PUGPRV593.pdf",
      "https://www.nctracks.nc.gov/content/public/providers/provider-enrollment.html"
    ],
    "confidence": "high",
    "verify": "The NCID registration page URL and identity-proofing steps were not opened. Follow the NCTracks Register Now link and the state NCID guidance for current steps."
  },
  "step_18_sub_1": {
    "instructions": [
      "Confirm your organization NPI is active (Step 3) and your legal name and EIN match IRS records. Review the Provider Permission Matrix dated 08-16-2026 for your services.",
      "Log in to the NCTracks Provider Portal with the OA's NCID and start the Organization enrollment for NC Medicaid. Enter basic information, ownership and managing employees, the OA, and exclusion and sanction answers.",
      "Pay the fees. The $100 NC Provider Application Fee applies, and the Provider Permission Matrix flags a federal application fee, site visit and fingerprinting for taxonomy 251S00000X (high risk). The 2026 federal fee is $750.",
      "Sign the W-9 attestation and application electronically and submit. Within 15 calendar days, finish the NC Medicaid New Provider Training, which is required before initial enrollment under G.S. 108C-9."
    ],
    "tips": [
      "AUDIT TRAP: Taxonomy 251S00000X providers must have at least one Service selected on the Provider Permission Matrix. NC Medicaid extended the deadline to October 1, 2026, so confirm that Peer Support, SAIOP and SACOT show on your record.",
      "Disclose every owner and managing employee, since high-risk status means fingerprinting for owners. Omitted owners or incomplete sanction documentation are a common cause of denial.",
      "The NCTracks Organization user guide (D2.0.1, Sept 3, 2025) has no HIE page, so the NCTracks application itself does not ask for NC HealthConnex proof."
    ],
    "contacts": [
      "NCTracks CSRA Call Center: 800-688-6696 (https://www.nctracks.nc.gov/content/public/providers/provider-enrollment.html)",
      "PCG Provider Enrollment Support: 877-522-1057 option 2 (https://medicaid.ncdhhs.gov/providers/programs-and-services/behavioral-health-mental-health-idd)"
    ],
    "sources": [
      "https://www.nctracks.nc.gov/content/dam/jcr:8d0d2b03-b987-41b2-855c-cb5d1ad4980f/PUGPRV593.pdf",
      "https://www.nctracks.nc.gov/content/public/providers/provider-enrollment.html",
      "https://www.nctracks.nc.gov/content/dam/jcr:5088259c-ab17-4c01-bf6d-c64786be1da4/State%20and%20Federal%20Fee%20Amounts%20by%20Year.xlsx",
      "https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx",
      "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-Behavioral-Health-Provider-Enrollment.html",
      "https://medicaid.ncdhhs.gov/provider-enrollment-2026-summer-and-fall-series-1-powerpoint/open"
    ],
    "confidence": "high",
    "verify": "Check the fee amounts on the NCTracks fee page on the day you apply. Confirm fingerprinting and site-visit steps and timelines with NCTracks, and ask whether any federal fee waiver applies (for example, Medicare enrollment). Processing time was not stated by a source."
  },
  "step_18_sub_2": {
    "instructions": [
      "Select taxonomy 251S00000X, Agencies - Community/Behavioral Health. The Provider Permission Matrix shows this as the only Medicaid organization taxonomy for these three services.",
      "Add the services CIS Services - Peer Support Services, Substance Abuse Intensive Outpatient Program, and Substance Abuse Comprehensive Outpatient Treatment Program. Match each to the CCP you are billing (8G, 8A-12, 8A-13).",
      "Read the matrix rows for each service. SAIOP and SACOT require an NC DHSR Mental Health License and accreditation within 3 years of enrolling the service. Peer Support requires accreditation within 1 year and no DHSR license.",
      "Calendar the accreditation deadline. Accepted bodies for these services on the matrix are CARF, the Joint Commission, CQL and COA."
    ],
    "tips": [
      "AUDIT TRAP: Enrolling under 251S00000X without a service selected is no longer allowed. NC Medicaid set October 1, 2026 as the deadline for existing providers, and a new application needs services chosen up front.",
      "Do not choose a different taxonomy to avoid the high-risk screening. The matrix controls which taxonomy supports which service.",
      "NC Medicaid announced national accreditation changes for behavioral health services. Check the Medicaid behavioral health page for the current accreditation timeline before you apply."
    ],
    "contacts": [
      "NCTracks CSRA Call Center: 800-688-6696 (https://www.nctracks.nc.gov/content/public/providers/provider-enrollment.html)"
    ],
    "sources": [
      "https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx",
      "https://medicaid.ncdhhs.gov/providers/programs-and-services/behavioral-health-mental-health-idd",
      "https://medicaid.ncdhhs.gov/provider-enrollment-2026-summer-and-fall-series-1-powerpoint/open"
    ],
    "confidence": "high",
    "verify": "Re-download the current Provider Permission Matrix on the day you apply, since it is updated often (this entry uses the 08-16-2026 version). Confirm that accreditation is not required earlier by your Tailored Plan contract."
  },
  "step_18_sub_3": {
    "instructions": [
      "Check the Required Attachments section of the application. In the NCTracks Organization guide (Sept 2025), listed uploads are the CMS Medicare letter, DME, NP certificate, CLIA and sanction documents. A DHSR license is not listed.",
      "Do not upload a W-9. Organizations electronically sign the W-9 Attestation for Organizations as part of the online application.",
      "Enter bank details on the EFT Account Information page. All NCTracks payments are by EFT. Use the account in the organization's legal name and EIN.",
      "If NCTracks asks for any extra document, upload it or send it by email, fax or mail with the NPI shown: NCTracksprovider@nctracks.com, fax 855-710-1965, NCTracks, PO Box 300009, Raleigh, NC 27622-8009."
    ],
    "tips": [
      "NCTracks verifies the DHSR license against the state's own records according to the matrix, so the license number and service categories must be exact on the application. Keep a copy anyway for LME/MCO credentialing.",
      "AUDIT TRAP: A bank name, account title or EIN that does not match the legal entity delays EFT setup and payment. Use the same name as on your W-9 and IRS records.",
      "Attach accreditation proof if your taxonomy's Required Attachments section lists it. Documents sent by email, fax or mail must show the NPI or they may be misrouted."
    ],
    "contacts": [
      "NCTracks CSRA Call Center: 800-688-6696 (https://www.nctracks.nc.gov/content/public/providers/provider-enrollment.html)"
    ],
    "sources": [
      "https://www.nctracks.nc.gov/content/dam/jcr:8d0d2b03-b987-41b2-855c-cb5d1ad4980f/PUGPRV593.pdf",
      "https://per.nctracks.com/content/public/providers/provider-enrollment/terms-and-conditions.html",
      "https://www.nctracks.nc.gov/content/dam/jcr:7d4728a7-9427-4ebb-9d21-3f1262cbf772/PUG_Human%20Service%20Organization%20Enrollment%20Participant%20User%20Guide.pdf",
      "https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx"
    ],
    "confidence": "medium",
    "verify": "NOT VERIFIED: whether NCTracks asks for a voided check or bank letter at the EFT step for organizations. The EFT page description comes from a 2022 Human Service Organization guide. Call the CSRA Call Center to confirm, and confirm whether a DHSR license upload is ever requested."
  }
}
```

## SOURCES

| Title | Publisher | URL | Date or version | Type |
|---|---|---|---|---|
| Initial licensure application packet | NC DHSR MHLCS | [https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf](https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf) | Rev. 10/01/25 | Primary |
| Required Materials for Licensure Review | NC DHSR MHLCS | [https://info.ncdhhs.gov/dhsr/mhlcs/pdf/listmaterials.pdf](https://info.ncdhhs.gov/dhsr/mhlcs/pdf/listmaterials.pdf) | Current | Primary |
| Facility Walk-Through form | NC DHSR MHLCS | [https://info.ncdhhs.gov/dhsr/mhlcs/pdf/FacilityWalk-Through.pdf](https://info.ncdhhs.gov/dhsr/mhlcs/pdf/FacilityWalk-Through.pdf) | Rev. 12-17-25 | Primary |
| Provider Resource Manual | NC DHSR MHLCS | [https://info.ncdhhs.gov/dhsr/mhlcs/pdf/train/resource.pdf](https://info.ncdhhs.gov/dhsr/mhlcs/pdf/train/resource.pdf) | Rev. 9/4/2019 | Primary, older |
| Establishing a facility page | NC DHSR MHLCS | [https://info.ncdhhs.gov/dhsr/mhlcs/establish.html](https://info.ncdhhs.gov/dhsr/mhlcs/establish.html) | Current | Primary |
| Health Care Personnel Registry | NC DHSR | https://info.ncdhhs.gov/dhsr/hcpr/[info.ncdhhs.gov](https://info.ncdhhs.gov/dhsr/hcpr/?share_frome=aipt) | Current | Primary |
| 10A NCAC 27G .0209, .0301, .4400, .4500 | NC OAH | http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/10a%20ncac%2027g%20.0209.pdf | Current | Primary |
| 10A NCAC 27E .0104, .0107, .0108 | NC OAH | http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20e/10a%20ncac%2027e%20.0104.pdf | Current | Primary |
| Training requirements for restrictive interventions | NC DHHS | https://www.ncdhhs.gov/divisions/mental-health-developmental-disabilities-and-substance-use-services/involuntary-commitment/training-requirements-use-non-restrictive-and-restrictive-intervention-strategies[ncdhhs.gov](https://www.ncdhhs.gov/divisions/mental-health-developmental-disabilities-and-substance-use-services/involuntary-commitment/training-requirements-use-non-restrictive-and-restrictive-intervention-strategies?share_frome=aipt) | Current | Primary |
| G.S. 122C-23 and G.S. 122C-80 | NC General Assembly | https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/BySection/Chapter_122C/GS_122C-23.pdf[ncleg.gov](https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/BySection/Chapter_122C/GS_122C-23.pdf?share_frome=aipt) | Current | Primary |
| G.S. 90-414.4 | NC General Assembly | https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/BySection/Chapter_90/GS_90-414.4.pdf[ncleg.gov](https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/BySection/Chapter_90/GS_90-414.4.pdf?share_frome=aipt) | Last amended 2023 | Primary |
| NC HealthConnex Participation Agreement page | NC HIEA | https://hiea.nc.gov/providers/how-connect/nc-healthconnex-participation-agreement[hiea.nc.gov](https://hiea.nc.gov/providers/how-connect/nc-healthconnex-participation-agreement?share_frome=aipt) | Current | Primary |
| What does the law mandate | NC HIEA | [https://hiea.nc.gov/providers/what-does-law-mandate](https://hiea.nc.gov/providers/what-does-law-mandate) | Current | Primary |
| Health care provider FAQs | NC HIEA | [https://hiea.nc.gov/faqs/health-care-provider-faqs](https://hiea.nc.gov/faqs/health-care-provider-faqs) | Current | Primary |
| Data Specifications Onboarding Packet | NC HIEA | https://hiea.nc.gov/nc-healthconnex-onboarding-packet-and-technical-specifications/download?attachment[hiea.nc.gov](https://hiea.nc.gov/nc-healthconnex-onboarding-packet-and-technical-specifications/download?attachment=&share_frome=aipt) | 2021 edition | Primary, older |
| Provider enrollment page | NCTracks | https://www.nctracks.nc.gov/content/public/providers/provider-enrollment.html[nctracks.nc.gov](https://www.nctracks.nc.gov/content/public/providers/provider-enrollment.html?share_frome=aipt) | Current | Primary |
| Provider Permission Matrix | NCTracks / NC Medicaid | [https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx](https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx) | 08-16-2026 | Primary |
| State and Federal Fee Amounts by Year | NCTracks | [https://www.nctracks.nc.gov/content/dam/jcr:5088259c-ab17-4c01-bf6d-c64786be1da4/State%20and%20Federal%20Fee%20Amounts%20by%20Year.xlsx](https://www.nctracks.nc.gov/content/dam/jcr:5088259c-ab17-4c01-bf6d-c64786be1da4/State%20and%20Federal%20Fee%20Amounts%20by%20Year.xlsx) | Current | Primary |
| Enroll in NC Medicaid - Organization user guide (PUG_PRV593) | NCTracks | https://www.nctracks.nc.gov/content/dam/jcr:8d0d2b03-b987-41b2-855c-cb5d1ad4980f/PUGPRV593.pdf[nctracks.nc.gov](https://www.nctracks.nc.gov/content/dam/jcr:8d0d2b03-b987-41b2-855c-cb5d1ad4980f/PUGPRV593.pdf?share_frome=aipt) | D2.0.1, Sept 3, 2025 | Primary |
| Human Service Organization enrollment guide | NCTracks | [https://www.nctracks.nc.gov/content/dam/jcr:7d4728a7-9427-4ebb-9d21-3f1262cbf772/PUG_Human%20Service%20Organization%20Enrollment%20Participant%20User%20Guide.pdf](https://www.nctracks.nc.gov/content/dam/jcr:7d4728a7-9427-4ebb-9d21-3f1262cbf772/PUG_Human%20Service%20Organization%20Enrollment%20Participant%20User%20Guide.pdf) | Oct 27, 2022 | Primary, older |
| Behavioral Health Provider Enrollment FAQs | NCTracks | https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-Behavioral-Health-Provider-Enrollment.html[nctracks.nc.gov](https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-Behavioral-Health-Provider-Enrollment.html?share_frome=aipt) | Current | Primary |
| Terms and conditions (W-9 attestation) | NCTracks | https://per.nctracks.com/content/public/providers/provider-enrollment/terms-and-conditions.html[per.nctracks.com](https://per.nctracks.com/content/public/providers/provider-enrollment/terms-and-conditions.html?share_frome=aipt) | Current | Primary |
| Provider Enrollment 2026 Summer and Fall Series | NC Medicaid | https://medicaid.ncdhhs.gov/provider-enrollment-2026-summer-and-fall-series-1-powerpoint/open[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/provider-enrollment-2026-summer-and-fall-series-1-powerpoint/open?share_frome=aipt) | 2026 | Primary |
| Behavioral health, mental health, IDD page | NC Medicaid | https://medicaid.ncdhhs.gov/providers/programs-and-services/behavioral-health-mental-health-idd[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers/programs-and-services/behavioral-health-mental-health-idd?share_frome=aipt) | Current | Primary |

## CORRECTIONS

- **Step 15, "4-8 weeks queue wait":** NOT VERIFIED. DHSR states only that an applicant has six months from first contact with a Licensure and Training team member to meet all requirements ([DHSR application packet](https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf)).
- **Step 15, "$0 (included in filing)":** Mostly right. The $265 non-residential initial license fee is paid with the application, and G.S. 122C-23 bars issuance until it is paid ([DHSR packet](https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf)).
- **Step 15, applies to CCP 8G:** The matrix lists no DHSR license for Peer Support, but does for SAIOP and SACOT ([Provider Permission Matrix](https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx)). Steps 15 and 16 may not apply to an 8G-only site.
- **Step 15, 10A NCAC 27G .0209:** This rule is Medication Requirements. Restrictive interventions are in 10A NCAC 27E .0101 to .0108 ([OAH 27E .0104](http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20e/10a%20ncac%2027e%20.0104.pdf)).[reports.oah.state.nc.us](http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/10a%20ncac%2027g%20.0209.pdf?share_frome=aipt)
- **Step 16, "10-15 calendar days":** DHSR's template says return the POC within 10 days of receipt of the SOD. No 15-day figure was found ([Provider Resource Manual](https://info.ncdhhs.gov/dhsr/mhlcs/pdf/train/resource.pdf), rev. 9/4/2019).
- **Step 16, correction timing:** Correction deadlines run from the survey exit date: A1/A2 23 days, B 45 days, standard 60 days, re-cited standard 30 days ([Provider Resource Manual](https://info.ncdhhs.gov/dhsr/mhlcs/pdf/train/resource.pdf)).
- **Step 16, "2-4 weeks" to license:** DHSR says issuing a license or MHL number may take up to three weeks ([Walk-Through form](https://info.ncdhhs.gov/dhsr/mhlcs/pdf/FacilityWalk-Through.pdf)).
- **Step 17, "mandatory full participation agreement ... online":** The agreement is a PDF emailed to hiea@nc.gov or mailed, not signed online. Several types exist, and a Submission-only option is available.[hiea.nc.gov](https://hiea.nc.gov/providers/how-connect/nc-healthconnex-participation-agreement?share_frome=aipt)
- **Step 17, "3-6 weeks":** HIEA says to allow 6 to 8 weeks to receive the executed agreement.[hiea.nc.gov](https://hiea.nc.gov/providers/how-connect/nc-healthconnex-participation-agreement?share_frome=aipt)
- **Step 17, dependency on Step 16 (license):** No source requires the DHSR license before signing. HIEA's page asks only for entity and contact details.
- **Step 17, "HL7/FHIR" and "certified EHR":** HIEA asks only that the EHR can send HL7 version 2.0 or higher. ONC certification is preferred, not required. FHIR is for health plan data access.[hiea.nc.gov](https://hiea.nc.gov/providers/how-connect/nc-healthconnex-participation-agreement?share_frome=aipt)
- **Step 17, "approved HIEA extension":** The hardship extension in G.S. 90-414.4(a3) cannot extend beyond the statutory deadline of January 1, 2023 ([NC HIEA](https://hiea.nc.gov/providers/what-does-law-mandate)).
- **Step 17, "proof of connection before billing":** No source found requires this. See Open Questions.
- **Step 17, Part 2 records:** Records subject to 42 CFR Part 2 are exempt from submission under G.S. 90-414.4(c) ([NC HIEA](https://hiea.nc.gov/providers/what-does-law-mandate)). SAIOP and SACOT may hold such records.
- **Step 18, "$709 federal application fee":** The 2026 federal fee is $750. The $100 NC fee is correct.[nctracks.nc.gov](https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-Behavioral-Health-Provider-Enrollment.html?share_frome=aipt)[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/provider-enrollment-2026-summer-and-fall-series-1-powerpoint/open?share_frome=aipt)
- **Step 18, "assign taxonomy codes" (plural):** The matrix lists one taxonomy, 251S00000X, with each service selected under it ([Provider Permission Matrix](https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx)).
- **Step 18, "attach DHSR license":** The Sept 2025 guide lists no license upload. NCTracks verifies it, and the matrix flags it as source-verified.[nctracks.nc.gov](https://www.nctracks.nc.gov/content/dam/jcr:8d0d2b03-b987-41b2-855c-cb5d1ad4980f/PUGPRV593.pdf?share_frome=aipt)
- **Step 18, W-9 and banking documents:** The W-9 is an electronic attestation. EFT details are entered on an EFT Account Information page ([HSO guide](https://www.nctracks.nc.gov/content/dam/jcr:7d4728a7-9427-4ebb-9d21-3f1262cbf772/PUG_Human%20Service%20Organization%20Enrollment%20Participant%20User%20Guide.pdf)). No bank document upload was found.[per.nctracks.com](https://per.nctracks.com/content/public/providers/provider-enrollment/terms-and-conditions.html?share_frome=aipt)
- **Step 18, dependency on Step 17 (HIE):** The Sept 2025 Organization guide has no HIE step.
- **Step 18, additional requirements not in app context:**
  - The Office Administrator must be an owner or managing employee.[nctracks.nc.gov](https://www.nctracks.nc.gov/content/dam/jcr:8d0d2b03-b987-41b2-855c-cb5d1ad4980f/PUGPRV593.pdf?share_frome=aipt)
  - The matrix shows taxonomy 251S00000X as high risk with a site visit and fingerprinting.
  - New Provider Training is due within 15 calendar days.
  - Taxonomy 251S00000X needs a service selected, with an extended deadline of October 1, 2026.[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/provider-enrollment-2026-summer-and-fall-series-1-powerpoint/open?share_frome=aipt)

## OPEN QUESTIONS

- **Initial review process:** Ask MHLCS (919-855-3795) how findings on an initial licensure review are communicated and whether an SOD with a 10-day POC applies. Also ask whether an 8G-only site needs any DHSR review.
- **POC submission and timing:** Ask MHLCS whether POCs can be emailed. Also ask for the realistic wait for the on-site visit, since the 4-8 week figure is unverified.
- **HIE and billing:** Ask HIEA (919-754-6912) whether a new provider has a grace period to connect after it starts billing. Ask NC Medicaid and each Tailored Plan contracting desk whether proof of connection is required before billing.
- **Part 2 handling:** Ask HIEA whether a Part 2 program such as SAIOP or SACOT should sign the Full or Submission-only agreement. Also ask what test data, if any, to send for Part 2 filtering.
- **NCTracks EFT:** Ask the CSRA Call Center (800-688-6696) whether a voided check or bank letter is requested for organizations, and how long EFT pre-note verification takes.
- **NCTracks processing:** Ask the CSRA Call Center for current processing time, site-visit scheduling and fingerprinting steps for taxonomy 251S00000X. Also ask whether a federal fee waiver applies to your organization.
- **Tailored Plan requirements:** Ask Alliance, Trillium, Vaya and Partners credentialing desks which of these steps they require before network participation. Requirements may differ by LME/MCO.