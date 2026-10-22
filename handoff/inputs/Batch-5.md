> From: https://www.perplexity.ai/computer/tasks/b6dc2d42-c77f-40e7-83f7-b718ed23ca6d

# you asked

message time: 2026-10-18 20:13:36

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

---

# perplexity response

Ran grep -n -i -E "managing|owner|cost|fee|\\$|sheriff|LiveScan|Live Scan|results" output_9a8a099b92d34acd87ee2008fbab5e25.t …

---

# perplexity response

```json
{
  "step_19_sub_0": {
    "instructions": [
      "Check the Office Administrator email in NCTracks for the fingerprinting notice. NCTracks generates an Electronic Fingerprint Submission Release of Information form with a unique case number for each 5% or greater owner.",
      "Do not get fingerprinted before the notice arrives. Prints taken without the NCTracks-generated form and case number are not accepted.",
      "Download the 'Locations for Fingerprinting Services' list from the NCTracks Fingerprinting FAQ page. Book LiveScan at a listed sheriff's office or approved site, and bring a government photo ID plus the case-number form.",
      "Have the law enforcement official complete the Law Enforcement Agency Section of the form at the appointment. Pay the fee at the site; it varies by location.",
      "Finish before the deadline printed in your notice. Missing it results in denial or termination."
    ],
    "tips": [
      "AUDIT TRAP: Fingerprint results from other agencies cannot be reused. Only Medicare fingerprint results through PECOS are accepted, so a prior DHHS or DSS background check will not satisfy NCTracks.",
      "Results stay valid for five years for owners holding 5% or more. A risk-level bump-up forces earlier re-fingerprinting.",
      "Prefer LiveScan to ten-print cards. A card must be mailed to NC SBI with BOTH the Applicant Information form and the Release of Information form."
    ],
    "contacts": [
      "NCTracks Call Center: 1-800-688-6696 (https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-fingerprinting.html)"
    ],
    "sources": [
      "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-fingerprinting.html",
      "https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx",
      "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108C/GS_108C-3.html",
      "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-Behavioral-Health-Provider-Enrollment.html",
      "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-OPR-providers.html"
    ],
    "confidence": "medium",
    "verify": "The 30-day window is not stated in the Aug. 11, 2026 NCTracks fingerprinting FAQ; use the deadline printed in your notice. The $38 fee is NOT VERIFIED (the FAQ says cost varies by location); confirm with the site when booking. Confirm your risk level in the notice, because the Aug. 16, 2026 Provider Permission Matrix shows High risk for 251S00000X, but a different taxonomy or national accreditation may change it."
  },
  "step_19_sub_1": {
    "instructions": [
      "Log in to the NCTracks Secure Provider Portal as Office Administrator and open the Status and Management page.",
      "Under Submitted Applications, find the NPI with status In Review and click Upload Documents.",
      "Attach the signed Electronic Fingerprint Submission Release of Information form for each notified owner, then click Submit Now.",
      "If you used a ten-print card, also mail the card, the Applicant Information form and the Release form to the SBI Civilian Services Unit, 'DHHSDMA00', PO Box 29500, Raleigh NC 27626-0500.",
      "If a name is misspelled on the form, contact the NCTracks Call Center to withdraw the application and resubmit it so the form regenerates."
    ],
    "tips": [
      "AUDIT TRAP: Forms mailed to NCTracks or to the address on the form's Agency Section are not processed. Only the portal upload counts.",
      "The form is generated from what you typed in the enrollment application. Spelling, DOB or ownership-percentage errors mean you must withdraw and re-apply.",
      "Managing employees are not required to be fingerprinted, only providers and owners with 5% or greater direct or indirect ownership. List ownership correctly in the application, because an unlisted owner is a common cause of denial."
    ],
    "contacts": [
      "NCTracks Call Center: 1-800-688-6696 (https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-fingerprinting.html)"
    ],
    "sources": [
      "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-fingerprinting.html"
    ],
    "confidence": "high",
    "verify": "The FAQ lists the SBI mailing address as PO Box 29500. Another NCTracks page may list a Garner Road street address, so confirm the current address on the form itself before mailing. No 'Provider Screening Unit' name appears in the FAQ; the process runs through the portal upload."
  },
  "step_19_sub_2": {
    "instructions": [
      "Confirm your service location address in NCTracks exactly matches the building where services are delivered, and that the site is open and staffed during posted hours.",
      "Watch the Office Administrator email for the site visit notice. NC Medicaid uses Public Consulting Group (PCG) for pre-enrollment visits required by 42 CFR 455.432 for moderate and high risk taxonomies.",
      "Have the owner or clinical lead on site with the DHSR license, service descriptions, program schedule and staff list ready.",
      "Make sure the person who meets the visitor can explain the services you enrolled for (SAIOP, SACOT).",
      "If you are asked to reschedule or correct information, respond through the NCTracks Call Center promptly and keep the ticket number."
    ],
    "tips": [
      "AUDIT TRAP: If the person at the visit cannot show basic knowledge of the enrolled services, the visit is recorded as a fail, which leads to automatic termination of participation per NC Medicaid's March 2026 provider notice.",
      "Information on the NCTracks record must match what the visitor finds, including address, services and hours. Keep the record current through Manage Change Requests.",
      "Do not schedule the visit around an unfinished buildout. The program should be set up to operate."
    ],
    "contacts": [
      "NCTracks Call Center: 1-800-688-6696 (https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faq-general.html)"
    ],
    "sources": [
      "https://medicaid.ncdhhs.gov/blog/2026/03/04/providers-risks-not-accurately-reporting-your-nctracks-provider-record",
      "https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx",
      "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-fingerprinting.html",
      "https://www.nctracks.nc.gov/content/dam/jcr:b8628768-96d7-406d-8fa5-dd9cb7351ee2/837P%20Professional%20Health%20Care%20Claim.pdf"
    ],
    "confidence": "medium",
    "verify": "NOT VERIFIED: the visit checklist, notice lead time, and PCG scheduling contact number. Ask the NCTracks Call Center for the current PCG site visit contact and what documents the visitor will request."
  },
  "step_20_sub_0": {
    "instructions": [
      "Open the approval letter and the NCTracks Provider Record. Compare the enrollment effective date for each health plan, service location, taxonomy and service against your DHSR license effective date.",
      "Confirm the effective date is not earlier than the date of your required license, certification or accreditation on file.",
      "Check the date is no more than 365 days before the application and no more than 90 days after it.",
      "If the date is wrong, have the Office Administrator submit a Request to Back-Date Enrollment Effective Dates through Manage Change Request, in a single session.",
      "Do not bill or schedule Medicaid services before the date shown on the record."
    ],
    "tips": [
      "AUDIT TRAP: Services delivered before the effective date shown on the provider record are not billable. A back-date request cannot precede the license or accreditation begin date on file.",
      "The 2019 NCTracks notice limits approvals to system issues, emergencies or medically necessary services. Backdating is not routine, so set the requested date correctly at the start.",
      "Only the Office Administrator sees the back-date page, and it cannot be saved as a draft."
    ],
    "contacts": [
      "NCTracks Call Center: 1-800-688-6696 (https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faq-general.html)"
    ],
    "sources": [
      "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-providerenrollment.html",
      "https://www.nctracks.nc.gov/content/dam/jcr:89fd797c-32a7-41f8-8dd0-8e078d47152d/JA_PRV702%20Req%20Backdate%20Enroll%20Eff%20Dates_W1.0.1.pdf",
      "https://www.nctracks.nc.gov/content/public/providers/provider-communications/2019-announcements/Provider-Ability-to-Request-Approval-for-Backdated-Enrollment-Effective-Date.html"
    ],
    "confidence": "high",
    "verify": "The back-date job aid (PRV702, Nov. 2025) may allow a wider range of reasons than the 2019 notice. Confirm with the NCTracks Call Center before relying on backdating. Also confirm separately that each Tailored Plan honors the same effective date in its own contract."
  },
  "step_20_sub_1": {
    "instructions": [
      "Decide which clinicians need individual NCTracks records, such as an LCAS or other licensed professional who enrolled as an individual provider. Qualified Professionals and CCS-credentialed supervisors are not separate NCTracks provider types.",
      "Wait until your organization is approved. Newly enrolling organizations must be approved before individuals can affiliate.",
      "Have each individual provider's Office Administrator log in, open Status and Management, select the individual NPI under Manage Change Request and click Update.",
      "Select Add/Update Affiliations, enter your organization NPI, click Lookup NPI, tick the organization and location, then click Add.",
      "Submit the Manage Change Request and confirm the affiliation shows on the individual record."
    ],
    "tips": [
      "AUDIT TRAP: Your organization cannot create or change the affiliation. Only the Office Administrator of the individual's record can. The older Medicaid Bulletin says affiliation-related claims deny if not fixed within the stated period.",
      "Affiliation begin dates default to the current date and cannot be changed. Affiliate before the clinician delivers billable services.",
      "A clinician on another organization's record stays there until you become that record's Office Administrator. Alliance says it fills its claim system from daily NCTracks files, so errors here carry into the Tailored Plan network."
    ],
    "contacts": [
      "NCTracks Call Center: 1-800-688-6696 (https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faq-general.html)"
    ],
    "sources": [
      "https://www.nctracks.nc.gov/content/dam/jcr:478f30b7-5d05-4472-bc46-7ba53811d0de/JA%20-%20How%20to%20Affiliate%20an%20Individual%20Provider%20Record%20to%20a%20Group-Organization%20Provider%20Record%20in%20NCTracks%2020170531.pdf",
      "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-manage-change-requests.html",
      "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-providerenrollment.html",
      "https://medicaid.ncdhhs.gov/blog/2021/10/18/provider-reminders-individual-provider-affiliation-and-keeping-nctracks-records-current",
      "https://medicaid.ncdhhs.gov/documents/files/medicaid-bulletin-2017-06/open",
      "https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/"
    ],
    "confidence": "medium",
    "verify": "NOT VERIFIED: whether agency-based staff (QPs, peer support specialists, associate-level staff) must be enrolled and affiliated in NCTracks for 8G, 8A-12 or 8A-13 claims. Ask NC Medicaid Provider Enrollment and each Tailored Plan. Also check whether your plan requires the rendering NPI on the claim."
  },
  "step_20_sub_2": {
    "instructions": [
      "Decide how you will bill NCTracks (Medicaid Direct fee-for-service): direct 837P, a clearinghouse or a billing agent. If using an agent, add it to your NCTracks record through the billing agent option in Manage Change Request.",
      "If submitting 837P directly, sign the Trading Partner Agreement in the NCTracks portal and obtain your Transaction Supplier Number. Email NCMMIS_EDI_Support@gdit.com for the contact form and a Ramp Management invitation.",
      "Run test 837P files in Ramp Management using the Companion Guide, and fix errors until certified.",
      "Request the 835 electronic remittance through the same trading partner setup, then confirm the first production remittance arrives and reconciles to payments.",
      "Submit one low-dollar production claim and trace it through the 835."
    ],
    "tips": [
      "AUDIT TRAP: Medicaid Direct claims go to NCTracks, but Tailored Plan and Standard Plan claims go to the plan, not NCTracks. Test each plan's claim route separately.",
      "NC DHHS can require re-testing if a trading partner generates too many errors in production.",
      "Match the service location, taxonomy and NPI on the 837P to the NCTracks record. Mismatches are the usual cause of early denials."
    ],
    "contacts": [
      "NCTracks EDI Support: NCMMIS_EDI_Support@gdit.com (https://www.nctracks.nc.gov/content/public/providers/provider-trading-partners/faqs-for-trading-partners.html)",
      "NCTracks Call Center: 1-800-688-6696 (https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-edi.html)"
    ],
    "sources": [
      "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-edi.html",
      "https://www.nctracks.nc.gov/content/public/providers/provider-trading-partners/faqs-for-trading-partners.html",
      "https://www.nctracks.nc.gov/content/dam/jcr:775ac675-c2b9-48ce-9da0-42e045db9a88/JA%20-%20How%20to%20select%20a%20Billing%20Agent%20and%20Other%20Claims%20Submission%20Options%20in%20NCTracks%2020170531.pdf",
      "https://www.trilliumhealthresources.org/sites/default/files/docs/Provider-documents/Claims/Trillium-Unified-Claims-Platform-Questions-Answer.pdf"
    ],
    "confidence": "medium",
    "verify": "The trading partner FAQ says some trading partners need no certification testing while the EDI page says testing or third-party certification is required. Confirm with NCTracks EDI Support which path applies to a clearinghouse versus a direct submitter, and how a provider requests the 835 specifically."
  },
  "step_21_sub_0": {
    "instructions": [
      "Confirm NCTracks enrollment is active; Alliance, Trillium and Vaya Partners all require it before network contracting.",
      "Apply to each plan you want: Alliance Provider Application, Trillium request by email to NetworkServicesSupport@TrilliumNC.org, or Vaya Partners Provider Contract Request Form.",
      "Ask for the plan's current service-needs list before applying for Peer Support (8G), which is now a closed-network service.",
      "Sign the contract and keep the welcome letter, which gives orientation, claims and UM instructions.",
      "Also ask about Medicaid Direct and State-funded contract amendments, and about Standard Plan contracts if you want those members."
    ],
    "tips": [
      "Vaya Health and Partners combined as Vaya Partners on Oct. 1, 2026, so there are three Tailored Plan regions, not four. Use providers.vayapartners.org, not the legacy sites.",
      "Under Session Law 2026-41, NC Medicaid says plans may close their networks for Peer Support and RB-BHT services as of July 7, 2026. Alliance cites Senate Bill 257 effective July 2, 2026. A new peer-support provider may be turned away unless a need is posted.",
      "AUDIT TRAP: National accreditation is due within one year of NC Medicaid enrollment for 8G, 8A-12 and 8A-13 per the CCPs. Plans can terminate contracts for missing it."
    ],
    "contacts": [
      "Alliance Health Provider Support: 855-759-9700 (https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/)",
      "Trillium Provider Support Services: 1-855-250-1539 (https://www.trilliumhealthresources.org/contracting-information)",
      "Vaya Partners ACCESS Provider Services: 1-866-990-9712 (https://providers.vayapartners.org/enrollment/)"
    ],
    "sources": [
      "https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/",
      "https://www.trilliumhealthresources.org/contracting-information",
      "https://providers.vayapartners.org/enrollment/",
      "https://providers.vayahealth.com/wp-content/uploads/2026/09/Joint_VP_Merger_Info_Session_9-14-26.pdf",
      "https://medicaid.ncdhhs.gov/providers/provider-playbook-medicaid-managed-care/fact-sheets/mandatory-closed-networks",
      "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108D/GS_108D-23.html",
      "https://medicaid.ncdhhs.gov/8g-peer-support-services/open",
      "https://medicaid.ncdhhs.gov/media/15767/download?attachment",
      "https://medicaid.ncdhhs.gov/media/15769/download?attachment"
    ],
    "confidence": "medium",
    "verify": "NOT VERIFIED: Partners legacy region application path and current timelines after the Oct. 1, 2026 merger. NOT VERIFIED: the 6-12 week estimate; only Alliance states a 5 business day application decision. Confirm which county catchment each plan serves and whether Standard Plan contracts are required for your service mix. The PPM and CCP accreditation timing (1 year) differ from the PPM's note on SAIOP/SACOT; ask NC Medicaid which applies."
  },
  "step_21_sub_1": {
    "instructions": [
      "Ask each plan's enrollment team which clinician roster process applies after contract. Alliance says practitioners joining a contracted behavioral health entity need no extra submission because it loads daily NCTracks files.",
      "For Vaya Partners, submit an Enrollment Initiation Form (EIF) to add each new clinician to your agency contract.",
      "Make sure every rostered clinician is enrolled and affiliated in NCTracks first, then confirm the NPI, name and location match.",
      "Give plans your DHSR license, accreditation status and insurance certificates when asked.",
      "Record each plan's confirmation of the roster in your contracting file."
    ],
    "tips": [
      "NC Medicaid says LME/MCOs no longer perform credentialing; NCTracks does. None of the plan pages opened ask for CAQH IDs, so do not build the process around them without a written plan request.",
      "AUDIT TRAP: Alliance requires professional liability and general liability of at least $1,000,000 per occurrence and $3,000,000 aggregate, plus workers' compensation. Missing certificates stall contracts.",
      "Alliance requires 30 days' advance notice of site address changes, ownership or tax ID changes."
    ],
    "contacts": [
      "Vaya Partners Provider Enrollment Services Team: 1-855-432-9139 (https://providers.vayapartners.org/enrollment/)",
      "Alliance Health Provider Support: 855-759-9700 (https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/)"
    ],
    "sources": [
      "https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/",
      "https://providers.vayapartners.org/enrollment/",
      "https://www.trilliumhealthresources.org/contracting-information",
      "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-Behavioral-Health-Provider-Enrollment.html"
    ],
    "confidence": "medium",
    "verify": "NOT VERIFIED: whether any of the three plans requires CAQH IDs or a separate roster attestation form. Ask each plan's contract manager in writing. Trillium's roster process was not found on the page opened."
  },
  "step_21_sub_2": {
    "instructions": [
      "Alliance: use EDI Payer ID 23071, return the Trading Partner Agreement and Connectivity Form, and keep your first 837 file to 5 to 10 claims.",
      "Trillium: from Oct. 1, 2026 Tailored Plan claims use payor ID 43072 via Availity, Change Healthcare or SSI Group, direct SFTP, or the iTransact portal. Medicaid Direct and State-funded claims are unchanged.",
      "Vaya Partners: use payor ID 13010. Request a Trading Partner Agreement and EDI Enrollment Form at EDI@vayahealth.com, and use the ProviderCONNECT portal or SFTP.",
      "Send test 837s per plan, confirm acceptance reports, then confirm the first paid claim and remittance match."
    ],
    "tips": [
      "AUDIT TRAP: Alliance's billing-loop address, including zip+4, must exactly match the site address in NCTracks, or claims map to the wrong site and deny.",
      "Alliance 837 files are not processed if the EDI Certified box is not checked.",
      "Trillium and Vaya Partners both moved to unified claims systems on Oct. 1, 2026. Use their newest guides, not older Partners, Vaya or Trillium instructions."
    ],
    "contacts": [
      "Alliance Provider Helpdesk (ACS): (919) 651-8500 (https://www.alliancehealthplan.org/providers/network/alliance-claim-system-acs/)",
      "Trillium Provider Support Services: 1-855-250-1539 (https://www.trilliumhealthresources.org/contracting-information)",
      "Vaya Partners ACCESS Provider Services: 1-866-990-9712 (https://providers.vayapartners.org/enrollment/)"
    ],
    "sources": [
      "https://www.alliancehealthplan.org/document-library/Claims-and-Enrollment-Guide.pdf",
      "https://www.alliancehealthplan.org/providers/network/alliance-claim-system-acs/",
      "https://www.trilliumhealthresources.org/sites/default/files/docs/Provider-documents/Claims/Trillium-Unified-Claims-Platform-Questions-Answer.pdf",
      "https://providers.vayahealth.com/wp-content/uploads/2026/09/Joint_VP_Merger_Info_Session_9-14-26.pdf",
      "https://providers.vayahealth.com/wp-content/uploads/2025/02/Vaya_EDI_276_277_Companion_Guide_OOC_20250129.pdf",
      "https://providers.vayahealth.com/authorization-information/prior-authorization/"
    ],
    "confidence": "medium",
    "verify": "Alliance guide is dated for FY 2026-27 and Trillium's FAQ was revised Sept. 30, 2026; payer IDs and clearinghouse lists can change. The Vaya payor ID was seen in the Sept. 14, 2026 merger presentation and an older companion guide, not on a current claims page. Confirm with each plan's EDI team."
  },
  "step_21_sub_3": {
    "instructions": [
      "After contract, request portal access: Alliance Claim System (ACS) Provider Portal, Trillium iTransact and Provider Data Management System, or Vaya Partners ProviderCONNECT.",
      "Attend each plan's live training. Trillium requires System Administrator training for its unified claims system.",
      "Download each plan's authorization guidelines and look up SAIOP (H0015), SACOT (H2035) and Peer Support (H0038). Peer Support needs prior approval after the 24 unmanaged units.",
      "Practice a test authorization request with the plan's UM team and record the turnaround time."
    ],
    "tips": [
      "Vaya Partners says prior authorization and admission notification flexibilities run through Dec. 29, 2026 for services after Sept. 30, 2026. Confirm which services this covers; it does not apply to Peer Support units beyond the 8G limits.",
      "AUDIT TRAP: You may not bill units beyond those authorized by the plan. Vaya Partners states this directly.",
      "CCP 8G caps unmanaged Peer Support at 24 units once per episode of care, then 176 units per 60 days and no more than 88 per 30 days without extra review."
    ],
    "contacts": [
      "Alliance Provider Helpdesk (ACS): (919) 651-8500 (https://www.alliancehealthplan.org/providers/network/alliance-claim-system-acs/)",
      "Vaya Partners ACCESS Provider Services: 1-866-990-9712 (https://providers.vayapartners.org/authorization-guidelines/)"
    ],
    "sources": [
      "https://www.alliancehealthplan.org/providers/network/alliance-claim-system-acs/",
      "https://www.trilliumhealthresources.org/contracting-information",
      "https://providers.vayapartners.org/authorization-guidelines/",
      "https://providers.vayahealth.com/authorization-information/prior-authorization/",
      "https://providers.vayahealth.com/wp-content/uploads/2026/09/Joint_VP_Merger_Info_Session_9-14-26.pdf",
      "https://medicaid.ncdhhs.gov/8g-peer-support-services/open"
    ],
    "confidence": "medium",
    "verify": "NOT VERIFIED: which plan requires prior authorization or notification for SAIOP and SACOT after the Vaya Partners flexibility window ends. Check each plan's authorization lookup tool. Trillium's training schedule was not confirmed on a page opened."
  },
  "step_22_sub_0": {
    "instructions": [
      "Build the note template from the DHHS Record Management and Documentation Manual, July 2025 (effective July 8, 2025). Add fields for individual name, record number or Medicaid ID, full date, service name, contact type, place of service and purpose tied to plan goals.",
      "Add required fields for interventions, duration, effectiveness and response to goals, and electronic authentication with date stamp and credentials.",
      "Add CCP-specific fields: for 8G, start and end time for each PSS unit; for SAIOP and SACOT, hours attended each day.",
      "Make group notes require an individual effectiveness entry per person, and enforce documentation within the required timeframe, with late entries flagged.",
      "Write an EHR standard operating procedure and confirm NC Health Connex (NC HIEA) compliance."
    ],
    "tips": [
      "AUDIT TRAP: Duration billed must match the duration in the note. Late entries are billable only up to seven business days after the service date; after that the service is not billable.",
      "Group notes need a full note for every person; the intervention can match across members but effectiveness must be individual.",
      "Cursive font in a Word document is not a valid electronic signature. The EHR must record date-stamped authentication at the time the person signs."
    ],
    "contacts": [
      "NC DHHS Records Management and Documentation Manual: https://www.ncdhhs.gov/rmdmjuly-2025/download?attachment (use the plan's provider relations line for questions)"
    ],
    "sources": [
      "https://www.ncdhhs.gov/rmdmjuly-2025/download?attachment",
      "https://medicaid.ncdhhs.gov/8g-peer-support-services/open",
      "https://medicaid.ncdhhs.gov/media/15767/download?attachment",
      "https://medicaid.ncdhhs.gov/media/15769/download?attachment"
    ],
    "confidence": "medium",
    "verify": "The July 2025 manual lists about 10 core content items plus authentication and CCP-specific additions, and does not mention APSM 45-2 in the text reviewed. Confirm with your Tailored Plan whether it still audits against APSM 45-2 wording. The 8G start-and-end-time element comes from CCP 8G Section 5.5.1; confirm the exact wording of that section in your copy."
  },
  "step_22_sub_1": {
    "instructions": [
      "Create a claim-scrubber rule that checks for SAIOP (H0015) and SACOT (H2035) within the same episode of care for the same member, not just the same calendar day.",
      "Allow an exception only on the day of admission or discharge for the program the member is entering or leaving.",
      "Add a rule blocking SAIOP or SACOT billing in the same episode as individual, family or group SUD therapy, except on admission or discharge days.",
      "Block 8G Peer Support at the same time of day as SAIOP or SACOT, though PSS in the same episode is allowed.",
      "Test with sample claims and have the Billing Specialist sign off before go-live."
    ],
    "tips": [
      "AUDIT TRAP: The CCP rule is 'same episode of care', not 'same day'. A member can be in only one of SAIOP or SACOT during a treatment episode, apart from the admission or discharge day.",
      "SACOT is for beneficiaries 18 and older with a primary SUD diagnosis; add an age check.",
      "Document each transition between levels of care so the admission or discharge exception can be proven."
    ],
    "contacts": [
      "Alliance Health Provider Support: 855-759-9700 (https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/)"
    ],
    "sources": [
      "https://medicaid.ncdhhs.gov/media/15767/download?attachment",
      "https://medicaid.ncdhhs.gov/media/15769/download?attachment",
      "https://medicaid.ncdhhs.gov/8g-peer-support-services/open"
    ],
    "confidence": "high",
    "verify": "Plans may add edits beyond the CCP. Ask each Tailored Plan for its claim edit list. Also confirm how the policy defines an episode of care for your EHR's admission dates."
  },
  "step_22_sub_2": {
    "instructions": [
      "Set the Peer Support (H0038) billing unit as 15 minutes in the EHR charge master. H0038 HQ for group is also 15 minutes, but not telehealth or telephonic eligible.",
      "Build the unmanaged-unit rule: the first 24 units per beneficiary per episode of care need no prior approval; require authorization after that.",
      "Build an authorization rule capping billing at 176 units per 60-day authorization period and 88 units per 30-day period unless a higher approval is on file.",
      "Block overlap with SAIOP, SACOT, partial hospitalization, PSR, respite and ITS at the same time of day.",
      "Do not hard-code 20 units per day or 80 per week unless a Tailored Plan tells you in writing to."
    ],
    "tips": [
      "AUDIT TRAP: The 20-unit daily and 80-unit weekly limits do not appear in CCP 8G amended Sept. 1, 2026. Hard-coding unsourced caps can block payable services or hide real limits.",
      "The Sept. 1, 2026 revision of 8G added unmanaged units and prior approval, so older templates are outdated.",
      "Telehealth and telephonic delivery are limited by the policy; check the current 8G and Policy 1-H before enabling remote delivery."
    ],
    "contacts": [
      "Vaya Partners ACCESS Provider Services: 1-866-990-9712 (https://providers.vayapartners.org/authorization-guidelines/)"
    ],
    "sources": [
      "https://medicaid.ncdhhs.gov/8g-peer-support-services/open"
    ],
    "confidence": "medium",
    "verify": "NOT VERIFIED: any daily or weekly Peer Support limits in Tailored Plan authorization guidelines. Check each plan's Behavioral Health Prior Authorization Look-up Tool. I did not confirm whether 8G's telehealth limits changed in the Sept. 2026 revision."
  },
  "step_22_sub_3": {
    "instructions": [
      "Set SAIOP H0015 as one unit per day (an event) and require at least 3 hours of documented service that day before the claim can release.",
      "Set SACOT as H2035, one unit per hour, and require at least 4 hours of SACOT that day before any hours can be billed.",
      "Add scheduling checks: SAIOP at least 3 service days per week; SACOT at least 4 hours per day, 5 days per week, 20 hours per week.",
      "Reject claims where billed duration differs from the note.",
      "Test with sample days of 2.5, 3 and 4 hours."
    ],
    "tips": [
      "AUDIT TRAP: The SACOT code is H2035, not H2036. A wrong code will deny or be paid incorrectly.",
      "CCP 8A-12 says adolescents may be scheduled for 2 hours per SAIOP service day, but billing requires 3 hours. Do not bill adolescent days under 3 hours without plan confirmation.",
      "SACOT must operate at least 20 hours per week, with no more than two consecutive days without services."
    ],
    "contacts": [
      "Trillium Provider Support Services: 1-855-250-1539 (https://www.trilliumhealthresources.org/contracting-information)"
    ],
    "sources": [
      "https://medicaid.ncdhhs.gov/media/15767/download?attachment",
      "https://medicaid.ncdhhs.gov/media/15769/download?attachment"
    ],
    "confidence": "high",
    "verify": "Confirm with each Tailored Plan how it treats an adolescent SAIOP day of 2 hours, since the CCP's scheduling minimum and billing minimum differ. Confirm the SAIOP weekly service-day rule in your copy of 8A-12."
  }
}
```

## SOURCES

| Title | Publisher | URL | Date or version | Type |
|---|---|---|---|---|
| Fingerprinting FAQs | NCTracks | [https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-fingerprinting.html](https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-fingerprinting.html) | Updated Aug. 11, 2026 | Primary |
| Provider Permission Matrix | NCTracks | [https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx](https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx) | Aug. 16, 2026 | Primary |
| State and Federal Fee Amounts by Year | NCTracks | [https://www.nctracks.nc.gov/content/dam/jcr:5088259c-ab17-4c01-bf6d-c64786be1da4/State%20and%20Federal%20Fee%20Amounts%20by%20Year.xlsx](https://www.nctracks.nc.gov/content/dam/jcr:5088259c-ab17-4c01-bf6d-c64786be1da4/State%20and%20Federal%20Fee%20Amounts%20by%20Year.xlsx) | 2026 row | Primary |
| G.S. 108C-3 | NC General Assembly | [https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108C/GS_108C-3.html](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108C/GS_108C-3.html) | Current | Primary |
| G.S. 108D-23 | NC General Assembly | [https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108D/GS_108D-23.html](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108D/GS_108D-23.html) | Amended by S.L. 2026-1 | Primary |
| Behavioral Health Provider Enrollment FAQs | NCTracks | [https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-Behavioral-Health-Provider-Enrollment.html](https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-Behavioral-Health-Provider-Enrollment.html) | Oct. 2026 | Primary |
| General Provider Enrollment FAQs | NCTracks | [https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-providerenrollment.html](https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-providerenrollment.html) | Oct. 2026 | Primary |
| OPR Provider FAQs | NCTracks | [https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-OPR-providers.html](https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-OPR-providers.html) | Current | Primary |
| Manage Change Request FAQs | NCTracks | https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-manage-change-requests.html[nctracks.nc.gov](https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-manage-change-requests.html?share_frome=aipt) | Oct. 2026 | Primary |
| Request to Back-Date Enrollment Effective Dates job aid (PRV702) | NCTracks | https://www.nctracks.nc.gov/content/dam/jcr:89fd797c-32a7-41f8-8dd0-8e078d47152d/JA_PRV702%20Req%20Backdate%20Enroll%20Eff%20Dates_W1.0.1.pdf[nctracks.nc.gov](https://www.nctracks.nc.gov/content/dam/jcr:89fd797c-32a7-41f8-8dd0-8e078d47152d/JA_PRV702%20Req%20Backdate%20Enroll%20Eff%20Dates_W1.0.1.pdf?share_frome=aipt) | Nov. 2025 | Primary |
| Backdated Enrollment Effective Date announcement | NCTracks | https://www.nctracks.nc.gov/content/public/providers/provider-communications/2019-announcements/Provider-Ability-to-Request-Approval-for-Backdated-Enrollment-Effective-Date.html[nctracks.nc.gov](https://www.nctracks.nc.gov/content/public/providers/provider-communications/2019-announcements/Provider-Ability-to-Request-Approval-for-Backdated-Enrollment-Effective-Date.html?share_frome=aipt) | Apr. 28, 2019 | Primary (older) |
| Affiliate an Individual Provider Record job aid | NCTracks | https://www.nctracks.nc.gov/content/dam/jcr:478f30b7-5d05-4472-bc46-7ba53811d0de/JA%20-%20How%20to%20Affiliate%20an%20Individual%20Provider%20Record%20to%20a%20Group-Organization%20Provider%20Record%20in%20NCTracks%2020170531.pdf[nctracks.nc.gov](https://www.nctracks.nc.gov/content/dam/jcr:478f30b7-5d05-4472-bc46-7ba53811d0de/JA%20-%20How%20to%20Affiliate%20an%20Individual%20Provider%20Record%20to%20a%20Group-Organization%20Provider%20Record%20in%20NCTracks%2020170531.pdf?share_frome=aipt) | 2017 version | Primary |
| Individual Provider Affiliation reminders | NC Medicaid | [https://medicaid.ncdhhs.gov/blog/2021/10/18/provider-reminders-individual-provider-affiliation-and-keeping-nctracks-records-current](https://medicaid.ncdhhs.gov/blog/2021/10/18/provider-reminders-individual-provider-affiliation-and-keeping-nctracks-records-current) | Oct. 18, 2021 | Primary |
| Medicaid Bulletin June 2017 | NC Medicaid | [https://medicaid.ncdhhs.gov/documents/files/medicaid-bulletin-2017-06/open](https://medicaid.ncdhhs.gov/documents/files/medicaid-bulletin-2017-06/open) | June 2017 | Primary (older) |
| Risks of not accurately reporting NCTracks record | NC Medicaid | [https://medicaid.ncdhhs.gov/blog/2026/03/04/providers-risks-not-accurately-reporting-your-nctracks-provider-record](https://medicaid.ncdhhs.gov/blog/2026/03/04/providers-risks-not-accurately-reporting-your-nctracks-provider-record) | Mar. 4, 2026 | Primary |
| EDI FAQs | NCTracks | https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-edi.html[nctracks.nc.gov](https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-edi.html?share_frome=aipt) | Current | Primary |
| FAQs re: Trading Partners | NCTracks | https://www.nctracks.nc.gov/content/public/providers/provider-trading-partners/faqs-for-trading-partners.html[nctracks.nc.gov](https://www.nctracks.nc.gov/content/public/providers/provider-trading-partners/faqs-for-trading-partners.html?share_frome=aipt) | Current | Primary |
| Billing Agent job aid | NCTracks | https://www.nctracks.nc.gov/content/dam/jcr:775ac675-c2b9-48ce-9da0-42e045db9a88/JA%20-%20How%20to%20select%20a%20Billing%20Agent%20and%20Other%20Claims%20Submission%20Options%20in%20NCTracks%2020170531.pdf[nctracks.nc.gov](https://www.nctracks.nc.gov/content/dam/jcr:775ac675-c2b9-48ce-9da0-42e045db9a88/JA%20-%20How%20to%20select%20a%20Billing%20Agent%20and%20Other%20Claims%20Submission%20Options%20in%20NCTracks%2020170531.pdf?share_frome=aipt) | 2017 version | Primary |
| General FAQs | NCTracks | [https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faq-general.html](https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faq-general.html) | Oct. 2026 | Primary |
| 837P Professional Health Care Claim guide | NCTracks | [https://www.nctracks.nc.gov/content/dam/jcr:b8628768-96d7-406d-8fa5-dd9cb7351ee2/837P%20Professional%20Health%20Care%20Claim.pdf](https://www.nctracks.nc.gov/content/dam/jcr:b8628768-96d7-406d-8fa5-dd9cb7351ee2/837P%20Professional%20Health%20Care%20Claim.pdf) | Current | Primary |
| CCP 8A-12 SAIOP | NC Medicaid | [https://medicaid.ncdhhs.gov/media/15767/download?attachment](https://medicaid.ncdhhs.gov/media/15767/download?attachment) | Amended Jan. 1, 2026 | Primary |
| CCP 8A-13 SACOT | NC Medicaid | [https://medicaid.ncdhhs.gov/media/15769/download?attachment](https://medicaid.ncdhhs.gov/media/15769/download?attachment) | Amended Jan. 1, 2026 | Primary |
| CCP 8G Peer Support Services | NC Medicaid | [https://medicaid.ncdhhs.gov/8g-peer-support-services/open](https://medicaid.ncdhhs.gov/8g-peer-support-services/open) | Amended Sept. 1, 2026 | Primary |
| Record Management and Documentation Manual | NC DHHS | [https://www.ncdhhs.gov/rmdmjuly-2025/download?attachment](https://www.ncdhhs.gov/rmdmjuly-2025/download?attachment) | Effective July 8, 2025 | Primary |
| Mandatory Closed Networks fact sheet | NC Medicaid | [https://medicaid.ncdhhs.gov/providers/provider-playbook-medicaid-managed-care/fact-sheets/mandatory-closed-networks](https://medicaid.ncdhhs.gov/providers/provider-playbook-medicaid-managed-care/fact-sheets/mandatory-closed-networks) | Modified Oct. 1, 2026 | Primary |
| Alliance Provider Enrollment | Alliance Health | [https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/](https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/) | Oct. 2026 | Primary (plan) |
| Alliance Claims and Enrollment Guide FY 2026-27 | Alliance Health | https://www.alliancehealthplan.org/document-library/Claims-and-Enrollment-Guide.pdf[alliancehealthplan.org](https://www.alliancehealthplan.org/document-library/Claims-and-Enrollment-Guide.pdf?share_frome=aipt) | July 2026 | Primary (plan) |
| Alliance Claim System (ACS) | Alliance Health | https://www.alliancehealthplan.org/providers/network/alliance-claim-system-acs/[alliancehealthplan.org](https://www.alliancehealthplan.org/providers/network/alliance-claim-system-acs/?share_frome=aipt) | Oct. 13, 2026 | Primary (plan) |
| Trillium Contracting Information | Trillium Health Resources | [https://www.trilliumhealthresources.org/contracting-information](https://www.trilliumhealthresources.org/contracting-information) | Verified Oct. 8, 2026 | Primary (plan) |
| Trillium Unified Claims System FAQ | Trillium Health Resources | https://www.trilliumhealthresources.org/sites/default/files/docs/Provider-documents/Claims/Trillium-Unified-Claims-Platform-Questions-Answer.pdf[trilliumhealthresources.org](https://www.trilliumhealthresources.org/sites/default/files/docs/Provider-documents/Claims/Trillium-Unified-Claims-Platform-Questions-Answer.pdf?share_frome=aipt) | Revised Sept. 30, 2026 | Primary (plan) |
| Vaya Partners Provider Enrollment | Vaya Partners | [https://providers.vayapartners.org/enrollment/](https://providers.vayapartners.org/enrollment/) | Oct. 2026 | Primary (plan) |
| Vaya Partners Authorization Guidelines | Vaya Partners | https://providers.vayapartners.org/authorization-guidelines/[providers.vayapartners.org](https://providers.vayapartners.org/authorization-guidelines/?share_frome=aipt) | Oct. 14, 2026 | Primary (plan) |
| Joint Vaya Partners merger info session | Vaya Health / Partners | https://providers.vayahealth.com/wp-content/uploads/2026/09/Joint_VP_Merger_Info_Session_9-14-26.pdf[providers.vayahealth.com](https://providers.vayahealth.com/wp-content/uploads/2026/09/Joint_VP_Merger_Info_Session_9-14-26.pdf?share_frome=aipt) | Sept. 14, 2026 | Primary (plan) |
| Vaya Prior Authorization page | Vaya Partners | [https://providers.vayahealth.com/authorization-information/prior-authorization/](https://providers.vayahealth.com/authorization-information/prior-authorization/) | Oct. 16, 2026 | Primary (plan) |
| Vaya EDI Companion Guide | Vaya Health | https://providers.vayahealth.com/wp-content/uploads/2025/02/Vaya_EDI_276_277_Companion_Guide_OOC_20250129.pdf[providers.vayahealth.com](https://providers.vayahealth.com/wp-content/uploads/2025/02/Vaya_EDI_276_277_Companion_Guide_OOC_20250129.pdf?share_frome=aipt) | Jan. 29, 2025 | Primary (older) |

## CORRECTIONS

- **Managing employees and fingerprinting (Step 19).** The app says 5%+ owners and managing employees must be fingerprinted. NCTracks says fingerprint checks apply to high-risk providers and owners with 5% or greater direct or indirect ownership, and states managing employees are not required to be fingerprinted ([NCTracks fingerprinting FAQ](https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-fingerprinting.html)). The statute still lets NC Medicaid raise risk based on a managing employee's history ([G.S. 108C-3](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108C/GS_108C-3.html)).
- **$38 fingerprint cost.** NOT VERIFIED. The FAQ says the person notified pays, and the cost varies by location.
- **"Fingerprint Verification Forms" to a "Provider Screening Unit."** The actual document is the NCTracks-generated Electronic Fingerprint Submission Release of Information form. It is uploaded to the application under Upload Documents; mailed forms are not processed.
- **"30-day notice window."** Not stated in the current FAQ. The deadline is the one in your notice.
- **Step 19 scope.** The app lists only 8A-12 and 8A-13. The Aug. 16, 2026 Provider Permission Matrix shows Peer Support Services (8G), SAIOP and SACOT all as High risk under taxonomy 251S00000X, with site visit, application fee and fingerprinting required ([Provider Permission Matrix](https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx)). So Step 19 also applies to 8G.
- **Missing fees.** High-risk enrollment carries a 2026 federal application fee of $750 plus the $100 NC fee ([NCTracks fee table](https://www.nctracks.nc.gov/content/dam/jcr:5088259c-ab17-4c01-bf6d-c64786be1da4/State%20and%20Federal%20Fee%20Amounts%20by%20Year.xlsx)). The app's $0 cost for Step 20 and $38 for Step 19 do not reflect these.
- **Step 20 affiliations.** The Manage Change Request must be initiated by the Office Administrator of the individual provider's record, not by the organization ([Medicaid Bulletin June 2017](https://medicaid.ncdhhs.gov/documents/files/medicaid-bulletin-2017-06/open)). CCS and QP are not NCTracks provider types; LCAS may be, if enrolled individually.
- **Step 21 plan list.** The app names Alliance, Partners, Trillium and Vaya. Vaya Health and Partners combined as Vaya Partners on Oct. 1, 2026 ([Vaya Partners enrollment page](https://providers.vayapartners.org/enrollment/); joint merger session).[providers.vayahealth.com](https://providers.vayahealth.com/wp-content/uploads/2026/09/Joint_VP_Merger_Info_Session_9-14-26.pdf?share_frome=aipt)
- **Step 21 main resource.** There is no single "Regional LME/MCO Contracting Portal." Each plan has its own enrollment page and process.
- **Peer Support network access.** Under Session Law 2026-41, NC Medicaid says plans must maintain closed networks for Peer Support Services and may exclude providers, effective July 7, 2026 ([NC Medicaid fact sheet](https://medicaid.ncdhhs.gov/providers/provider-playbook-medicaid-managed-care/fact-sheets/mandatory-closed-networks)). G.S. 108D-23(b) was repealed by Session Law 2026-1 ([G.S. 108D-23](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108D/GS_108D-23.html)). Alliance cites Senate Bill 257 effective July 2, 2026, which differs from NC Medicaid's July 7 date; NC Medicaid is the more authoritative source.
- **CAQH IDs.** None of the plan pages opened ask for CAQH, and NC Medicaid says LME/MCOs no longer perform credentialing ([NCTracks BH enrollment FAQ](https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-Behavioral-Health-Provider-Enrollment.html)). Treat CAQH as NOT VERIFIED and unrequired until a plan requests it.
- **APSM 45-2 and "10 elements" (Step 22).** The current rulebook is the NC DHHS Record Management and Documentation Manual, effective July 8, 2025 ([RM&DM](https://www.ncdhhs.gov/rmdmjuly-2025/download?attachment)). It lists about ten content elements plus electronic authentication and CCP-specific additions, and I found no mention of APSM 45-2 in the text reviewed. CCP 8G also adds start and end times.
- **SACOT code.** The app says H2036. CCP 8A-13 lists H2035, one unit equal to one hour, with a 4-hour daily minimum to bill ([CCP 8A-13](https://medicaid.ncdhhs.gov/media/15769/download?attachment)).
- **SAIOP billing.** H0015 is one unit per day as an event, with a 3-hour minimum ([CCP 8A-12](https://medicaid.ncdhhs.gov/media/15767/download?attachment)). The policy's 2-hour adolescent figure is a scheduling minimum, not a billing minimum.
- **"Same-day" exclusion.** Both CCPs bar SAIOP and SACOT in the same episode of care, not just the same day, except on the day of admission or discharge. They also bar billing with individual, family or group SUD therapy in that episode.
- **Peer Support limits.** CCP 8G (amended Sept. 1, 2026) has no 20-unit daily or 80-unit weekly cap. It has 24 unmanaged units per episode, then 176 units per 60 days and no more than 88 per 30 days without additional review. H0038 is a 15-minute unit ([CCP 8G](https://medicaid.ncdhhs.gov/8g-peer-support-services/open)).
- **EHR cost and resource.** The $150 to $400 per clinician per month figure and the healthit.gov link are NOT VERIFIED. Healthit.gov is a federal information site, not a behavioral health EHR vendor directory.

## OPEN QUESTIONS

- **Taxonomy and risk level.** Confirm your NCTracks taxonomy and whether national accreditation or another factor changes your risk level at revalidation. Ask the NCTracks Call Center at 1-800-688-6696.
- **Site visit details.** The site visit checklist, notice lead time and PCG contact number were not found. Ask the NCTracks Call Center.
- **Individual enrollment of agency staff.** Whether QPs, peer support specialists and other agency-based staff must be enrolled and affiliated in NCTracks for 8G, 8A-12 or 8A-13 claims. Ask NC Medicaid Provider Enrollment and each Tailored Plan.
- **EDI path.** Whether you need Ramp Management certification testing or can use a clearinghouse with no testing for NCTracks 835 delivery. Ask NCMMIS_EDI_Support@gdit.com.
- **Standard Plan contracts.** Whether you must also contract with the Standard Plans for SAIOP, SACOT or Peer Support. Check the Health Plan Contacts and Resources page on NC Medicaid.
- **Tailored Plan authorization rules.** Which services need prior authorization at each plan after the Vaya Partners flexibility window ends Dec. 29, 2026, and whether any plan sets daily or weekly Peer Support caps. Ask each plan's UM team.
- **Accreditation timing.** The CCPs say national accreditation is due within one year of NC Medicaid enrollment, but NC Medicaid's Behavioral Health page says the deadline is one or three years depending on the policy, and the Permission Matrix has its own accreditation entries. Ask NC Medicaid Behavioral Health which applies to each of your three services.
- **Vaya Partners legacy-region steps.** Application and roster steps for Partners-region counties after the Oct. 1, 2026 merger. Call 1-866-990-9712.