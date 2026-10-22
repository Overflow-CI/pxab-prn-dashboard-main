> From: https://www.perplexity.ai/computer/tasks/25f8abda-584c-4ac7-a9db-946f9727db46

# you asked

message time: 2026-10-18 21:47:08

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

---

# perplexity response

A) JSON

```json
{
  "step_26_sub_0": {
    "instructions": [
      "Read the CMS informational bulletin of Nov. 18, 2025 (CIB) on Public Law 119-21 for the federal dates in sections 71107, 71109, 71112, 71119 and 71120.",
      "Read the NC Medicaid page Federal Medicaid Changes: What Providers Need to Know and its linked Work and Community Engagement Requirement page for NC's dates and steps.",
      "Read the draft NC Medicaid H.R.1 Medical Frailty Exclusions policy (Policy No. HR-1), the DSS-8209 Medical Report and the code list. Public comment closes Nov. 5, 2026.",
      "Read G.S. 108A-55.7, effective Jan. 1, 2027. NC applicants must show 3 consecutive compliant months before applying, and 3 of the last 6 months at each renewal.",
      "Write a one-page memo marking each provision as affecting your clients' coverage, your billing, or your documentation, and file it with compliance records."
    ],
    "tips": [
      "Cost sharing (section 71120, starting Oct. 1, 2028) exempts behavioral health services, so it should not apply to 8G, SAIOP or SACOT claims. Confirm against NC's final State Plan before telling clients.",
      "Most H.R. 1 changes hit client eligibility, not your license. The provider-facing items are eligibility checks, faster coverage churn, shorter retroactive coverage, and DSS-8209 medical reports.",
      "AUDIT TRAP: NC's medical frailty policy is a DRAFT until NC Medicaid posts the final version, expected late Nov. or early Dec. 2026. Check the date on your memo against the final policy."
    ],
    "contacts": [
      "NC Medicaid Contact Center: 888-245-0179 (medicaid.ncdhhs.gov)",
      "NC Medicaid public comments on H.R. 1 medical frailty policy: medicaid.public.comment@dhhs.nc.gov (medicaid.ncdhhs.gov/providers/medical-frailty-clinical-coverage-policy-and-comment-period)"
    ],
    "sources": [
      "https://www.congress.gov/bill/119th-congress/house-bill/1",
      "https://www.medicaid.gov/federal-policy-guidance/downloads/cib11182025.pdf",
      "https://www.medicaid.gov/resources-for-states/working-families-tax-cut-legislation",
      "https://medicaid.ncdhhs.gov/providers/federal-medicaid-changes-what-providers-need-know",
      "https://medicaid.ncdhhs.gov/beneficiaries/impact-hr-1-and-federal-changes-medicaid/work-and-community-engagement-requirement",
      "https://medicaid.ncdhhs.gov/providers/medical-frailty-clinical-coverage-policy-and-comment-period",
      "https://medicaid.ncdhhs.gov/media/16285/download?attachment",
      "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108A/GS_108A-55.7.html"
    ],
    "confidence": "high",
    "verify": "Not a legal duty. Suggested wording: Review H.R. 1 provisions and NC Medicaid H.R. 1 provider guidance that affect client eligibility, billing and documentation. Re-check the final Medical Frailty policy (late Nov. or early Dec. 2026). Also check whether CMS has approved any NC good-faith extension, since NCDHHS told CMS on July 30, 2026 that full implementation by Jan. 1, 2027 is unlikely.",
    "basis": "recommended",
    "effective_date": "unknown"
  },
  "step_26_sub_1": {
    "instructions": [
      "Draft a governing body resolution naming one H.R. 1 compliance owner and one backup, with duties: monitoring, calendar, staff training, DSS-8209 process and quarterly reporting.",
      "Approve the resolution at a governing body meeting and record it in signed, dated minutes kept with your 10A NCAC 27G governing body policies.",
      "Add the owner and backup to your compliance plan, organizational chart and job descriptions, and give both login access to bulletin subscriptions and Tailored Plan portals.",
      "Re-confirm both names at each annual policy review, and within 30 days of any staffing change."
    ],
    "tips": [
      "Pick a backup who is not the billing manager, so eligibility-denial trends are reviewed independently from the people who submit claims.",
      "Make sure the owner, or a named clinician, holds a credential on the DSS-8209 signer list. The current draft form (REV. 08/2026 and 09/2026) does not list LCAS or certified peer support specialists."
    ],
    "contacts": [
      "NC Medicaid Contact Center: 888-245-0179 (medicaid.ncdhhs.gov)"
    ],
    "sources": [
      "https://medicaid.ncdhhs.gov/providers/federal-medicaid-changes-what-providers-need-know",
      "https://medicaid.ncdhhs.gov/media/16282/download?attachment"
    ],
    "confidence": "medium",
    "verify": "No statute, CCP or Tailored Plan source I found requires a named H.R. 1 owner. This is internal good practice. Suggested wording: Assign H.R. 1 monitoring to your existing compliance officer, with a backup, and record it in governing body minutes. Have your healthcare attorney confirm your governing body documentation format.",
    "basis": "recommended",
    "effective_date": "unknown"
  },
  "step_26_sub_2": {
    "instructions": [
      "Sign up for NCTracks email communications through the NCTracks Provider Communications page (Sign up for NCTracks Communications). Per NC Medicaid, these emails link each Medicaid Bulletin shortly after it posts.",
      "Bookmark NC Medicaid's provider page Federal Medicaid Changes: What Providers Need to Know and the Medical Frailty policy page. Check both weekly until Jan. 31, 2027.",
      "Sign up for Alliance Health's Provider News Service emails, Trillium's Provider Communication Bulletins and Urgent Notifications, and Vaya Partners' Provider Communication Bulletins.",
      "Use a shared compliance mailbox for every subscription, so notices still arrive if staff leave. Log each H.R. 1 notice with its date and the action taken."
    ],
    "tips": [
      "Vaya Health and Partners Health Management merged into Vaya Partners on Oct. 1, 2026. NC now has three Tailored Plan LME/MCOs: Alliance, Trillium and Vaya Partners. Update old Partners or Vaya subscriptions.",
      "SAIOP, SACOT and peer support are also covered for Standard Plan members, so sign up for notices from each Standard Plan you contract with.",
      "AUDIT TRAP: Tailored Plan bulletins can change contract or billing requirements. Keep a dated log showing you received and acted on each notice."
    ],
    "contacts": [
      "NC Medicaid Communications: Medicaid.Communications@dhhs.nc.gov (medicaid.ncdhhs.gov/providers/medicaid-bulletin/medicaid-bulletin-digests)",
      "Trillium Health Resources Provider Support Service: 1-855-250-1539 (trilliumhealthresources.org)",
      "Vaya Partners ACCESS Provider Services: 1-866-990-9712 (providers.vayapartners.org)"
    ],
    "sources": [
      "https://medicaid.ncdhhs.gov/providers/medicaid-bulletin/medicaid-bulletin-digests",
      "https://medicaid.ncdhhs.gov/documents/providers/bulletins/archives/0813bulletin/download",
      "https://medicaid.ncdhhs.gov/providers/federal-medicaid-changes-what-providers-need-know",
      "https://www.alliancehealthplan.org/provider-updates/provider-news-service-email-sign-up/",
      "https://www.trilliumhealthresources.org/for-providers/provider-communications",
      "https://providers.vayapartners.org/bulletins/",
      "https://medicaid.ncdhhs.gov/information-regarding-vaya-health-and-partners-health-management-merger/open"
    ],
    "confidence": "medium",
    "verify": "The NCTracks sign-up link location comes from a 2013 Medicaid Bulletin. Check that the link still appears on the NCTracks Provider Communications page. Vaya Partners' bulletin page says Subscribe but shows no sign-up link: call ACCESS Provider Services. Alliance's sign-up page is dated 2021. This is recommended practice, not a stated legal duty.",
    "basis": "recommended",
    "effective_date": "unknown"
  },
  "step_26_sub_3": {
    "instructions": [
      "Build a dated calendar: Oct. 1, 2026 immigrant eligibility (in effect); Nov. 5, 2026 comment deadline; Jan. 1, 2027 work requirement, six-month renewals and retroactive limits; Oct. 1, 2028 cost sharing.",
      "For each date, set an internal deadline at least 30 days earlier and assign an owner. Add a watch item for the final Medical Frailty policy, expected late Nov. or early Dec. 2026.",
      "Mark each item as statute, CMS guidance or rule, NC announcement, or NC draft, with the source date. Show it as tentative until NC finalizes it.",
      "Review the calendar monthly in compliance meetings and update it within 5 business days of any new NC Medicaid or Tailored Plan notice."
    ],
    "tips": [
      "Six-month renewals apply to renewals scheduled on or after Jan. 1, 2027, per the CMS bulletin, CMS letter SMD 26-001 and NC Medicaid. The Dec. 2026 date in some materials is imprecise.",
      "Retroactive coverage limits apply to applications filed on or after Jan. 1, 2027: one month for expansion adults, two months for others. Plan for less retroactive recovery on uninsured intakes.",
      "Optional: track NC ROOTS (the Rural Health Transformation Program) funding rounds. NC was awarded $213 million on Dec. 29, 2025. This is a funding opportunity, not a compliance duty."
    ],
    "contacts": [
      "NC Medicaid Contact Center: 888-245-0179 (medicaid.ncdhhs.gov)"
    ],
    "sources": [
      "https://www.medicaid.gov/federal-policy-guidance/downloads/cib11182025.pdf",
      "https://www.medicaid.gov/federal-policy-guidance/downloads/smd26001.pdf",
      "https://medicaid.ncdhhs.gov/medicaid-hr1-essentials-deck-speakers-notes/download?attachment",
      "https://medicaid.ncdhhs.gov/providers/medical-frailty-clinical-coverage-policy-and-comment-period",
      "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108A/GS_108A-55.7.html",
      "https://www.ncdhhs.gov/news/press-releases/2025/12/29/north-carolina-awarded-213-million-rural-health-transformation-program-strategic-roadmap-and-federal"
    ],
    "confidence": "high",
    "verify": "Internal planning tool, not a legal duty. Watch for any CMS good-faith exemption for NC (the statute allows these through Dec. 31, 2028), which could move the work requirement date. NC's IFC comment letter of July 30, 2026 says full implementation by Jan. 1, 2027 is unlikely.",
    "basis": "recommended",
    "effective_date": "unknown"
  },
  "step_27_sub_0": {
    "instructions": [
      "Check eligibility in the NCTracks Provider Portal, AVRS or a 270/271 transaction at intake and on every date of service, as CCP 8G and 8A-12 Section 2.1.1 require.",
      "Record the health plan shown in NCTracks (Medicaid Direct, Standard Plan or Tailored Plan) and route claims and authorizations to that plan.",
      "If NCTracks shows no eligibility but the client has a card, call the NCTracks Call Center, which can check NC FAST directly. Updates can take up to a week.",
      "Save a screenshot or 271 response of each check in the EHR. Before each authorization renewal, also confirm the client's next six-month renewal date."
    ],
    "tips": [
      "AUDIT TRAP: The CCPs require eligibility checks each time a service is rendered, not once per billing period. Keep dated proof of every check for post-payment reviews.",
      "Before submitting claims, confirm eligibility shows in NCTracks, or the claim may deny even if NC FAST showed the client eligible.",
      "Starting Jan. 1, 2027, expansion adults renew every six months, so plan changes and lapses will be more frequent."
    ],
    "contacts": [
      "NCTracks Call Center: 1-800-688-6696 (nctracks.nc.gov)",
      "NC Medicaid Contact Center: 888-245-0179 (medicaid.ncdhhs.gov)"
    ],
    "sources": [
      "https://medicaid.ncdhhs.gov/8g-peer-support-services/download?attachment",
      "https://medicaid.ncdhhs.gov/media/15767/download",
      "https://www.nctracks.nc.gov/content/public/providers/provider-communications/provider-announcements/Verify-Recipient-Eligibility-with-NCTracks-Call-Center.html",
      "https://medicaid.ncdhhs.gov/managed-care-claims-submission-what-providers-need-know-part-1/open",
      "https://www.medicaid.gov/federal-policy-guidance/downloads/smd26001.pdf"
    ],
    "confidence": "high",
    "verify": "Confirm that CCP 8A-13 (SACOT) has the same Section 2.1.1 wording (each time a service is rendered) as 8G and 8A-12. Suggested wording: Verify Medicaid eligibility and health plan at intake and on every date of service.",
    "basis": "required",
    "effective_date": "In effect now (CCP eligibility check); six-month renewals begin 2027-01-01"
  },
  "step_27_sub_1": {
    "instructions": [
      "Set an EHR flag that holds claims automatically when NCTracks shows no eligibility for a date of service. Route held claims to the billing manager within 2 business days.",
      "Tell the client the same day, and document whether a renewal or application is pending with county DSS. Do not discharge for lapsed coverage alone without a clinical transition plan.",
      "If the client chooses to continue as self-pay, give the written private-pay notice required by 10A NCAC 22J .0106 before services. Refund any self-pay if retroactive Medicaid is later approved and billed.",
      "Ask the client's LME/MCO whether state-funded (non-Medicaid) services are available, and release or void held claims once eligibility is restored."
    ],
    "tips": [
      "AUDIT TRAP: Under 10A NCAC 22J .0106(f), once you are paid by Medicaid for a retroactively eligible client, you must refund what the client paid. Track this in the hold log.",
      "Retroactive coverage drops to one month (expansion adults) or two months (others) for applications filed on or after Jan. 1, 2027, so held claims may never become billable.",
      "Check each plan's timely filing limit before holding claims for a long time. Limits were not verified in this batch."
    ],
    "contacts": [
      "NCTracks Call Center: 1-800-688-6696 (nctracks.nc.gov)",
      "Trillium Health Resources Provider Support Service: 1-855-250-1539 (trilliumhealthresources.org)",
      "Vaya Partners ACCESS Provider Services: 1-866-990-9712 (providers.vayapartners.org)"
    ],
    "sources": [
      "http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2022%20-%20medical%20assistance%20eligibility/subchapter%20j/10a%20ncac%2022j%20.0106.pdf",
      "https://www.medicaid.gov/federal-policy-guidance/downloads/cib11182025.pdf",
      "https://www.nctracks.nc.gov/content/public/providers/provider-communications/provider-announcements/Verify-Recipient-Eligibility-with-NCTracks-Call-Center.html"
    ],
    "confidence": "medium",
    "verify": "NOT VERIFIED: timely filing limits for NC Medicaid Direct and each Tailored Plan or Standard Plan, and whether state-funded SAIOP, SACOT or peer support is available in your catchment area. Check the plan provider manuals or call provider services. Have a healthcare attorney review your self-pay notice. The hold workflow is good practice; the billing rules are required.",
    "basis": "recommended",
    "effective_date": "2027-01-01"
  },
  "step_27_sub_2": {
    "instructions": [
      "Train intake and peer staff to remind clients at each review to update their address and phone with local DSS and to answer DSS letters right away.",
      "Show clients how to find their local DSS at dhhs.nc.gov/localdss and how to call the NC Medicaid Contact Center. Encourage an enhanced ePASS account for uploading documents.",
      "Hand out NC Medicaid's Know What's Next toolkit flyers instead of making your own explanations of eligibility rules.",
      "Document each reminder or referral in the EHR, and record staff training completion with the date and materials used."
    ],
    "tips": [
      "Tell staff they may remind, refer and help with logistics, but not decide whether someone is eligible or exempt. Only DSS makes that decision.",
      "Starting Jan. 1, 2027, NC says most adults renew every six months, including many who do not have to meet the work requirement, so set reminders at every treatment plan review."
    ],
    "contacts": [
      "NC Medicaid Contact Center: 888-245-0179 (medicaid.ncdhhs.gov)",
      "Local DSS directory: dhhs.nc.gov/localdss"
    ],
    "sources": [
      "https://medicaid.ncdhhs.gov/medicaid-hr1-essentials-deck-speakers-notes/download?attachment",
      "https://medicaid.ncdhhs.gov/providers/federal-medicaid-changes-what-providers-need-know",
      "https://medicaid.ncdhhs.gov/beneficiaries/impact-hr-1-and-federal-changes-medicaid/work-and-community-engagement-requirement"
    ],
    "confidence": "high",
    "verify": "Not a legal duty. Good practice only. Check that the dhhs.nc.gov/localdss shortcut still redirects to the county DSS directory.",
    "basis": "recommended",
    "effective_date": "2027-01-01"
  },
  "step_27_sub_3": {
    "instructions": [
      "Add a required coverage-loss reason field to the EHR or billing log: procedural or paperwork, work requirement, income, immigration status, moved, regained coverage, or unknown.",
      "Run a monthly report of lapses by service line (8G, SAIOP, SACOT), payer and reason, plus days to restore coverage and dollars held or written off.",
      "Present the report quarterly to the governing body, and record its review and any corrective actions in the minutes.",
      "Share trends without client identifiers with your Tailored Plan provider network contact when lapses rise, and adjust staffing or intake reminders as needed."
    ],
    "tips": [
      "Record only reasons the client or a DSS notice states. Do not guess at an eligibility reason, and keep SUD details out of governing body reports to protect 42 CFR Part 2 records.",
      "Starting Jan. 1, 2027, compare monthly lapses to each client's six-month renewal month to catch paperwork-related losses early."
    ],
    "contacts": [
      "NC Medicaid Contact Center: 888-245-0179 (medicaid.ncdhhs.gov)"
    ],
    "sources": [
      "https://www.medicaid.gov/federal-policy-guidance/downloads/smd26001.pdf",
      "https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-2/subpart-C/section-2.31"
    ],
    "confidence": "medium",
    "verify": "Not a legal or contract duty that I found. Internal quality improvement only. Suggested wording: Track monthly Medicaid coverage lapses and reasons for quality improvement and governing body review.",
    "basis": "recommended",
    "effective_date": "unknown"
  },
  "step_28_sub_0": {
    "instructions": [
      "Read NC Medicaid's Work and Community Engagement page for who must comply: most adults ages 19 through 64 in the expansion group, starting Jan. 1, 2027 ($580 a month or 80 hours).",
      "Note the exclusions that fit your clients: people in a drug or alcohol treatment and rehabilitation program, a substance use disorder, a disabling mental disorder, or medical frailty.",
      "Read the draft H.R.1 Medical Frailty policy. NC checks Tier 1 codes in claims automatically. Providers complete a DSS-8209 Medical Report, signed by the client, for submission to the client's local DSS.",
      "Send comments by Nov. 5, 2026 to medicaid.public.comment@dhhs.nc.gov. Then ask each Tailored Plan how it will support members, while recognizing that DSS makes the determination."
    ],
    "tips": [
      "Tailored Plan-eligible members are automatically placed in Tier 1 under the draft policy. SAIOP (H0015) and SACOT (H2035) are Tier 1 service codes. Peer support (H0038) is not listed.",
      "Accurate coding matters. Mild use disorder codes such as F10.10 and F11.10 are not on the draft Tier 1 list, while F11.20 is. Never change a diagnosis to trigger an exclusion.",
      "AUDIT TRAP: Exemption documents go to county DSS, not to NCTracks or the Tailored Plan. Keep a copy of every DSS-8209 you sign and the date it was sent."
    ],
    "contacts": [
      "NC Medicaid public comments: medicaid.public.comment@dhhs.nc.gov (medicaid.ncdhhs.gov)",
      "NC Medicaid Contact Center: 888-245-0179 (medicaid.ncdhhs.gov)",
      "Alliance Health Provider Network: ProviderNetwork@alliancehealthplan.org (medicaid.ncdhhs.gov/about-nc-medicaid/health-plans)"
    ],
    "sources": [
      "https://medicaid.ncdhhs.gov/beneficiaries/impact-hr-1-and-federal-changes-medicaid/work-and-community-engagement-requirement",
      "https://medicaid.ncdhhs.gov/providers/medical-frailty-clinical-coverage-policy-and-comment-period",
      "https://medicaid.ncdhhs.gov/media/16285/download?attachment",
      "https://medicaid.ncdhhs.gov/media/16283/download?attachment",
      "https://www.medicaid.gov/federal-policy-guidance/downloads/cib11182025.pdf",
      "https://medicaid.ncdhhs.gov/about-nc-medicaid/health-plans"
    ],
    "confidence": "high",
    "verify": "Policy HR-1, the DSS-8209 and the code list are drafts, with final versions expected late Nov. or early Dec. 2026. Suggested wording: Confirm NC Medicaid's final medical frailty policy and DSS-8209 process; providers document, and county DSS decides. Also check whether peer support (H0038) or mild SUD codes are added to the final list.",
    "basis": "expected",
    "effective_date": "2027-01-01"
  },
  "step_28_sub_1": {
    "instructions": [
      "Have a healthcare attorney confirm whether each service line (SAIOP, SACOT, and peer support if SUD-focused) is a 42 CFR Part 2 program.",
      "Use the DSS-8209 Section B client permission, and check the separate 42 CFR Part 2 box whenever the report includes any SUD diagnosis or treatment information.",
      "If you use your own consent instead, include every 42 CFR 2.31(a) element: client name, discloser, specific information, recipient, purpose, revocation right, expiration, signature and date.",
      "Attach the 42 CFR 2.32 redisclosure notice to every Part 2 disclosure, and log each disclosure in the client record."
    ],
    "tips": [
      "The 2024 Part 2 final rule compliance date was Feb. 16, 2026, and HHS OCR began civil enforcement that day. Older consent forms may be out of date.",
      "HHS OCR guidance says a state Medicaid agency may use Part 2 records received under a valid treatment, payment and operations (TPO) consent to verify an exclusion. Send the consent or a clear explanation of its scope with the records.",
      "AUDIT TRAP: The DSS-8209 permission ends when the eligibility decision is complete. A new report at the next six-month renewal needs a new signed consent."
    ],
    "contacts": [
      "NC Medicaid Contact Center: 888-245-0179 (medicaid.ncdhhs.gov)"
    ],
    "sources": [
      "https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-2/subpart-C/section-2.31",
      "https://www.hhs.gov/sites/default/files/ocr-faq-part-2-sud.pdf",
      "https://www.hhs.gov/hipaa/for-professionals/regulatory-initiatives/fact-sheet-42-cfr-part-2-final-rule/index.html",
      "https://medicaid.ncdhhs.gov/media/16282/download?attachment"
    ],
    "confidence": "high",
    "verify": "Have a healthcare attorney review whether the draft DSS-8209 Section B wording meets all 42 CFR 2.31(a) elements, and check NC confidentiality law (G.S. 122C) consent requirements. G.S. 122C was not reviewed in this batch.",
    "basis": "required",
    "effective_date": "2026-02-16"
  },
  "step_28_sub_2": {
    "instructions": [
      "Do not draft a free-form letter. Plan to use NC's DSS-8209 Medical Report (Work Requirement Exclusions and Exemptions), and download the final version when NC Medicaid posts it.",
      "Have only an eligible signer complete Questions 3 to 5, for example LCMHC, LPC, social worker, psychologist, physician, NP, CADC or CSAC, and only with an established clinical relationship (Policy HR-1 Section 5.0).",
      "For SAIOP or SACOT participation, any program representative may complete Question 2 with the program name and the date participation began.",
      "Have the client sign Section B before submission, send the form to the client's local DSS, and file a copy in the record."
    ],
    "tips": [
      "In the draft form, a substance use disorder qualifies without current treatment, but stable recovery of 5 years or more does not. Answer from the documented assessment.",
      "The draft signer list leaves out LCAS, LCAS-A and certified peer support specialists for Questions 3 and 4. Consider commenting by Nov. 5, 2026, and assign a listed clinician for now.",
      "AUDIT TRAP: A DSS-8209 is a certification to the state. Each answer must match the diagnosis, assessment and service notes in the chart."
    ],
    "contacts": [
      "NC Medicaid public comments: medicaid.public.comment@dhhs.nc.gov (medicaid.ncdhhs.gov)",
      "NC Medicaid Contact Center: 888-245-0179 (medicaid.ncdhhs.gov)"
    ],
    "sources": [
      "https://medicaid.ncdhhs.gov/media/16282/download?attachment",
      "https://medicaid.ncdhhs.gov/media/16285/download?attachment",
      "https://medicaid.ncdhhs.gov/providers/medical-frailty-clinical-coverage-policy-and-comment-period"
    ],
    "confidence": "high",
    "verify": "Suggested wording: Prepare clinicians to complete NC's DSS-8209 Medical Report for SUD treatment participation, SUD, disabling mental disorder or medical frailty exclusions. The form is a draft and its revision label is inconsistent (REV. 08/2026 and 09/2026 DRAFT), so re-check the final version and signer list.",
    "basis": "expected",
    "effective_date": "2027-01-01"
  },
  "step_28_sub_3": {
    "instructions": [
      "Build an EHR report for each client showing program (8G, SAIOP, SACOT), admission date, last service date, discharge status and dates attended.",
      "Add a session-hours column calculated from the start and stop times in each service note, and confirm your 8G, SAIOP and SACOT note templates capture those times.",
      "Restrict the report to the compliance owner and clinical director, and release it only with a valid Part 2 consent or a written DSS request.",
      "Test the report against 5 charts before Jan. 1, 2027, and keep the test results."
    ],
    "tips": [
      "For the treatment-program exclusion, DSS-8209 Question 2 asks for the program name and start date, not monthly hours. Treatment attendance hours are not a listed qualifying activity toward the 80-hour test.",
      "AUDIT TRAP: Report totals must match the signed service notes and claims. A mismatch between a DSS-8209 and your billing is a program integrity risk."
    ],
    "contacts": [
      "NC Medicaid Contact Center: 888-245-0179 (medicaid.ncdhhs.gov)"
    ],
    "sources": [
      "https://medicaid.ncdhhs.gov/media/16282/download?attachment",
      "https://medicaid.ncdhhs.gov/beneficiaries/impact-hr-1-and-federal-changes-medicaid/work-and-community-engagement-requirement",
      "https://medicaid.ncdhhs.gov/8g-peer-support-services/download?attachment",
      "https://www.hhs.gov/sites/default/files/ocr-faq-part-2-sud.pdf"
    ],
    "confidence": "medium",
    "verify": "Not required by any source I found. Suggested wording: Set up EHR reports showing each client's program enrollment dates and active participation to support DSS-8209 Question 2 and DSS verification requests. NOT VERIFIED: whether peer support alone counts as a treatment and rehabilitation program; ask NC Medicaid. Also check the current CCP 8G (amended 2026), 8A-12 and 8A-13 documentation sections for required start and stop times.",
    "basis": "recommended",
    "effective_date": "2027-01-01"
  },
  "step_28_sub_4": {
    "instructions": [
      "Train all staff using NC Medicaid's Know What's Next toolkit and September 2026 webinar. Cover the Jan. 1, 2027 start, the $580 or 80-hour test, exclusions and six-month renewals.",
      "Script staff to say that DSS decides who must comply, then refer the client to local DSS (dhhs.nc.gov/localdss) or the NC Medicaid Contact Center.",
      "Tell clients who may qualify to collect proof and submit it to local DSS, and offer a DSS-8209 from an eligible clinician when appropriate.",
      "Record training dates and attendee sign-in sheets, and refresh the training when the final medical frailty policy posts."
    ],
    "tips": [
      "Staff should never tell a client they are exempt or will keep coverage. NC itself tells unsure beneficiaries to call DSS and not guess.",
      "NC law (G.S. 108A-55.7) requires applicants to show 3 consecutive compliant months before the month they apply, and 3 of the last 6 months at renewal. Refer applicants to DSS early."
    ],
    "contacts": [
      "NC Medicaid Contact Center: 888-245-0179 (medicaid.ncdhhs.gov)",
      "Local DSS directory: dhhs.nc.gov/localdss"
    ],
    "sources": [
      "https://medicaid.ncdhhs.gov/providers/federal-medicaid-changes-what-providers-need-know",
      "https://medicaid.ncdhhs.gov/beneficiaries/impact-hr-1-and-federal-changes-medicaid/work-and-community-engagement-requirement",
      "https://medicaid.ncdhhs.gov/medicaid-hr1-essentials-deck-speakers-notes/download?attachment",
      "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108A/GS_108A-55.7.html"
    ],
    "confidence": "high",
    "verify": "Not a legal duty. Good practice. Register staff for the NC Medicaid Back Porch Chat on Nov. 19, 2026 (noon to 1 p.m.) for updates.",
    "basis": "recommended",
    "effective_date": "2027-01-01"
  }
}
```

B) SOURCES

| Title | Publisher | URL | Date / version | Type |
|---|---|---|---|---|
| H.R. 1, 119th Congress (P.L. 119-21) | Congress.gov | congress.gov[congress.gov](https://www.congress.gov/bill/119th-congress/house-bill/1?share_frome=aipt) | Enacted July 4, 2025 | Primary |
| CMCS Informational Bulletin on P.L. 119-21 | CMS | CIB[medicaid.gov](https://www.medicaid.gov/federal-policy-guidance/downloads/cib11182025.pdf?share_frome=aipt) | Nov. 18, 2025 | Primary |
| SMD 26-001, six-month renewals | CMS | SMD 26-001[medicaid.gov](https://www.medicaid.gov/federal-policy-guidance/downloads/smd26001.pdf?share_frome=aipt) | 2026 | Primary |
| Working Families Tax Cut Legislation hub | CMS | medicaid.gov[medicaid.gov](https://www.medicaid.gov/resources-for-states/working-families-tax-cut-legislation?share_frome=aipt) | Accessed Oct. 2026 | Primary |
| Community Engagement page (CMS-2454-IFC) | CMS | medicaid.gov[medicaid.gov](https://www.medicaid.gov/resources-for-states/working-families-tax-cut-legislation/community-engagement?share_frome=aipt) | IFC published June 3, 2026 | Primary |
| Federal Medicaid Changes: What Providers Need to Know | NC Medicaid | NC Medicaid[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers/federal-medicaid-changes-what-providers-need-know?share_frome=aipt) | Modified Oct. 13, 2026 | Primary |
| Work and Community Engagement Requirement | NC Medicaid | NC Medicaid[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/beneficiaries/impact-hr-1-and-federal-changes-medicaid/work-and-community-engagement-requirement?share_frome=aipt) | Oct. 13, 2026 | Primary |
| Medical Frailty: Clinical Coverage Policy and Comment Period | NC Medicaid | NC Medicaid[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers/medical-frailty-clinical-coverage-policy-and-comment-period?share_frome=aipt) | Modified Oct. 14, 2026 | Primary |
| Draft H.R.1 Medical Frailty Exclusions, Policy No. HR-1 | NC Medicaid | [draft policy](https://medicaid.ncdhhs.gov/media/16285/download?attachment) | Draft, proposed effective Jan. 1, 2027 | Primary (draft) |
| Draft DSS-8209 Medical Report | NC DHHS | [DSS-8209](https://medicaid.ncdhhs.gov/media/16282/download?attachment) | REV. 08/2026 and 09/2026 DRAFT | Primary (draft) |
| Draft Medically Frail Code List | NC Medicaid | [code list](https://medicaid.ncdhhs.gov/media/16283/download?attachment) | Draft, 2026 | Primary (draft) |
| H.R. 1 Essentials deck, speaker's notes | NC Medicaid | speaker notes[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/medicaid-hr1-essentials-deck-speakers-notes/download?attachment=&share_frome=aipt) | 2026 | Primary |
| G.S. 108A-55.7 | NC General Assembly | ncleg.gov[ncleg.gov](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108A/GS_108A-55.7.html?share_frome=aipt) | S.L. 2026-1, effective Jan. 1, 2027 | Primary |
| NCDHHS comment letter on the CMS IFC | NCDHHS | ncdhhs.gov[ncdhhs.gov](https://www.ncdhhs.gov/north-carolina-dhhs-ifc-comment-letter/open?share_frome=aipt) | July 30, 2026 | Primary |
| CCP 8G Peer Support Services | NC Medicaid | 8G[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/8g-peer-support-services/download?attachment=&share_frome=aipt) | Posted Sept. 2026 | Primary |
| CCP 8A-12 | NC Medicaid | 8A-12[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/media/15767/download?share_frome=aipt) | 2026 | Primary |
| Verify Recipient Eligibility on NCTracks | NCTracks | NCTracks[nctracks.nc.gov](https://www.nctracks.nc.gov/content/public/providers/provider-communications/provider-announcements/Verify-Recipient-Eligibility-with-NCTracks-Call-Center.html?share_frome=aipt) | Aug. 12, 2014 | Primary (older) |
| Managed Care Claims Submission, Part 1 | NC Medicaid | fact sheet[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/managed-care-claims-submission-what-providers-need-know-part-1/open?share_frome=aipt) | Accessed 2026 | Primary |
| 10A NCAC 22J .0106 | NC OAH | rule[reports.oah.state.nc.us](http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2022%20-%20medical%20assistance%20eligibility/subchapter%20j/10a%20ncac%2022j%20.0106.pdf?share_frome=aipt) | Current | Primary |
| Medicaid Bulletin Digests | NC Medicaid | digests[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers/medicaid-bulletin/medicaid-bulletin-digests?share_frome=aipt) | Oct. 12, 2026 | Primary |
| Aug. 2013 Medicaid Bulletin (NCTracks email sign-up) | NC Medicaid | bulletin[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/documents/providers/bulletins/archives/0813bulletin/download?share_frome=aipt) | Aug. 2013 | Primary (older) |
| Vaya and Partners merger notice | NC Medicaid | notice[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/information-regarding-vaya-health-and-partners-health-management-merger/open?share_frome=aipt) | Effective Oct. 1, 2026 | Primary |
| Health Plans contacts | NC Medicaid | health plans[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/about-nc-medicaid/health-plans?share_frome=aipt) | Oct. 2026 | Primary |
| Provider News Service email sign-up | Alliance Health | Alliance[alliancehealthplan.org](https://www.alliancehealthplan.org/provider-updates/provider-news-service-email-sign-up/?share_frome=aipt) | Page dated Sept. 2, 2021 | Primary (Tailored Plan) |
| Provider Communications | Trillium Health Resources | Trillium[trilliumhealthresources.org](https://www.trilliumhealthresources.org/for-providers/provider-communications?share_frome=aipt) | Oct. 2026 | Primary (Tailored Plan) |
| Provider Communication Bulletins | Vaya Partners | Vaya Partners[providers.vayapartners.org](https://providers.vayapartners.org/bulletins/?share_frome=aipt) | Oct. 2026 | Primary (Tailored Plan) |
| 42 CFR 2.31 | eCFR | eCFR[ecfr.gov](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-2/subpart-C/section-2.31?share_frome=aipt) | Current | Primary |
| Part 2 records and community engagement exclusion FAQ | HHS OCR | OCR FAQ[hhs.gov](https://www.hhs.gov/sites/default/files/ocr-faq-part-2-sud.pdf?share_frome=aipt) | 2026, cites 91 FR 33348 | Primary |
| Fact Sheet: 42 CFR Part 2 Final Rule | HHS | HHS[hhs.gov](https://www.hhs.gov/hipaa/for-professionals/regulatory-initiatives/fact-sheet-42-cfr-part-2-final-rule/index.html?share_frome=aipt) | Feb. 8, 2024, updated Jan. 30, 2026 | Primary |
| NC awarded $213M Rural Health Transformation Program | NCDHHS | press release[ncdhhs.gov](https://www.ncdhhs.gov/news/press-releases/2025/12/29/north-carolina-awarded-213-million-rural-health-transformation-program-strategic-roadmap-and-federal?share_frome=aipt) | Dec. 29, 2025 | Primary |

C) CORRECTIONS

- **"Dec 2026 (six-month renewals)" is imprecise.** The statute applies to renewals scheduled on or after the first day of the first quarter after Dec. 31, 2026. CMS states this as renewals on or after Jan. 1, 2027 (SMD 26-001; CMS CIB). NC Medicaid also says Jan. 1, 2027.[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/beneficiaries/impact-hr-1-and-federal-changes-medicaid/work-and-community-engagement-requirement?share_frome=aipt)[medicaid.gov](https://www.medicaid.gov/federal-policy-guidance/downloads/cib11182025.pdf?share_frome=aipt)[medicaid.gov](https://www.medicaid.gov/federal-policy-guidance/downloads/smd26001.pdf?share_frome=aipt)
- **"Oct 2028 (cost-sharing)": the date is correct but the impact is overstated.** Section 71120 exempts behavioral health services, so cost sharing should not reach 8G, SAIOP or SACOT.[medicaid.gov](https://www.medicaid.gov/federal-policy-guidance/downloads/cib11182025.pdf?share_frome=aipt)
- **"Exemptions may cover people in SUD treatment..." is too tentative.** The statute excludes people in drug or alcohol treatment and rehabilitation programs and people with a substance use disorder or a disabling mental disorder. NC lists all of these as exclusions.[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/beneficiaries/impact-hr-1-and-federal-changes-medicaid/work-and-community-engagement-requirement?share_frome=aipt)
- **The NC draft also goes further than the app context.** A substance use disorder qualifies without current treatment, but stable recovery of 5 years or more does not ([DSS-8209 draft](https://medicaid.ncdhhs.gov/media/16282/download?attachment)).
- **"Once NC Medicaid sets its process" is outdated.** NC has published a draft process: Policy HR-1, the DSS-8209 and a code list. Comments are open through Nov. 5, 2026, and the final version is expected late Nov. or early Dec. 2026.[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers/medical-frailty-clinical-coverage-policy-and-comment-period?share_frome=aipt)
- **"Confirm with each Tailored Plan... how providers submit documentation" names the wrong body.** Providers send the DSS-8209, signed by both provider and client, to the client's county DSS, and DSS decides. Tailored Plan-eligible members are automatically Tier 1.[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers/medical-frailty-clinical-coverage-policy-and-comment-period?share_frome=aipt)
- **"Clinician-signed template letter" is the wrong format.** NC uses the standard DSS-8209 form. Its draft signer list does not include LCAS or certified peer support specialists, and Question 2 (treatment program participation) can be signed by any program representative ([DSS-8209 draft](https://medicaid.ncdhhs.gov/media/16282/download?attachment)).
- **"Check eligibility before every billing period" is too weak.** CCP 8G and 8A-12 require checking eligibility each time a service is rendered (CCP 8G; CCP 8A-12).[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/8g-peer-support-services/download?attachment=&share_frome=aipt)[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/media/15767/download?share_frome=aipt)
- **"Attendance hours" reports do not match what the exclusion needs.** The DSS-8209 asks for the program name and start date, and treatment hours are not a listed qualifying activity for the 80-hour test ([DSS-8209 draft](https://medicaid.ncdhhs.gov/media/16282/download?attachment); NC Medicaid).[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/beneficiaries/impact-hr-1-and-federal-changes-medicaid/work-and-community-engagement-requirement?share_frome=aipt)
- **The app context leaves out NC's own law.** G.S. 108A-55.7 (S.L. 2026-1), effective Jan. 1, 2027, requires 3 consecutive compliant months before an application and 3 of the last 6 months at redetermination.[ncleg.gov](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108A/GS_108A-55.7.html?share_frome=aipt)
- **"Each Tailored Plan" needs updating.** Vaya Health and Partners merged into Vaya Partners on Oct. 1, 2026, which leaves three Tailored Plan LME/MCOs.[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/information-regarding-vaya-health-and-partners-health-management-merger/open?share_frome=aipt)
- **"Jan 2027 (community engagement)" is the federal deadline, but NC may not meet it fully.** On July 30, 2026, NCDHHS told CMS that full implementation by Jan. 1, 2027 is unlikely. NC's public page still says Jan. 1, 2027.[ncdhhs.gov](https://www.ncdhhs.gov/north-carolina-dhhs-ifc-comment-letter/open?share_frome=aipt)
- **Status of each item, by source and date:**
  - Statute: P.L. 119-21, enacted July 4, 2025.
  - CMS: CIB of Nov. 18, 2025; SMD 26-001; and CMS-2454-IFC, published June 3, 2026.
  - NC announcements: provider and beneficiary pages dated Oct. 13–14, 2026.
  - NC drafts, not final: Policy HR-1, the DSS-8209 and the code list.
- **Confirmed as correct:** Oct. 1, 2026 for immigrant eligibility, and Jan. 1, 2027 for the retroactive coverage limits (one month for expansion adults, two months for others).[medicaid.gov](https://www.medicaid.gov/federal-policy-guidance/downloads/cib11182025.pdf?share_frome=aipt)

D) OPEN QUESTIONS

- **Final Policy HR-1, DSS-8209 and code list:** Will they add LCAS, LCAS-A or certified peer support specialists as signers, peer support (H0038), or mild SUD codes such as F10.10? Ask the NC Medicaid Contact Center (888-245-0179) or comment to medicaid.public.comment@dhhs.nc.gov by Nov. 5, 2026.[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers/medical-frailty-clinical-coverage-policy-and-comment-period?share_frome=aipt)
- **Peer support and the treatment-program exclusion:** Does 8G peer support alone count as a "drug or alcohol treatment and rehabilitation program"? Not verified; ask NC Medicaid.
- **Good-faith extension:** Has CMS approved a delay for NC? Not verified; watch the NC Medicaid provider page and CMS.
- **CCP 8A-13 eligibility wording:** Does SACOT's Section 2.1.1 match 8G and 8A-12? Not checked in this batch.
- **Billing limits:** Timely filing limits and state-funded service availability for each Tailored Plan and Standard Plan were not verified. Call Trillium Provider Support (1-855-250-1539), Vaya Partners ACCESS (1-866-990-9712) or Alliance (ProviderNetwork@alliancehealthplan.org).
- **Consent forms:** Does the DSS-8209 Section B wording meet all 42 CFR 2.31(a) elements and NC G.S. 122C confidentiality rules? A healthcare attorney should confirm.
- **Subscription links:** The NCTracks sign-up link location comes from a 2013 bulletin, and the Vaya Partners bulletin page has no visible sign-up link. Check the NCTracks Provider Communications page and call Vaya Partners ACCESS.