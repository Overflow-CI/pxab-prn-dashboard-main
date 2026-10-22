> From: https://www.perplexity.ai/computer/tasks/56331496-c3ef-47ca-9327-43154a562b30

# you asked

message time: 2026-10-18 21:53:00

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

---

# perplexity response

A)
```json
{
  "step_29_sub_0": {
    "instructions": [
      "Revise intake so staff verify Medicaid eligibility and health plan assignment in the NCTracks Provider Portal (Eligibility > Inquiry) or AVRS at 1-800-723-4337 before the first SAIOP, SACOT or peer support service.",
      "Re-check eligibility at every authorization request and at least monthly, because most adults 19 to 64 move to 6-month recertifications starting January 1, 2027.",
      "Write a pending-application rule: for applications made on or after January 1, 2027, retroactive coverage reaches back 1 month for expansion adults and 2 months for children, adults 65+ and people with disabilities.",
      "Send uninsured clients who may be eligible to the local DSS the same day, and record the application date, so services you deliver fall inside the shorter retroactive window.",
      "Add a retro-eligibility claims workflow: contact the new plan when eligibility moves to managed care, and rebill NC Medicaid Direct within 180 days of any plan recoupment."
    ],
    "tips": [
      "AUDIT TRAP: Applications filed by December 31, 2026 still get up to 3 months of retroactive coverage. Do not apply the 1-month rule to those clients, and do not write off claims for those months.",
      "AUDIT TRAP: Under 10A NCAC 22J .0106, once you accept someone as a Medicaid patient you cannot bill them for covered services. Decide private-pay status in writing before the service is delivered.",
      "SL 2026-1 Section 3C.5 adds G.S. 108A-55.7, which requires applicants to prove community engagement for the 3 months before they apply. Clients with a substance use disorder may need clinical documentation from you. Watch NC Medicaid's draft medical frailty policy."
    ],
    "contacts": [
      "NCTracks Call Center: 800-688-6696 (https://www.nctracks.nc.gov)",
      "NCTracks AVRS eligibility line: 1-800-723-4337 (https://www.nctracks.nc.gov/content/public/providers/faq-main-page/nctracks-glossary-of-terms.html)",
      "NC Medicaid Contact Center: 888-245-0179 (https://medicaid.ncdhhs.gov)"
    ],
    "sources": [
      "https://www.medicaid.gov/federal-policy-guidance/downloads/cib11182025.pdf",
      "https://medicaid.ncdhhs.gov/beneficiaries/medicaid-is-changing",
      "https://medicaid.ncdhhs.gov/dcdl-re-hr-1-beneficiary-mailings/open",
      "https://medicaid.ncdhhs.gov/provider-quick-reference-guide-tailored-plans/open",
      "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/nctracks-glossary-of-terms.html",
      "https://medicaid.ncdhhs.gov/blog/2026/08/10/claim-submission-process-when-eligibility-retroactively-updated",
      "https://medicaid.ncdhhs.gov/providers-billing-beneficiaries/open",
      "https://www.ncleg.gov/EnactedLegislation/SessionLaws/HTML/2025-2026/SL2026-1.html",
      "https://medicaid.ncdhhs.gov/providers/federal-medicaid-changes-what-providers-need-know"
    ],
    "confidence": "high",
    "verify": "Statute: H.R. 1 Sec. 71112 (July 4, 2025). CMS guidance: CMCS Informational Bulletin of November 18, 2025. NC has announced the change on its Medicaid is Changing page and in the June 18, 2026 DCDL letter. Confirm with each Tailored Plan how it handles claims for retroactive months, which may sit in NC Medicaid Direct. The effective date of G.S. 108A-55.7 (SL 2026-1 Section 3C.5) is NOT VERIFIED; check the session law text.",
    "basis": "expected",
    "effective_date": "2027-01-01 (applications made on or after this date)"
  },
  "step_29_sub_1": {
    "instructions": [
      "Write a financial responsibility policy covering clients who lose Medicaid, including noncitizens who lost full coverage on October 1, 2026, and people who are denied or not yet approved.",
      "Before scheduling a self-pay or uninsured client, give a written No Surprises Act Good Faith Estimate of expected charges, and ask every client about their insurance status.",
      "Use a signed private-pay acknowledgment, completed before the service, that meets 10A NCAC 22J .0106(a) and (c)(2). Never use it for a Medicaid-covered service once you have accepted the client as a Medicaid patient.",
      "Ask each LME/MCO whether uninsured clients can get state-funded SAIOP, SACOT or peer support, and what fee or sliding-scale rules the LME/MCO contract sets.",
      "Adopt a board-approved sliding-fee schedule tied to the current federal poverty guidelines, and post client notices in English and Spanish at the front desk."
    ],
    "tips": [
      "AUDIT TRAP: If a client turns out to be retroactively eligible, 10A NCAC 22J .0106(f) lets you file with Medicaid, but you must refund what the client paid. Track self-pay receipts by date of service.",
      "AUDIT TRAP: CMS FAQs say Good Faith Estimates apply to all provider types and must be given in writing. Keep a copy in each self-pay record, because a missing estimate opens the door to patient-provider dispute claims.",
      "Noncitizens limited to emergency Medicaid are removed from health plans under G.S. 108D-40, effective October 1, 2026. Emergency Medicaid does not cover routine SAIOP, SACOT or peer support."
    ],
    "contacts": [
      "NC Medicaid Contact Center: 888-245-0179 (https://medicaid.ncdhhs.gov)",
      "Alliance Health Provider Support: 855-759-9700 (https://www.alliancehealthplan.org/providers/)",
      "Vaya Partners ACCESS Provider Services: 1-866-990-9712 (https://providers.vayahealth.com/contact/)"
    ],
    "sources": [
      "https://medicaid.ncdhhs.gov/providers-billing-beneficiaries/open",
      "https://www.cms.gov/cciio/resources/regulations-and-guidance/downloads/guidance-good-faith-estimates-faq.pdf",
      "https://www.cms.gov/newsroom/fact-sheets/requirements-related-surprise-billing-part-ii-interim-final-rule-comment-period",
      "https://medicaid.ncdhhs.gov/about-nc-medicaid/eligibility/immigration-status-and-eligibility-nc-medicaid",
      "https://ncleg.gov/EnactedLegislation/Statutes/HTML/ByArticle/Chapter_108D/Article_4.html",
      "https://policies.ncdhhs.gov/wp-content/uploads/MA-2504-Final.pdf"
    ],
    "confidence": "medium",
    "verify": "The Good Faith Estimate and 10A NCAC 22J .0106 are current duties. A sliding fee is good practice unless your LME/MCO state-funded contract requires one. NOT VERIFIED: whether DMH/DD/SUS or LME/MCO contracts require a sliding-fee schedule for state-funded SAIOP, SACOT or peer support. Check with each LME/MCO's contracting staff. Have a healthcare attorney review the client notices.",
    "basis": "required",
    "effective_date": "2026-10-01 (noncitizen coverage loss); Good Faith Estimate in effect since 2022-01-01"
  },
  "step_29_sub_2": {
    "instructions": [
      "Note that H.R. 1 Sec. 71120 cost sharing for expansion adults above 100 percent of the poverty line starts October 1, 2028, and exempts mental health and substance use disorder services.",
      "Confirm that NC Medicaid's managed care billing guidance currently treats behavioral health claims as exempt from copayments.",
      "Email Alliance Health, Trillium Health Resources and Vaya Partners. Ask whether any copayment will apply to peer support, SAIOP or SACOT codes, citing new G.S. 108A-58.3 (effective July 1, 2027), and request written answers.",
      "Write a front-desk script that says no copay is collected for these services, unless a plan confirms otherwise in writing."
    ],
    "tips": [
      "AUDIT TRAP: Collecting a copay that is not allowed is billing a Medicaid member for a covered service, which 10A NCAC 22J .0106 prohibits. Refund it right away and document the refund.",
      "SL 2026-1 Section 3C.16 directs DHHS to set all Medicaid copays at the federal maximum starting July 1, 2027. Watch Medicaid Bulletins for any change to the behavioral health exemption.",
      "There are now 3 Tailored Plans. Vaya Health and Partners Health Management merged into Vaya Partners on October 1, 2026."
    ],
    "contacts": [
      "Alliance Health Provider Support: 855-759-9700 (https://www.alliancehealthplan.org/providers/)",
      "Trillium Health Resources Provider Support Services: 1-855-250-1539 (https://www.trilliumhealthresources.org/NCRootsHub)",
      "Vaya Partners ACCESS Provider Services: 1-866-990-9712 (https://providers.vayahealth.com/contact/)"
    ],
    "sources": [
      "https://www.congress.gov/bill/119th-congress/house-bill/1",
      "https://www.medicaid.gov/federal-policy-guidance/downloads/cib11182025.pdf",
      "https://medicaid.ncdhhs.gov/health-plan-billing-guide-version-32/open",
      "https://www.ncleg.gov/EnactedLegislation/SessionLaws/HTML/2025-2026/SL2026-1.html",
      "https://medicaid.ncdhhs.gov/providers-billing-beneficiaries/open",
      "https://medicaid.ncdhhs.gov/information-regarding-vaya-health-and-partners-health-management-merger/download?attachment"
    ],
    "confidence": "high",
    "verify": "Mostly not a provider obligation. Statute (Sec. 71120) and CMS (November 18, 2025 bulletin) exempt behavioral health and SUD services from the new cost sharing, and NC's billing guide exempts behavioral health claims from copays. Suggested rewording: Confirm in writing that peer support, SAIOP and SACOT remain copay-exempt, and set a front-desk no-copay script.",
    "basis": "recommended",
    "effective_date": "2028-10-01 (federal cost sharing start; MH/SUD exempt); 2027-07-01 (G.S. 108A-58.3)"
  },
  "step_29_sub_3": {
    "instructions": [
      "Map the eligibility responses from NCTracks or the 270/271 transaction into your billing system, and add a hard stop when a client shows emergency-services-only coverage, no coverage, or an end date.",
      "Flag noncitizen clients for review: since October 1, 2026, only citizens, green card holders, Cuban/Haitian entrants, COFA migrants, lawfully residing children under 19 and pregnant or postpartum people keep full Medicaid.",
      "Add an edit for the 6-month recertification date of adults 19 to 64 starting January 1, 2027, so an expiring eligibility triggers an outreach task 30 days ahead.",
      "Send test claims for each payer (NC Medicaid Direct, Alliance, Trillium, Vaya Partners) for every planned code, and confirm the remittance results before you launch."
    ],
    "tips": [
      "AUDIT TRAP: Under G.S. 108D-40 (effective October 1, 2026), emergency-only noncitizens are not in Tailored Plans. Claims sent to a plan for these clients will deny and cannot be rebilled as SAIOP or SACOT.",
      "Vaya Partners began using payer ID 13010 and added claim validation checks on October 1, 2026. Update clearinghouse payer tables for former Partners clients.",
      "Keep eligibility screenshots or 271 responses in the record for each date of service. LME/MCO post-payment reviews ask for proof of eligibility."
    ],
    "contacts": [
      "NCTracks Call Center: 800-688-6696 (https://www.nctracks.nc.gov)",
      "Vaya Partners ACCESS Provider Services: 1-866-990-9712 (https://providers.vayahealth.com/contact/)",
      "NC Medicaid Claims TA: Medicaid.ClaimsTA@dhhs.nc.gov (https://medicaid.ncdhhs.gov/blog/2026/08/10/claim-submission-process-when-eligibility-retroactively-updated)"
    ],
    "sources": [
      "https://www.medicaid.gov/medicaid/downloads/State-Implementation-Tool-Sect-71109.pdf",
      "https://medicaid.ncdhhs.gov/about-nc-medicaid/eligibility/immigration-status-and-eligibility-nc-medicaid",
      "https://policies.ncdhhs.gov/wp-content/uploads/MA-2504-Final.pdf",
      "https://ncleg.gov/EnactedLegislation/Statutes/HTML/ByArticle/Chapter_108D/Article_4.html",
      "https://www.medicaid.gov/federal-policy-guidance/downloads/smd26001.pdf",
      "https://medicaid.ncdhhs.gov/0814specialbulletinrecipienteligibility/download?attachment",
      "https://providers.vayahealth.com/wp-content/uploads/2026/09/pcb-09-10-26-issue-17.pdf"
    ],
    "confidence": "medium",
    "verify": "Statute: Sec. 71109 (effective October 1, 2026) and Sec. 71107 (renewals on or after January 1, 2027). CMS: Sec. 71109 State Implementation Tool and SMD 26-001. NC: MA-2504 revised October 2, 2026 and SL 2026-1 Section 3C.4. NOT VERIFIED: the exact NCTracks benefit plan or aid category codes that mark emergency-only coverage. Ask the NCTracks Call Center or your clearinghouse for the current code list.",
    "basis": "expected",
    "effective_date": "2026-10-01"
  },
  "step_30_sub_0": {
    "instructions": [
      "Each month, screen every owner, managing employee, employee, contractor and rendering staff member against the OIG LEIE and the SAM.gov exclusions, as the NCDHHS Provider Administrative Participation Agreement requires.",
      "Also check the NC Medicaid State Excluded Provider List, which is updated monthly, and NPPES. Alliance Health's manual also lists the SSA Death Master File and OFAC.",
      "Save dated search results or vendor reports for each person, and screen new hires before their start date.",
      "If you find a match, stop the person from billable work, notify NCTracks by Managed Change Request within 30 days, and notify Alliance Health within 2 business days or Trillium within 5 business days."
    ],
    "tips": [
      "AUDIT TRAP: Payments for services ordered or furnished by an excluded person are overpayments, and OIG can impose civil money penalties on whoever hired them. Monthly screening matches OIG's monthly LEIE updates.",
      "Checking the Death Master File quarterly is a state duty under H.R. 1 Sec. 71105, starting January 1, 2028. It is not a new provider duty, so keep NPPES and NCTracks records current to avoid false matches.",
      "Search under name variants and former names, and use dates of birth to clear near-matches. Surveyors want to see how you resolved each possible match."
    ],
    "contacts": [
      "NCTracks Call Center: 800-688-6696 (https://www.nctracks.nc.gov)",
      "NC Medicaid Contact Center: 888-245-0179 (https://medicaid.ncdhhs.gov/providers/excluded-providers)",
      "Alliance Health Provider Support: 855-759-9700 (https://www.alliancehealthplan.org/providers/)"
    ],
    "sources": [
      "https://www.nctracks.nc.gov/content/public/providers/provider-enrollment/terms-and-conditions/admin-participation-rev.html",
      "https://oig.hhs.gov/exclusions/",
      "https://oig.hhs.gov/exclusions/special-advisory-bulletin-and-other-guidance/the-effect-of-exclusion-from-participation-in-federal-health-care-programs/",
      "https://sam.gov/content/exclusions",
      "https://medicaid.ncdhhs.gov/providers/excluded-providers",
      "https://www.alliancehealthplan.org/document-library/79431/",
      "https://www.trilliumhealthresources.org/sites/default/files/docs/Provider-documents/Provider-Manual/Trillium-Provider-Manual.pdf",
      "https://www.medicaid.gov/federal-policy-guidance/downloads/cib11182025.pdf",
      "https://www.cms.gov/sites/default/files/repo-new/24/Toolkit%20for%20Database%20Checks%2042%20CFR%20455%20436.pdf"
    ],
    "confidence": "high",
    "verify": "Monthly LEIE and SAM screening comes from the NCDHHS participation agreement and predates H.R. 1. NC Medicaid does not appear to require providers to check death records, but Alliance's manual lists the SSA DMF. Ask Alliance which DMF access method it accepts. Vaya Partners' screening and reporting rules are NOT VERIFIED; check its provider manual.",
    "basis": "required",
    "effective_date": "In effect now; state quarterly provider DMF checks begin 2028-01-01"
  },
  "step_30_sub_1": {
    "instructions": [
      "Put the change-of-ownership deadline on the calendar: notify NCDHHS at least 30 days before the effective date with the Change of Ownership Disclosure Form, then submit 42 CFR 455.104 owner data within 35 days after.",
      "For changes to license, tax ID, NPI, bankruptcy, group membership, address, phone or email, submit an NCTracks Managed Change Request within 30 calendar days of the change.",
      "Report any adverse action against a required license, certification, accreditation or endorsement within 30 calendar days of learning about it, and upload supporting documents to the pending Managed Change Request.",
      "Run the NCTracks reverification report monthly. Complete reverification within 70 days of the invitation, and pay the $100 NC application fee by 5 p.m. on the due date.",
      "After each NCTracks change, update every Tailored Plan contract and directory record within that plan's required timeframe."
    ],
    "tips": [
      "AUDIT TRAP: NC Medicaid says that missing the 30-day deadline for disclosing an adverse action will terminate your NCTracks provider record.",
      "AUDIT TRAP: Errors in a reverification application cannot be corrected after you submit it. A rejected application after the suspension date automatically terminates your enrollment.",
      "Changes to a DHSR license, site address or service line usually require NCTracks and Tailored Plan updates too, so route all three through one change log."
    ],
    "contacts": [
      "NCTracks Call Center: 800-688-6696 (https://www.nctracks.nc.gov)",
      "NC Medicaid Provider Ombudsman: 866-304-7062 (https://medicaid.ncdhhs.gov/blog/2025/11/04/reminders-about-required-provider-disclosures)"
    ],
    "sources": [
      "https://www.nctracks.nc.gov/content/public/providers/provider-enrollment/terms-and-conditions/admin-participation-rev.html",
      "https://medicaid.ncdhhs.gov/blog/2025/11/04/reminders-about-required-provider-disclosures",
      "https://medicaid.ncdhhs.gov/blog/2026/04/16/quarterly-provider-update-spring-2026",
      "https://www.nctracks.nc.gov/content/public/providers/provider-recredentialing.html",
      "https://medicaid.ncdhhs.gov/providers/provider-data-management-credentialing-verification-organization"
    ],
    "confidence": "high",
    "verify": "This is not an H.R. 1 change. It rests on G.S. 108C-4, G.S. 108C-10 and the participation agreement. Taxonomy and managing-employee changes are not expressly listed in the agreement; treat them as 30-day changes and confirm with NCTracks (NOT VERIFIED). The PDM/CVO replacement is paused, so keep using NCTracks. Each Tailored Plan's update timeframe is NOT VERIFIED.",
    "basis": "required",
    "effective_date": "In effect now"
  },
  "step_30_sub_2": {
    "instructions": [
      "Build a 12-month cash-flow model by payer (Alliance, Trillium, Vaya Partners, Medicaid Direct, state-funded) and service (8G, 8A-12, 8A-13), with base, 10 percent and 20 percent decline scenarios.",
      "Model the volume risk from H.R. 1 enrollment rules: noncitizen coverage loss on October 1, 2026, and 6-month renewals plus work requirements for adults 19 to 64 starting January 1, 2027.",
      "Model rate risk using the October 1, 2025 NC precedent: a 3 percent cut to enhanced mental health fee schedules, reversed on December 10, 2025.",
      "Identify fixed costs, such as qualified professional and peer salaries and the lease, that you must cover in the 20 percent scenario, and list the actions and timing that would trigger staffing changes."
    ],
    "tips": [
      "H.R. 1's provider-tax and state-directed-payment limits mainly affect hospital payments in NC (HASP). NC has not announced any H.R. 1-based cut to SAIOP, SACOT or peer support rates.",
      "NC Medicaid says the FY2025-26 state funding shortfall was unresolved when its budget page was posted. Rate risk from state appropriations is more immediate than risk from federal financing limits.",
      "Have a CPA review the model, and keep it with your board minutes. LME/MCO network staff and lenders may ask for proof of financial viability."
    ],
    "contacts": [
      "NC Medicaid Contact Center: 888-245-0179 (https://medicaid.ncdhhs.gov)"
    ],
    "sources": [
      "https://www.medicaid.gov/federal-policy-guidance/downloads/cib11182025.pdf",
      "https://www.ncleg.gov/Sessions/2025/FiscalNotes/House/PDF/HFN696v4.pdf",
      "https://medicaid.ncdhhs.gov/providers/claims-and-billing/october-1-2025-nc-medicaid-rate-reduction-questions-and-answers",
      "https://medicaid.ncdhhs.gov/about-nc-medicaid/understanding-impact-cuts-nc-medicaid-budget",
      "https://webservices.ncleg.gov/ViewDocSiteFile/104990",
      "https://medicaid.ncdhhs.gov/about-nc-medicaid/eligibility/immigration-status-and-eligibility-nc-medicaid"
    ],
    "confidence": "medium",
    "verify": "Good practice, not a legal duty. The 10 to 20 percent range is an assumption for planning, not an NC forecast. Confirm whether SL 2026-1 or a later budget closed the Medicaid funding gap; the budget page is dated March 2026. Confirm which fee schedules hold your codes.",
    "basis": "recommended",
    "effective_date": "unknown"
  },
  "step_30_sub_3": {
    "instructions": [
      "Set a cash reserve target, for example 60 to 90 days of operating expenses, using the 20 percent scenario from your reimbursement-risk budget, and have the board approve it in writing.",
      "Schedule a reserve review each quarter and whenever NC Medicaid publishes a rate bulletin or fee schedule change, or a Tailored Plan issues a rate schedule or contract amendment.",
      "Subscribe to NC Medicaid Bulletins and to Alliance, Trillium and Vaya Partners provider communications. Log each rate notice with its effective date.",
      "Add fixed review dates on October 1 and January 1, the H.R. 1 eligibility milestones, and July 1, the start of the state fiscal year and the date G.S. 108A-58.3 takes effect."
    ],
    "tips": [
      "Vaya Partners standard rate schedules took effect for its whole network on October 1, 2026. Former Partners providers should compare their old rates with the new ones now.",
      "Health plans get 45 days to load DHB rate changes and 30 more days to reprocess claims, as in the August 1, 2026 PCS increase. Expect a similar cash lag when rates change.",
      "Keep reserves in a separate account with a written drawdown policy. Auditors and LME/MCO financial reviewers look for board control."
    ],
    "contacts": [
      "NC Medicaid Contact Center: 888-245-0179 (https://medicaid.ncdhhs.gov)",
      "Vaya Partners ACCESS Provider Services: 1-866-990-9712 (https://providers.vayahealth.com/contact/)",
      "Trillium Health Resources Provider Support Services: 1-855-250-1539 (https://www.trilliumhealthresources.org/NCRootsHub)"
    ],
    "sources": [
      "https://resources.vayapartners.org/",
      "https://medicaid.ncdhhs.gov/blog/2026/08/04/updates-rate-increase-personal-care-services-and-community-alternatives-program",
      "https://medicaid.ncdhhs.gov/blog/2025/10/30/updated-nc-medicaid-rate-reductions-effective-oct-1-2025",
      "https://medicaid.ncdhhs.gov/about-nc-medicaid/understanding-impact-cuts-nc-medicaid-budget",
      "https://www.ncleg.gov/EnactedLegislation/SessionLaws/HTML/2025-2026/SL2026-1.html"
    ],
    "confidence": "medium",
    "verify": "Good practice only. No NC or federal source sets a reserve level for these providers; the 60 to 90 days figure is a common planning benchmark, not a verified rule. Check whether any Tailored Plan contract or accreditor sets a financial-solvency standard (NOT VERIFIED).",
    "basis": "recommended",
    "effective_date": "unknown"
  },
  "step_31_sub_0": {
    "instructions": [
      "Bookmark the NCDHHS Rural Health Transformation Program page and its Grant Opportunities page. NC calls the program NCRHTP; NC ROOTS is its regional hub network.",
      "Review the Rural Health Innovation Fund: complete the readiness intake on ncbroadband.gov, then apply in the NCDIT grant portal by 11:59 p.m. on November 16, 2026.",
      "Confirm eligibility: a facility in one of the 85 federally designated rural counties or at least 40 percent rural patients, no SAM.gov or NC Medicaid sanction, and a low or medium risk rating.",
      "Check your county's NC ROOTS Hub Lead page for regional sub-award requests for applications, and sign up for its updates list."
    ],
    "tips": [
      "The sources conflict: the Governor's September 30, 2026 release limits the first RHIF round to primary care, FQHCs, community health centers and certain safety-net providers, while ncbroadband.gov lists behavioral health providers. Email RHIF@nc.gov before you apply.",
      "RHIF is reimbursement-based, awards are expected in January 2027, and projects must be finished by July 30, 2027. You will need cash to pay for project costs up front.",
      "Several earlier NCRHTP opportunities, including the hub lead application and the school health, diabetes and EMS programs, are closed. Do not plan around them."
    ],
    "contacts": [
      "Rural Health Innovation Fund: RHIF@nc.gov (https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-health-transformation-program-grant-opportunities)",
      "NCDIT Division of Broadband and Digital Opportunity: 919-754-6733 (https://www.ncbroadband.gov/ruralhealthinnovation)",
      "NCDHHS Customer Service Center: 1-800-662-7030 (https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program)"
    ],
    "sources": [
      "https://www.medicaid.gov/resources-for-states/rural-health",
      "https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program",
      "https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-health-transformation-program-grant-opportunities",
      "https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/ncrhtp-initiative-six-digital-health",
      "https://www.ncbroadband.gov/ruralhealthinnovation",
      "https://governor.nc.gov/news/press-releases/2026/09/30/governor-stein-launches-20-million-fund-increase-access-care-rural-north-carolina",
      "https://governor.nc.gov/news/press-releases/2025/12/29/north-carolina-awarded-213-million-rural-health-transformation-program"
    ],
    "confidence": "high",
    "verify": "Optional funding, not a provider obligation. Statute: H.R. 1 Sec. 71401, $50 billion over FY2026 to FY2030. CMS awarded NC $213,008,356.47 for year 1 on December 29, 2025. Settle the conflict over first-round RHIF eligibility with RHIF@nc.gov. Suggested rewording: Check whether NCRHTP or NC ROOTS funding is open to your organization and counties.",
    "basis": "recommended",
    "effective_date": "RHIF application deadline 2026-11-16"
  },
  "step_31_sub_1": {
    "instructions": [
      "Find your counties' Medicaid region on the NCDHHS ROOTS Hub Leads map, and match each county to its hub lead.",
      "Email the hub lead: Region 1 Impact Health (t.smith@impacthealth.org), Regions 2 and 5 Trillium, Region 3 Vaya (RHTP@vayahealth.com), Region 4 UNC Health, Region 6 Access East (rhtp@accesseast.org).",
      "Ask how providers join the partner network, when the next request for applications opens, which behavioral health and substance use priorities the regional needs assessment found, and what data reporting is required.",
      "Sign up for each hub's interest or contact list, then log the replies and next-contact dates in your grants tracker."
    ],
    "tips": [
      "Trillium's first round of requests for applications for Regions 2 and 5 is closed, and Trillium says more will follow. Region 3 (Vaya) and Region 4 (UNC Health) are still building their application processes.",
      "Hub regions include urban counties such as Mecklenburg, but funding generally targets rural residents. Be ready to show the rural share of the people you serve.",
      "Use the hub's official mailbox rather than staff personal emails, so your request is logged."
    ],
    "contacts": [
      "Trillium NC ROOTS Hub Regions 2 and 5: Region2NCRootsHub@trilliumnc.org, Region5NCRootsHub@trilliumnc.org (https://www.trilliumhealthresources.org/NCRootsHub)",
      "UNC Health NC ROOTS Region 4: NCROOTSRegion4@unchealth.unc.edu (https://www.unchealth.org/ncroots)",
      "Access East NC ROOTS Region 6: rhtp@accesseast.org (https://accesseast.org/nc-roots-hub-region-6/)"
    ],
    "sources": [
      "https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-organizations-orchestrating-transformation-sustainability-roots-hub-leads",
      "https://www.ncdhhs.gov/news/press-releases/2026/05/01/ncdhhs-selects-nc-roots-hub-leads-strengthen-rural-health-care-across-north-carolina",
      "https://www.trilliumhealthresources.org/NCRootsHub",
      "https://www.trilliumhealthresources.org/NC-ROOTS-Region-2",
      "https://rhtp.vayapartners.org/",
      "https://www.unchealth.org/ncroots",
      "https://impacthealth.org/rural-health/",
      "https://accesseast.org/nc-roots-hub-region-6/"
    ],
    "confidence": "high",
    "verify": "Optional, not a provider obligation. The email addresses come from the NCDHHS hub lead page (October 2026). Check whether Vaya's Region 3 mailbox changed after the October 1, 2026 Vaya Partners merger. The Region 4 and Region 5 county lists were not checked here.",
    "basis": "recommended",
    "effective_date": "unknown"
  },
  "step_31_sub_2": {
    "instructions": [
      "Draft a one-page capability statement listing your legal name, NPI, DHSR license numbers and services (CCP 8G peer support, 8A-12 SAIOP, 8A-13 SACOT).",
      "List the counties you serve, marking which are among the 85 federally designated rural counties, and give the percentage of rural clients.",
      "Describe your peer workforce: number of NC Certified Peer Support Specialists, their lived-experience focus, supervision structure and training pipeline.",
      "State expected outcomes tied to NCRHTP behavioral health and workforce initiatives, such as engagement in treatment, step-down from SACOT to SAIOP, emergency department diversion, and NCCARE360 referral closure."
    ],
    "tips": [
      "Match your wording to NCRHTP's six initiatives, especially Behavioral Health Expansion and Workforce Development. Hub reviewers score how well you fit regional priorities.",
      "Add SAM.gov registration status, your NC Medicaid enrollment status and Tailored Plan contracts. RHIF eligibility excludes applicants sanctioned in SAM.gov or by NC Medicaid.",
      "Use only outcomes you can measure from your EHR or NC-TOPPS data, because grant reports will hold you to them."
    ],
    "contacts": [
      "NCDHHS Customer Service Center: 1-800-662-7030 (https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program)"
    ],
    "sources": [
      "https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program",
      "https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/ncrhtp-initiative-six-digital-health",
      "https://rhtp.vayapartners.org/",
      "https://www.trilliumhealthresources.org/NC-ROOTS-Region-2"
    ],
    "confidence": "medium",
    "verify": "Good practice only; no NC source requires a capability statement. Check the content against the specific request for applications, since hubs may require their own forms. Confirm the exact NC peer certification title and the count of certified staff before publishing.",
    "basis": "recommended",
    "effective_date": "unknown"
  },
  "step_31_sub_3": {
    "instructions": [
      "Add these dates to the compliance calendar: RHIF application due 11:59 p.m. November 16, 2026; awards expected January 2027; RHIF projects complete by July 30, 2027.",
      "Calendar a 21-day appeal window after any RHIF ineligibility or non-approval email, with appeals sent to RHIF@nc.gov.",
      "Check whether your EHR can send HL7 v2 data to NC HealthConnex, which G.S. 90-414.4 requires for providers that receive state funds. Ask RHTP.HIEA@nc.gov about one-time rural connection funding.",
      "Plan NCCARE360 adoption if you apply for hub sub-awards, because Trillium's Region 2 and 5 requests for applications build in NCCARE360 closed-loop referrals.",
      "After any award, calendar the reporting dates, invoice deadlines and data submissions in the sub-award agreement."
    ],
    "tips": [
      "AUDIT TRAP: RHIF and hub funds are federal money. Expect a risk assessment, reimbursement-only payment and records of allowable costs, and keep receipts tied to each budget line.",
      "The HIEA says enforcement of the NC HealthConnex funding penalty is temporarily suspended, but the duty to connect still applies. Connecting now strengthens rural grant applications.",
      "Hub request-for-application windows have been short; Trillium's Region 2 round ran from July 30 to August 24, 2026. Check hub pages every two weeks."
    ],
    "contacts": [
      "NC HIEA: (919) 754-6912 (https://hiea.nc.gov/programs/nc-rural-health-transformation-program)",
      "Rural Health Innovation Fund: RHIF@nc.gov (https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/ncrhtp-initiative-six-digital-health)",
      "NCDIT Division of Broadband and Digital Opportunity: 919-754-6733 (https://www.ncbroadband.gov/ruralhealthinnovation)"
    ],
    "sources": [
      "https://governor.nc.gov/news/press-releases/2026/09/30/governor-stein-launches-20-million-fund-increase-access-care-rural-north-carolina",
      "https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/ncrhtp-initiative-six-digital-health",
      "https://hiea.nc.gov/programs/nc-rural-health-transformation-program",
      "https://hiea.nc.gov/faqs/health-care-provider-faqs",
      "https://www.trilliumhealthresources.org/NC-ROOTS-Region-2",
      "https://www.ncbroadband.gov/ruralhealthinnovation"
    ],
    "confidence": "medium",
    "verify": "The grant conditions apply only if you apply or receive an award. The NC HealthConnex connection duty under G.S. 90-414.4 is a current legal duty. Federal sub-award conditions, such as single audit thresholds and SAM UEI registration, are NOT VERIFIED for NCRHTP; read the award agreement and ask a CPA.",
    "basis": "recommended",
    "effective_date": "2026-11-16 (RHIF deadline); 2027-07-30 (RHIF project completion)"
  }
}
```

B) SOURCES

| Title | Publisher | URL | Date / version | Type |
|---|---|---|---|---|
| H.R. 1 summary (PL 119-21) | Congress.gov | link[congress.gov](https://www.congress.gov/bill/119th-congress/house-bill/1?share_frome=aipt) | PL 119-21, 7/4/2025 | Primary |
| CMCS Informational Bulletin on H.R. 1 provisions | CMS | link[medicaid.gov](https://www.medicaid.gov/federal-policy-guidance/downloads/cib11182025.pdf?share_frome=aipt) | 11/18/2025 | Primary |
| SMD 26-001, Sec. 71107 redeterminations | CMS | link[medicaid.gov](https://www.medicaid.gov/federal-policy-guidance/downloads/smd26001.pdf?share_frome=aipt) | 2026 | Primary |
| Sec. 71109 State Implementation Tool | CMS | link[medicaid.gov](https://www.medicaid.gov/medicaid/downloads/State-Implementation-Tool-Sect-71109.pdf?share_frome=aipt) | 2026 | Primary |
| Rural Health Transformation Program | CMS | link[medicaid.gov](https://www.medicaid.gov/resources-for-states/rural-health?share_frome=aipt) | accessed 10/2026 | Primary |
| Database checks toolkit, 42 CFR 455.436 | CMS | link[cms.gov](https://www.cms.gov/sites/default/files/repo-new/24/Toolkit%20for%20Database%20Checks%2042%20CFR%20455%20436.pdf?share_frome=aipt) | undated | Primary |
| Good Faith Estimate FAQs; NSA Part II fact sheet | CMS | FAQ[cms.gov](https://www.cms.gov/cciio/resources/regulations-and-guidance/downloads/guidance-good-faith-estimates-faq.pdf?share_frome=aipt), fact sheet[cms.gov](https://www.cms.gov/newsroom/fact-sheets/requirements-related-surprise-billing-part-ii-interim-final-rule-comment-period?share_frome=aipt) | in effect since 1/1/2022 | Primary |
| Exclusions Program; 2013 Special Advisory Bulletin | HHS-OIG | LEIE[oig.hhs.gov](https://oig.hhs.gov/exclusions/?share_frome=aipt), bulletin[oig.hhs.gov](https://oig.hhs.gov/exclusions/special-advisory-bulletin-and-other-guidance/the-effect-of-exclusion-from-participation-in-federal-health-care-programs/?share_frome=aipt) | 2013 bulletin | Primary |
| SAM.gov Exclusions | GSA | link[sam.gov](https://sam.gov/content/exclusions?share_frome=aipt) | accessed 10/2026 | Primary |
| Medicaid is Changing in 2026-27 | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/beneficiaries/medicaid-is-changing?share_frome=aipt) | modified 10/2026 | Primary |
| DCDL letter: H.R. 1 beneficiary mailings | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/dcdl-re-hr-1-beneficiary-mailings/open?share_frome=aipt) | 6/18/2026 | Primary |
| Immigration Status and Eligibility | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/about-nc-medicaid/eligibility/immigration-status-and-eligibility-nc-medicaid?share_frome=aipt) | 10/2026 | Primary |
| MA-2504 eligibility manual | NCDHHS | link[policies.ncdhhs.gov](https://policies.ncdhhs.gov/wp-content/uploads/MA-2504-Final.pdf?share_frome=aipt) | revised 10/2/2026 | Primary |
| Federal Medicaid Changes: What Providers Need to Know | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers/federal-medicaid-changes-what-providers-need-know?share_frome=aipt) | modified 10/13/2026 | Primary |
| Provider Billing of Medicaid Beneficiaries (10A NCAC 22J .0106) | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers-billing-beneficiaries/open?share_frome=aipt) | undated | Primary |
| Managed Care Billing Guidance to Health Plans (copays) | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/health-plan-billing-guide-version-32/open?share_frome=aipt) | v32 | Primary |
| Retro-eligibility claim submission | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/blog/2026/08/10/claim-submission-process-when-eligibility-retroactively-updated?share_frome=aipt) | 8/10/2026 | Primary |
| Tailored Plan Provider Quick Reference Guide | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/provider-quick-reference-guide-tailored-plans/open?share_frome=aipt) | 2026 | Primary |
| Recipient eligibility special bulletin | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/0814specialbulletinrecipienteligibility/download?attachment=&share_frome=aipt) | older | Primary (medium) |
| Required Provider Disclosures; Spring 2026 Quarterly Update | NC Medicaid | disclosures[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/blog/2025/11/04/reminders-about-required-provider-disclosures?share_frome=aipt), update[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/blog/2026/04/16/quarterly-provider-update-spring-2026?share_frome=aipt) | 11/4/2025; 4/16/2026 | Primary |
| PDM/CVO pause | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers/provider-data-management-credentialing-verification-organization?share_frome=aipt) | 2026 | Primary |
| Excluded Providers | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers/excluded-providers?share_frome=aipt) | list updated 9/24/2026 | Primary |
| Rate reduction bulletin and Q&A; Budget cuts page | NC Medicaid | bulletin[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/blog/2025/10/30/updated-nc-medicaid-rate-reductions-effective-oct-1-2025?share_frome=aipt), Q&A[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers/claims-and-billing/october-1-2025-nc-medicaid-rate-reduction-questions-and-answers?share_frome=aipt), budget[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/about-nc-medicaid/understanding-impact-cuts-nc-medicaid-budget?share_frome=aipt) | 10/30/2025; 3/2026 | Primary |
| PCS rate increase (plan rate-load timing) | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/blog/2026/08/04/updates-rate-increase-personal-care-services-and-community-alternatives-program?share_frome=aipt) | 8/4/2026 | Primary |
| Vaya/Partners merger notice | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/information-regarding-vaya-health-and-partners-health-management-merger/download?attachment=&share_frome=aipt) | 9/2026 | Primary |
| NCDHHS Provider Administrative Participation Agreement | NCTracks | link[nctracks.nc.gov](https://www.nctracks.nc.gov/content/public/providers/provider-enrollment/terms-and-conditions/admin-participation-rev.html?share_frome=aipt) | current | Primary |
| Re-credentialing/Re-verification; Glossary (AVRS) | NCTracks | recredentialing[nctracks.nc.gov](https://www.nctracks.nc.gov/content/public/providers/provider-recredentialing.html?share_frome=aipt), glossary[nctracks.nc.gov](https://www.nctracks.nc.gov/content/public/providers/faq-main-page/nctracks-glossary-of-terms.html?share_frome=aipt) | current | Primary |
| SL 2026-1 (HB 696) | NCGA | link[ncleg.gov](https://www.ncleg.gov/EnactedLegislation/SessionLaws/HTML/2025-2026/SL2026-1.html?share_frome=aipt) | 2026 | Primary |
| G.S. Chapter 108D Article 4 (108D-40) | NCGA | link[ncleg.gov](https://ncleg.gov/EnactedLegislation/Statutes/HTML/ByArticle/Chapter_108D/Article_4.html?share_frome=aipt) | eff. 10/1/2026 version | Primary |
| Fiscal note, HB 696 v4 | NCGA Fiscal Research | link[ncleg.gov](https://www.ncleg.gov/Sessions/2025/FiscalNotes/House/PDF/HFN696v4.pdf?share_frome=aipt) | 2025-26 | Primary |
| H.R. 1 Eligibility and Enrollment Changes for NC Medicaid | NCDHHS presentation to NCGA | link[webservices.ncleg.gov](https://webservices.ncleg.gov/ViewDocSiteFile/104990?share_frome=aipt) | 8/2026 | Primary |
| NCRHTP main page; Grant Opportunities; Initiative Six; ROOTS Hub Leads; Hub Lead press release | NCDHHS | main[ncdhhs.gov](https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program?share_frome=aipt), grants[ncdhhs.gov](https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-health-transformation-program-grant-opportunities?share_frome=aipt), digital[ncdhhs.gov](https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/ncrhtp-initiative-six-digital-health?share_frome=aipt), hubs[ncdhhs.gov](https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-organizations-orchestrating-transformation-sustainability-roots-hub-leads?share_frome=aipt), release[ncdhhs.gov](https://www.ncdhhs.gov/news/press-releases/2026/05/01/ncdhhs-selects-nc-roots-hub-leads-strengthen-rural-health-care-across-north-carolina?share_frome=aipt) | 5/1/2026 to 10/2026 | Primary |
| NC awarded $213M; RHIF launch | NC Governor | award[governor.nc.gov](https://governor.nc.gov/news/press-releases/2025/12/29/north-carolina-awarded-213-million-rural-health-transformation-program?share_frome=aipt), RHIF[governor.nc.gov](https://governor.nc.gov/news/press-releases/2026/09/30/governor-stein-launches-20-million-fund-increase-access-care-rural-north-carolina?share_frome=aipt) | 12/29/2025; 9/30/2026 | Primary |
| Rural Health Innovation Fund | NCDIT | link[ncbroadband.gov](https://www.ncbroadband.gov/ruralhealthinnovation?share_frome=aipt) | 9/2026 | Primary |
| NC RHTP program page; Provider FAQs | NC HIEA | RHTP[hiea.nc.gov](https://hiea.nc.gov/programs/nc-rural-health-transformation-program?share_frome=aipt), FAQ[hiea.nc.gov](https://hiea.nc.gov/faqs/health-care-provider-faqs?share_frome=aipt) | 2026 | Primary |
| Alliance Tailored Plan Provider Manual; Provider Central | Alliance Health | manual[alliancehealthplan.org](https://www.alliancehealthplan.org/document-library/79431/?share_frome=aipt), providers[alliancehealthplan.org](https://www.alliancehealthplan.org/providers/?share_frome=aipt) | 2026 | Primary (plan) |
| Trillium Provider Manual; NC ROOTS Hub; Region 2 | Trillium | manual[trilliumhealthresources.org](https://www.trilliumhealthresources.org/sites/default/files/docs/Provider-documents/Provider-Manual/Trillium-Provider-Manual.pdf?share_frome=aipt), hub[trilliumhealthresources.org](https://www.trilliumhealthresources.org/NCRootsHub?share_frome=aipt), Region 2[trilliumhealthresources.org](https://www.trilliumhealthresources.org/NC-ROOTS-Region-2?share_frome=aipt) | 2026 | Primary (plan) |
| Vaya Partners contact page; merger resources; Sept. 10, 2026 provider bulletin; Region 3 RHTP | Vaya Partners | contact[providers.vayahealth.com](https://providers.vayahealth.com/contact/?share_frome=aipt), merger[resources.vayapartners.org](https://resources.vayapartners.org/?share_frome=aipt), bulletin[providers.vayahealth.com](https://providers.vayahealth.com/wp-content/uploads/2026/09/pcb-09-10-26-issue-17.pdf?share_frome=aipt), Region 3[rhtp.vayapartners.org](https://rhtp.vayapartners.org/?share_frome=aipt) | 9 to 10/2026 | Primary (plan) |
| Impact Health, UNC Health, Access East hub pages | Hub leads | Impact[impacthealth.org](https://impacthealth.org/rural-health/?share_frome=aipt), UNC[unchealth.org](https://www.unchealth.org/ncroots?share_frome=aipt), Access East[accesseast.org](https://accesseast.org/nc-roots-hub-region-6/?share_frome=aipt) | 2026 | Primary (hub) |

C) CORRECTIONS

- **Step 29, cost-sharing:** The new cost sharing for expansion adults does not reach these services. Under Sec. 71120 it starts October 1, 2028, applies only to expansion adults above 100% FPL, and exempts mental health and SUD services (Congress.gov; CMS CIB). NC already exempts behavioral health claims from copays.[congress.gov](https://www.congress.gov/bill/119th-congress/house-bill/1?share_frome=aipt)[medicaid.gov](https://www.medicaid.gov/federal-policy-guidance/downloads/cib11182025.pdf?share_frome=aipt)[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/health-plan-billing-guide-version-32/open?share_frome=aipt)
  - Separately, the new state statute G.S. 108A-58.3 sets copays at the federal maximum starting July 1, 2027.[ncleg.gov](https://www.ncleg.gov/EnactedLegislation/SessionLaws/HTML/2025-2026/SL2026-1.html?share_frome=aipt)
- **Step 29, retroactive coverage:** The shorter window applies only to applications made on or after January 1, 2027: 1 month for expansion adults and 2 months for others. Applications filed through December 31, 2026 keep 3 months.[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/beneficiaries/medicaid-is-changing?share_frome=aipt)
- **Step 29, immigrant eligibility:** This is not a future change. It took effect October 1, 2026, and emergency-only noncitizens are now excluded from health plans.[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/about-nc-medicaid/eligibility/immigration-status-and-eligibility-nc-medicaid?share_frome=aipt)[ncleg.gov](https://ncleg.gov/EnactedLegislation/Statutes/HTML/ByArticle/Chapter_108D/Article_4.html?share_frome=aipt)
- **"Each Tailored Plan":** There are now three: Alliance, Trillium and Vaya Partners. Vaya and Partners merged on October 1, 2026.[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/information-regarding-vaya-health-and-partners-health-management-merger/download?attachment=&share_frome=aipt)
- **Step 30, screening:** H.R. 1 did not add more frequent exclusion checks.
  - Monthly LEIE and SAM checks predate H.R. 1 and come from 42 CFR 455.436. The provider duty to screen staff monthly comes from the participation agreement.[cms.gov](https://www.cms.gov/sites/default/files/repo-new/24/Toolkit%20for%20Database%20Checks%2042%20CFR%20455%20436.pdf?share_frome=aipt)[nctracks.nc.gov](https://www.nctracks.nc.gov/content/public/providers/provider-enrollment/terms-and-conditions/admin-participation-rev.html?share_frome=aipt)
  - Sec. 71105 adds only a state duty: quarterly Death Master File checks of providers starting January 1, 2028.[medicaid.gov](https://www.medicaid.gov/federal-policy-guidance/downloads/cib11182025.pdf?share_frome=aipt)
  - "Death records NC Medicaid requires" of providers is not supported. Only Alliance's manual lists the SSA DMF.[alliancehealthplan.org](https://www.alliancehealthplan.org/document-library/79431/?share_frome=aipt)
- **Step 30, financing limits:** These mainly affect hospital assessments and HASP directed payments.[ncleg.gov](https://www.ncleg.gov/Sessions/2025/FiscalNotes/House/PDF/HFN696v4.pdf?share_frome=aipt)
  - The phase-down schedules conflict. The fiscal note says 0.5% per year from 2028, reaching 3.5% in 2034. CMS says 5.5% from October 1, 2027, reaching 3.5% in FY2032. CMS is more authoritative.
  - NC's October 2025 cuts came from the state budget, not H.R. 1, and were reversed December 10, 2025.[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/about-nc-medicaid/understanding-impact-cuts-nc-medicaid-budget?share_frome=aipt)
- **Step 30, main resource:** Adding SAM.gov and the NC State Excluded Provider List would be more accurate, since screening requires them too.[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers/excluded-providers?share_frome=aipt)
- **Step 31, program name:** NC's program is the NC Rural Health Transformation Program (NCRHTP). NC ROOTS is its regional hub network, which is one of six initiatives.[ncdhhs.gov](https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program?share_frome=aipt)
  - Nationally the program is $50 billion over FY2026 to FY2030. NC's year-1 award is $213,008,356.47.[medicaid.gov](https://www.medicaid.gov/resources-for-states/rural-health?share_frome=aipt)
- **Step 31, hub leads:** Five hub leads cover six regions: Impact Health (1), Trillium (2 and 5), Vaya (3), UNC Health (4) and Access East (6).[ncdhhs.gov](https://www.ncdhhs.gov/news/press-releases/2026/05/01/ncdhhs-selects-nc-roots-hub-leads-strengthen-rural-health-care-across-north-carolina?share_frome=aipt)
- **Step 31, main resource:** The generic ncdhhs.gov address should point to the NCRHTP page instead.
- **Step 31, rural eligibility:** It is not based on county alone. RHIF requires one of 85 federally designated rural counties or at least 40% rural patients, plus no SAM or NC Medicaid sanction and a low or medium risk rating.[ncbroadband.gov](https://www.ncbroadband.gov/ruralhealthinnovation?share_frome=aipt)
- **Step 31, cost:** "$0" may be misleading. RHIF is reimbursement-based, so you pay project costs up front.[governor.nc.gov](https://governor.nc.gov/news/press-releases/2026/09/30/governor-stein-launches-20-million-fund-increase-access-care-rural-north-carolina?share_frome=aipt)
- **Steps 29 to 31, scope:** Several tasks are not provider legal duties (29_sub_2, 30_sub_2, 30_sub_3 and all of Step 31). Suggested rewordings are in each verify field.

D) OPEN QUESTIONS

- **RHIF first-round eligibility:** The Governor's release lists only primary care and health-center types. NCDIT lists behavioral health providers. Ask RHIF@nc.gov or NCDIT at 919-754-6733.[ncbroadband.gov](https://www.ncbroadband.gov/ruralhealthinnovation?share_frome=aipt)[governor.nc.gov](https://governor.nc.gov/news/press-releases/2026/09/30/governor-stein-launches-20-million-fund-increase-access-care-rural-north-carolina?share_frome=aipt)
- **Sliding fees for state-funded services:** Whether LME/MCO contracts require a sliding fee for state-funded SAIOP, SACOT or peer support. Ask contracting staff at Alliance, Trillium and Vaya Partners.
- **Copays after July 1, 2027:** Whether G.S. 108A-58.3 will change NC's behavioral health copay exemption for groups other than expansion adults. Ask the NC Medicaid Contact Center (888-245-0179) and watch Medicaid Bulletins.
- **NCTracks codes:** The aid category or benefit plan codes that show emergency-only coverage. Ask the NCTracks Call Center (800-688-6696).
- **Undocumented reporting rules:**
  - Whether taxonomy and managing-employee changes fall under the 30-day rule. Ask NCTracks.
  - Vaya Partners' rules for exclusion screening and reporting. Ask Vaya Partners at 1-866-990-9712.
- **Effective date of G.S. 108A-55.7:** Applies to the 3-month community engagement look-back (SL 2026-1 Section 3C.5). Read the full session law or ask NCGA Fiscal Research.
- **Medicaid funding gap:** Whether SL 2026-1 closed the FY2025-26 gap. The NC Medicaid budget page is dated March 2026.[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/about-nc-medicaid/understanding-impact-cuts-nc-medicaid-budget?share_frome=aipt)
- **Hub details not verified:**
  - Region 4 and Region 5 county lists.
  - The Region 3 hub email after the merger.
  - Region 3 and Region 4 application timelines.
  - Ask each hub mailbox.
- **NCRHTP federal sub-award conditions:** Includes SAM UEI registration and audit thresholds. Read the award agreement and confirm with a CPA.