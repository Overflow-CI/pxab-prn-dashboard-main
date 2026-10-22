import json

steps = json.load(open('missing.json'))
counties = json.load(open('counties.json'))

# ---------------------------------------------------------------- source pack
# (id, name to give the source, url, what it is used for)
A = [
 ('S01', 'CCP 8G Peer Support Services', 'https://medicaid.ncdhhs.gov/8g-peer-support-services/open', 'Peer support: staffing ratios, units, authorization, telehealth, enrollment requirements'),
 ('S02', 'NC Medicaid bulletin - amendment to CCP 8G (Oct 2, 2026)', 'https://medicaid.ncdhhs.gov/blog/2026/10/02/amendment-clinical-coverage-policy-8g-peer-support-services', 'What changed in 8G effective Sept 1, 2026'),
 ('S03', 'CCP 8A-12 SAIOP', 'https://medicaid.ncdhhs.gov/media/15767/download', 'SAIOP: hours, billing, staffing, prior approval, accreditation'),
 ('S04', 'CCP 8A-13 SACOT', 'https://medicaid.ncdhhs.gov/media/15769/download', 'SACOT: hours, billing code, ratios, prior approval, accreditation'),
 ('S05', 'NC Medicaid behavioral health CCP updates (Jan 7, 2026)', 'https://medicaid.ncdhhs.gov/blog/2026/01/07/behavioral-health-clinical-coverage-policy-updates', 'When 8A-12 and 8A-13 became stand-alone policies'),
 ('S06', '10A NCAC 27G .0201 Governing Body Policies', 'http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/10a%20ncac%2027g%20.0201.pdf', 'Governing body and policy requirements'),
 ('S07', '10A NCAC 27G .4501 (SAIOP/SACOT facility rules)', 'http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/10a%20ncac%2027g%20.4501.html', 'Facility licensure rules for the day programs'),
 ('S08', 'DHSR MHLCS - establishing a facility', 'https://info.ncdhhs.gov/dhsr/mhlcs/establish.html', 'Licensure process, order of steps, time limits'),
 ('S09', 'DHSR initial licensure application packet (MHL5001)', 'https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf?ver=2', 'Application contents, exhibits, fees'),
 ('S10', 'DHHS Records Management and Documentation Manual - page', 'https://www.ncdhhs.gov/divisions/mental-health-developmental-disabilities-and-substance-use-services/records-management-and-documentation-manual', 'Service note and record rules (replaces APSM 45-2 references)'),
 ('S11', 'DHHS Records Management and Documentation Manual (July 2025)', 'https://www.ncdhhs.gov/rmdmjuly-2025/download', 'Full manual text'),
 ('S12', 'NCTracks provider recredentialing', 'https://www.nctracks.nc.gov/content/public/providers/provider-recredentialing.html', '5-year revalidation'),
 ('S13', 'NCTracks changes to re-credentialing and reverification (2018)', 'https://www.nctracks.nc.gov/content/public/providers/provider-communications/2018-announcements/Changes-to-Re-credentialing-and-Reverification-Process.html', 'Notice schedule, suspension and termination'),
 ('S14', 'NC Medicaid provider enrollment and recredentialing', 'https://medicaid.ncdhhs.gov/providers/provider-enrollment/provider-enrollment-recredentialing', 'Enrollment overview'),
 ('S15', 'NCTracks behavioral health provider enrollment FAQs', 'https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-Behavioral-Health-Provider-Enrollment.html', 'Taxonomy, credentialing split, enrollment questions (undated)'),
 ('S16', 'NCTracks 2026 federal application fee notice', 'https://www.nctracks.nc.gov/content/public/providers/provider-communications/2025-Announcements/Federal-Provider-Enrollment-Application-Fee-Increase-for-Year-2026.html', 'Federal fee amount for 2026'),
 ('S17', 'NCTracks state and federal fee amounts by year (spreadsheet)', 'https://www.nctracks.nc.gov/content/dam/jcr:5088259c-ab17-4c01-bf6d-c64786be1da4/State%20and%20Federal%20Fee%20Amounts%20by%20Year.xlsx', 'Fee history'),
 ('S18', 'NCTracks FAQs - application fee', 'https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-ACA-application-fee.html', 'When the fee applies'),
 ('S19', 'NCTracks FAQs - fingerprinting', 'https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-fingerprinting.html', 'Who is fingerprinted, how, cost'),
 ('S20', 'SBI non-criminal justice access agreement (SB-41)', 'https://info.ncdhhs.gov/dhsr/abcms/pdf/Non-Criminal-Justice-Access-Agreement-Form_SB-41.pdf', 'Background check fees and process'),
 ('S21', 'NC Medicaid bulletin - recent behavioral health enrollment updates (Sept 14, 2026)', 'https://medicaid.ncdhhs.gov/blog/2026/09/14/recent-behavioral-health-enrollment-updates-organizations', 'High-risk screening and waiver'),
 ('S22', 'NC Medicaid bulletin - post-enrollment national accreditation update (Apr 16, 2026)', 'https://medicaid.ncdhhs.gov/blog/2026/04/16/post-enrollment-national-accreditation-update', 'Accreditation deadlines and bodies'),
 ('S23', 'NC Medicaid provider enrollment 2026 summer and fall series 1 (PowerPoint)', 'https://medicaid.ncdhhs.gov/provider-enrollment-2026-summer-and-fall-series-1-powerpoint/open', 'Credentialing committee, enrollment changes'),
 ('S24', 'NCTracks Provider Permission Matrix (Aug 16, 2026) (spreadsheet)', 'https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx', 'Which taxonomy, license and screening each service needs'),
 ('S25', 'NC Secretary of State business registration fees', 'https://www.sosnc.gov/fees/by_title/_Business_Registration/', 'Filing fees'),
 ('S26', 'G.S. 143B-1209.20 (SBI check fee)', 'https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_143B/GS_143B-1209.20.html', 'State criminal check fee cap'),
 ('S27', 'G.S. 122C-80 (criminal history checks)', 'https://ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_122C/GS_122C-80.html', 'Who must be checked'),
]
B = [
 ('S30', 'SL 2026-1 (HB 696)', 'https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-1.pdf', 'Medicaid changes law: open and closed networks, credentialing plan'),
 ('S31', 'SL 2026-41 (SB 257)', 'https://www3.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-41.pdf', 'Closed-network authority cited by Alliance'),
 ('S32', 'NC Medicaid Plans - get answers (plans by county)', 'https://www.ncmedicaidplans.gov/en/get-answers', 'Which Tailored Plan covers which county'),
 ('S33', 'NCDHHS LME/MCO directory', 'https://www.ncdhhs.gov/providers/lme-mco-directory', 'Plan counties and contacts'),
 ('S34', 'NC Medicaid health plans', 'https://medicaid.ncdhhs.gov/about-nc-medicaid/health-plans', 'Plan provider-network contacts'),
 ('S35', 'NC Medicaid - contracting with Tailored Plans', 'https://medicaid.ncdhhs.gov/contracting-tailored-plans/download', 'Whether providers must contract with every plan'),
 ('S36', 'Vaya and Partners merger provider FAQ', 'https://www.vayahealth.com/wp-content/uploads/2026/07/Merger_Provider_FAQ.pdf', 'Merger effective date and provider impact'),
 ('S37', 'Partners - Vaya and Partners announce merger', 'https://providers.partnersbhm.org/vaya-health-and-partners-health-management-announce-merger/', 'Merger announcement'),
 ('S38', 'Alliance Health - become a provider', 'https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/', 'Alliance enrollment and network rules'),
 ('S39', 'Trillium Provider Manual (older edition)', 'https://www.trilliumhealthresources.org/sites/default/files/docs/Provider-documents/Provider-Manual/Trillium-Provider-Manual.pdf', 'Trillium credentialing and contracting'),
 ('S40', 'NCDHHS - NC ROOTS hub leads', 'https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-organizations-orchestrating-transformation-sustainability-roots-hub-leads', 'Hub leads by region'),
 ('S41', 'NCDHHS press release - NC ROOTS hub leads (May 1, 2026)', 'https://www.ncdhhs.gov/news/press-releases/2026/05/01/ncdhhs-selects-nc-roots-hub-leads-strengthen-rural-health-care-across-north-carolina', 'What ROOTS is and who runs it'),
 ('S42', 'NCDHHS Rural Health Transformation Program (parent page) - link derived, may need correcting', 'https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program', 'Funding opportunities and deadlines'),
 ('S43', 'Public Law 119-21 (H.R. 1) - link not yet checked', 'https://www.congress.gov/119/plaws/publ21/PLAW-119publ21.pdf', 'Statute text (Medicaid sections and the Rural Health Transformation Program)'),
 ('S44', '42 U.S.C. 1396a (Cornell LII)', 'https://www.law.cornell.edu/uscode/text/42/1396a', 'State plan law as amended by H.R. 1'),
 ('S45', 'NC legislative deck on H.R. 1', 'https://webservices.ncleg.gov/ViewDocSiteFile/104990', 'What NC says is in and out of scope'),
 ('S46', 'CMS fact sheet - community engagement interim final rule', 'https://www.cms.gov/newsroom/fact-sheets/medicaid-community-engagement-requirement-certain-individuals-interim-final-rule-comment-period-cms', 'Federal rule summary and exemptions'),
 ('S47', 'Federal Register 2026-11094 (CMS-2454-IFC) - short link, may need the PDF instead', 'https://www.federalregister.gov/d/2026-11094', 'Interim final rule text'),
 ('S48', 'Medicaid.gov - community engagement (H.R. 1)', 'https://www.medicaid.gov/resources-for-states/working-families-tax-cut-legislation/community-engagement', 'CMS guidance bulletin'),
 ('S49', 'NC Medicaid - work and community engagement requirement', 'https://medicaid.ncdhhs.gov/beneficiaries/impact-hr-1-and-federal-changes-medicaid/work-and-community-engagement-requirement', 'NC start date, exemptions, member steps'),
 ('S50', 'NC Medicaid is changing', 'https://medicaid.ncdhhs.gov/beneficiaries/medicaid-is-changing', 'Retroactive coverage and renewal changes'),
 ('S51', 'NC Medicaid - prior approval and due process (providers)', 'https://medicaid.ncdhhs.gov/providers/programs-and-services/prior-approval-and-due-process', 'Verifying eligibility on the date of service'),
 ('S52', 'HHS fact sheet - 42 CFR Part 2 final rule', 'https://www.hhs.gov/hipaa/for-professionals/regulatory-initiatives/fact-sheet-42-cfr-part-2-final-rule/index.html', 'Consent and disclosure of SUD records'),
 ('S53', 'HHS announcement - Part 2 civil enforcement', 'https://www.hhs.gov/press-room/hhs-announce-civil-enforcement-program-sud-patient-records.html', 'Enforcement start date'),
]

# which sources are most likely to answer each step (shown in each batch)
LIKELY = {
 4: 'None in the pack (local zoning and ADA). Add your county or city planning page and the ADA standards page, or expect NOT IN SOURCES.',
 5: 'None in the pack. Add NC Department of Insurance pages, or expect NOT IN SOURCES. Check S01, S03 and S04 for any insurance requirement.',
 6: 'S19 (EFT and enrollment context). Otherwise none: add the NCTracks EFT / banking page.',
 7: 'S06, S07, S08. Add 10A NCAC 27G .0104 (definitions) if not in the notebook.',
 8: 'S08, S35, S38, S39, S30',
 9: 'S06, S07, S10, S11, S52, S01, S03, S04',
 10: 'S01, S03, S04, S02',
 11: 'S26, S27, S19, S20',
 12: 'S01, S02 (CPSS roster and certification). Add the NC peer support certification program page.',
 13: 'S08, S09. Add the NC State Fire Marshal and local health department pages.',
 14: 'S08, S09, S24',
 15: 'S08, S09, S07',
 16: 'S08, S09',
 17: 'None in the pack. Add the NC HealthConnex participation pages.',
 18: 'S12, S14, S15, S16, S17, S18, S21, S23, S24',
 19: 'S19, S20, S21, S24',
 20: 'S12, S13, S14, S15, S23',
 21: 'S30, S31, S32, S33, S34, S35, S36, S37, S38, S39',
 22: 'S01, S03, S04, S10, S11, S02',
 23: 'S03, S04, S01, S07',
 24: 'S01, S03, S04, S10, S11, S52',
 25: 'S22, S21, S03, S04, S01, S12, S13, S24',
 26: 'S43, S44, S45, S48, S49, S50',
 27: 'S50, S49, S51, S45',
 28: 'S43, S44, S46, S47, S48, S49, S52, S53',
 29: 'S50, S49, S45, S43',
 30: 'S43, S45, S12, S13, S23',
 31: 'S40, S41, S42, S43',
}
NOTEBOOK = {sid: 'A' for sid in range(4, 26)}
NOTEBOOK.update({21: 'B', 26: 'B', 27: 'B', 28: 'B', 29: 'B', 30: 'B', 31: 'B'})

MASTER = r'''You are a research assistant for a new North Carolina Medicaid behavioral health provider standing up CCP 8G (Peer Support Services), CCP 8A-12 (SAIOP) and CCP 8A-13 (SACOT). It is October 2026. The notebook may also cover the federal H.R. 1 (Public Law 119-21) Medicaid changes.

GROUNDING RULES
- Use ONLY the sources in this notebook. Never use memory, outside knowledge or web search to state a requirement, fee, date, form, deadline, rule or policy number, phone number, email or URL.
- If the sources do not cover something, write "NOT IN SOURCES" and name the document I should add. Never guess and never fill a gap.
- If sources conflict, give both and say which is newer. Prefer primary sources (policy, rule, statute, agency notice) over FAQs and plan or vendor pages. Give a source's date or revision when it shows one.
- Treat any "app context" I paste as unverified claims to check, not facts. List the wrong or outdated ones under CORRECTIONS.
- For H.R. 1 items, separate statute, federal rule or guidance, and what North Carolina has announced, with dates. Do not present a proposal or plan as settled.
- Do not give legal advice.
- Sources are named S01, S02 and so on. Cite by those names and by section or page.

TASK ENTRIES
Each entry has these fields:
- instructions: 3 to 5 imperative steps in order, each under 40 words and supported by a source. A step that is general good practice and not in the sources must start with "GENERAL:" and be a plain administrative action. Never put a legal requirement, fee, deadline, form or contact behind "GENERAL:".
- tips: 2 to 3 items. Start a compliance risk with "AUDIT TRAP:".
- contacts: 1 to 3 items as "Office: phone (website)", only if that exact phone number or website appears in a source. Otherwise [].
- evidence: 1 to 4 items like "S03 section 5.1: \"exact quote of 25 words or fewer\"". No quote means no claim.
- confidence: "high" (a primary source states it), "medium", or "low" (inferred or secondary source only).
- verify: what a person must double-check, or "".
If the sources do not cover a task at all, return empty arrays, confidence "low" and verify "NOT IN SOURCES: add <document>".

OUTPUT, in this order
A) One valid JSON object in a json code block, keyed by the task keys I give (for example "step_4_sub_0"), every key in the order given, no extra keys. Plain text only inside strings, one line each, double quotes escaped, and no citation markers or footnote numbers inside the JSON.
B) CORRECTIONS: bullets of wrong claim -> correct value -> source and section.
C) MISSING SOURCES: documents to add, with the topic each would answer.
If you run out of space, finish the JSON for the keys you completed, list the keys remaining, and stop. Do not add commentary before part A.'''

AUDIT = r'''SOURCE AUDIT
List every source in this notebook as a table: name | publisher | date, version or "last updated" shown in the document | what it covers | problems (empty, cut off, looks like a navigation page, or older than 2026). Then list the topics from this list that no source covers at all: local zoning and ADA, insurance requirements, banking and EFT setup, NC HealthConnex participation, peer support specialist certification, fire marshal inspection, Tailored Plan credentialing forms.'''

VERIFY = r'''VERIFY THE CORRECTIONS ALREADY IN THE APP
Another research tool suggested the corrections below and I applied them. Check each one against this notebook only. Reply with a table: # | claim | CONFIRMED / CONTRADICTED / NOT IN SOURCES | what the source says (quote of 25 words or fewer) | source and section. After the table, list anything in the sources that conflicts with a claim or that I should know and did not ask about.

1. CCP 8G: a Qualified Professional supervises no more than 8 CPSS (ratio 1:8).
2. CCP 8G: CPSS to beneficiary ratio is 1:15 for individual and 1:12 for group.
3. CCP 8G was amended effective Sept 1, 2026: unmanaged units of 24 per episode; authorization up to 176 units per 60 days and no more than 88 per 30 days; telehealth and telephonic delivery limited to about 10% of service time; a CPSS roster is required; notes show start and end times.
4. CCP 8A-12 (SAIOP) and 8A-13 (SACOT) became stand-alone policies effective Jan 1, 2026.
5. CCP 8A-12: HCPCS H0015, one event per day, at least 3 hours; adult program runs 9 to 19 hours per week; clinical supervisor may be an LCAS, CCS or CSI.
6. CCP 8A-12 and 8A-13: Medicaid does not require prior approval (section 5.1). There is no 30-day or 60-day pass-through period.
7. CCP 8A-13: code H2035 (not H2036), one unit equals one hour, at least 4 hours per service day, program operates at least 20 hours per week, adults 18 and older.
8. CCP 8A-13: staffing is at least 1 clinical staff for every 10 or fewer beneficiaries in group counseling (section 6.2). No separate QP ratio is stated.
9. SAIOP is licensed under 10A NCAC 27G .4400 and SACOT under 27G .4500; 27G .0201 is "Governing Body Policies".
10. "APSM 45-2" does not appear in any source. The current documentation rules are in the Records Management and Documentation Manual (RMDM), effective July 8, 2025.
11. DHSR non-residential facilities (including SAIOP and SACOT) pay a $265 base fee with no per-capacity fee; licenses renew yearly.
12. NCTracks charges a $100 NC application fee plus a federal fee of $750 for calendar year 2026 ($709 was 2024). The fee applies at initial enrollment, re-enrollment, new owner or site, and revalidation.
13. NC Secretary of State: LLC or business corporation articles $125; nonprofit articles $60; Certificate of Existence $15.
14. NCTracks revalidation is every 5 years: first notice 70 days out, reminders at 50, 20 and 5 days; a missed deadline means suspension, then termination after 50 days of suspension.
15. Taxonomy 251S00000X is high categorical risk: site visit, fingerprinting and the federal fee apply. Per the Sept 14, 2026 bulletin, the site visit and fingerprinting are waived only with active national accreditation for the same location and service.
16. Accreditation (COA, The Joint Commission or CARF) is required within 1 year of enrollment for peer support. For SAIOP and SACOT the policies say 1 year and the Provider Permission Matrix says 3 years. Which source is newer, and what does the April 2026 notice say?
17. The Provider Permission Matrix (Aug 16, 2026) does not require a DHSR license for peer support but does for SAIOP and SACOT.
18. A provider needs both NCTracks enrollment and Tailored Plan credentialing and contracting; NCTracks comes first; providers may contract with as many Tailored Plans as they choose. One NCTracks FAQ says LME/MCOs no longer perform credentialing: how do the sources reconcile that?
19. SL 2026-1 (HB 696) became law Apr 30, 2026. Section 3C.12 covers open and closed networks; section 3C.13 moves the prepayment review threshold from 70% to 80%; section 3C.14 requires a Medicaid credentialing and integrity plan (report due Oct 1, 2026; implementation no earlier than July 1, 2027).
20. Tailored Plans are assigned by county, not by Medicaid Regions 1 to 6. Vaya Health and Partners merged on Oct 1, 2026 (Vaya Partners). Alliance covers 7 counties.
21. NC ROOTS (the Rural Health Transformation program) hub leads: Impact Health (Region 1), Trillium (Regions 2 and 5), Vaya (Region 3), UNC Health (Region 4), Access East (Region 6). It is a regional grant and coordination network, not part of licensure or enrollment.
22. SBI state criminal check fee is capped at $14 by G.S. 143B-1209.20. What do the sources say about the cost of fingerprint-based national checks for NCTracks and for staff?'''

COUNTY = r'''COUNTY TO TAILORED PLAN MAP
Using only the NC Medicaid Plans, NCDHHS LME/MCO directory, NC Medicaid health plans and Vaya/Partners merger sources, tell me which Tailored Plan covers each North Carolina county.
Return (A) one valid JSON object in a json code block where each key is a county name exactly as written in my list below and each value is the plan name exactly as the sources write it. Use "UNASSIGNED" if a source lists the county but names no plan. Use "NOT IN SOURCES" if no source mentions the county. If two sources disagree, use the value "CONFLICT: <plan from source A> vs <plan from source B>" and name the sources. No other keys.
Then (B) a table of each plan: plan name | counties covered (count) | provider-network phone and email | the source and section. Only give contacts that appear in a source. Note any difference between the NCDHHS directory and the NC Medicaid Plans page, and say which is newer.
My county list (100): ''' + ', '.join(counties) + '.'

HR1 = r'''H.R. 1 FOUNDATIONS
Check each claim against this notebook only. Reply with a table: # | claim | CONFIRMED / CONTRADICTED / NOT IN SOURCES | status (statute, federal rule or guidance, NC announcement, or proposal) | what the source says (quote of 25 words or fewer) | source and section. Then answer the questions at the end.

1. H.R. 1 is Public Law 119-21, the 2025 budget reconciliation act, signed July 4, 2025.
2. Community engagement: adult expansion enrollees must show about 80 hours a month of work, community service, a work program or education; states must start by Jan 1, 2027; the Secretary may grant a good-faith exemption that ends no later than Dec 31, 2028. Who is covered, and how is compliance verified and how often?
3. Exemptions: people with a substance use disorder, people in a drug addiction or alcoholic treatment and rehabilitation program, people with a disabling mental disorder, and medically frail people. Quote the statutory language and the CMS rule or guidance.
4. CMS interim final rule CMS-2454-IFC: issued June 1, 2026; published June 3, 2026; effective July 31, 2026. What does it say about notices (30 days?) and about provider attestation or documentation?
5. NC: requirement starts Jan 1, 2027; members must meet it in 3 of the 6 months before recertification; NC calls the medically frail pathway undefined; NC has not announced a good-faith exemption request.
6. Eligibility redeterminations every 6 months for expansion adults starting with renewals on or after Dec 31, 2026.
7. Retroactive coverage drops from 3 months to 1 month for most expansion-age adults on Jan 1, 2027.
8. Cost-sharing for expansion adults above 100% of the federal poverty level starts Oct 1, 2028. Which services are excluded? NC's legislative deck lists copayments as "not currently in scope".
9. Changes to eligibility for certain lawfully present immigrants start Oct 1, 2026.
10. Provider screening: required checks against death records, by what date, and whether the state or the provider must do them.
11. Provider tax limits and state directed payment limits: what do the sources say about effects on NC Medicaid or Tailored Plan payments to behavioral health providers?
12. Rural Health Transformation Program: $50 billion over fiscal years 2026 to 2030. NC's award, the name NC ROOTS, who runs it, whether providers can apply for sub-awards, deadlines.
13. 42 CFR Part 2: compliance and enforcement date (Feb 16, 2026?) and what consent rules apply when an SUD provider shares attendance or exemption information with NC Medicaid or a Tailored Plan.

Questions:
A. Which H.R. 1 provisions create real to-do items for a NEW NC outpatient behavioral health provider offering peer support, SAIOP and SACOT, beyond these: impact review, eligibility checks and renewals, community engagement documentation, coverage and cost-sharing billing controls, program integrity and funding risk, and rural health transformation funding? Give a prioritized list with sources and dates, or say NOT IN SOURCES.
B. Which of those areas are legal requirements on providers, which apply only to the state or members, and which are good practice?'''

def batch_text(group, label, hr1=False):
    keys, lines = [], []
    nb = sorted({NOTEBOOK[s['id']] for s in group})
    for s in group:
        lines.append(f"{s['stepNumber']} - {s['title']}  ({s['phaseName']})")
        lines.append(f"  Applies to: {', '.join('CCP ' + x for x in s['services'])}")
        lines.append(f"  Most likely sources: {LIKELY[s['id']]}")
        lines.append("  App context (unverified claims, check them):")
        lines.append(f"    Description: {s['description']}")
        lines.append(f"    Responsible: {s['responsible']} | Typical time: {s['timeWeeks']} | Cost shown: {s['costEstimate']}")
        lines.append(f"    Main resource the app links to: {s['resourceName']} ({s['resourceUrl']}) - add it as a source if the answer needs it")
        lines.append(f"    Depends on: {s['dependencies']}")
        lines.append("  Tasks:")
        for m in s['missing']:
            lines.append(f"    {m['key']} = {m['text']}")
            keys.append(m['key'])
        lines.append("")
    head = f"{label}: write entries for the {len(keys)} tasks below, using only this notebook. Return the JSON keys in this exact order: {', '.join(keys)}.\n"
    if hr1:
        head += ('These are H.R. 1 tasks. In EACH entry add two fields after verify: "basis" (one of "required" = a provider legal or contract duty today; "expected" = NC has published or announced it will apply to providers; "recommended" = good practice only) and "effective_date" (the date it applies, or "unknown"). If a task is not really a provider obligation, say so in verify and suggest better wording for the task.\n')
    return head + '\n'.join(lines).rstrip(), keys, nb

def chunk(seq, limit):
    out, cur, n = [], [], 0
    for s in seq:
        k = len(s['missing'])
        if cur and n + k > limit:
            out.append(cur); cur, n = [], 0
        cur.append(s); n += k
    if cur: out.append(cur)
    return out

need = [s for s in steps if s['missing']]
A_steps = [s for s in need if NOTEBOOK[s['id']] == 'A']
B_plan = [s for s in need if s['id'] == 21]
B_hr1 = [s for s in need if s['phase'] == 6]

batches = []
for g in chunk(A_steps, 10): batches.append((g, False))
for g in chunk(B_plan, 10): batches.append((g, False))
for g in chunk(B_hr1, 10): batches.append((g, True))

def src_table(rows):
    t = ['| ID | Name to give the source | Link | Used for |', '|---|---|---|---|']
    for sid, name, url, use in rows:
        t.append(f'| {sid} | {name} | {url} | {use} |')
    return '\n'.join(t)

def url_block(rows):
    return '\n'.join(u for _, _, u, _ in rows)

out = []
out.append('# NotebookLM research kit: instructions for the 104 checklist tasks\n')
out.append('''This kit replaces the Perplexity prompts. It assumes **Google NotebookLM** (the Gemini-powered notebook that answers from sources you add). If you meant a different Google product, tell me and I will adjust.

## How NotebookLM is different from Perplexity (and why the prompts changed)

- **It only knows what is in the notebook.** It does not search the web to answer. That is the main advantage: an answer is tied to a passage in a document you can open, so it cannot invent a fee or a phone number the way a web-search tool can. The cost is that you must load the right documents first.
- So the kit has three parts: a **source pack** to load, a **set of chat instructions** that forces it to stay inside the sources and quote them, and **prompts** to run in order.
- Anything the sources do not cover comes back as `NOT IN SOURCES`, with the name of the document to add. That is a feature. Add the document and re-ask.
- Practical steps that are not in any source (for example "open a business bank account") are allowed only if labeled `GENERAL:`, so I can show sourced and general steps differently in the app.
- Check the current limits on your account: NotebookLM caps the number of sources per notebook (about 50 on the free plan at the time I last knew; check yours) and the size of each source. The pack is split into **two notebooks** of 27 and 24 sources to stay under that.

## Run order

1. **Build Notebook A and Notebook B** from the source pack below.
2. In each notebook open **Configure chat**, choose a custom conversational style, and paste the **chat instructions**. If your version limits the length, paste it as the first message in each new chat instead.
3. Run the **source audit** in each notebook. Fix empty or broken sources (see the tips under the source pack) before going on.
4. Run **Prompt V: verify the corrections already in the app** (Notebook A for items 1 to 19; the Tailored Plan and ROOTS items 20 and 21 in Notebook B). This is the most important step: I applied corrections from another tool that I could not check myself, and this checks them against the primary documents.
5. Run **Prompt C: county to Tailored Plan map** in Notebook B. It fixes the region-based plan map that the app still gets wrong.
6. Run **Prompt H: H.R. 1 foundations** in Notebook B.
7. Run the **task batches**, one new chat per batch, in the order shown. Notebook letter is in each heading.
8. Paste every JSON block (and the CORRECTIONS and MISSING SOURCES lists) back to me. NotebookLM often puts numbered citation chips inside its answer; if some land inside the JSON just paste it anyway, I will strip them. I will validate the JSON, load it into the dashboard, keep `GENERAL:` steps and the evidence quotes, and rerun the tests.

If an answer is cut off, reply: "Continue from <next key>, same format."
''')
out.append('---\n\n## Source pack\n')
out.append('**Naming matters.** Start each source name with its ID (for example "S03 CCP 8A-12 SAIOP"). You can rename a source in NotebookLM. The prompts and the evidence quotes refer to sources by ID.\n')
out.append('**Tips for adding sources**\n\n- Use **Add source, Website**. NotebookLM imports only that single page, not the pages it links to. Some sites import as an empty or partial page; if the source audit shows that, open the page, print it to PDF (or download the PDF), and upload the PDF.\n- The two **spreadsheets** (S17, S24) may not import. Open them in Google Sheets and download as PDF, then upload the PDF, or copy the relevant rows into a Google Doc.\n- Some links came from another tool\'s answer and I have not opened them. Three are flagged in their name: S42 (derived address), S43 (Public Law link not checked) and S47 (short link). If one fails, search the title on the agency site.\n- If your NotebookLM has **Discover sources** or deep research, you can use it to find extra documents, but add only official government or agency pages.\n')
out.append('### Notebook A: services, licensure, enrollment and fees (S01 to S27)\n\n' + src_table(A) + '\n\nOne link per line, in case your version accepts several at once:\n\n````text\n' + url_block(A) + '\n````\n')
out.append('### Notebook B: Tailored Plans, H.R. 1 and rural funding (S30 to S53)\n\n' + src_table(B) + '\n\nOne link per line:\n\n````text\n' + url_block(B) + '\n````\n')
out.append('### Documents the pack does not have yet\n\nThese topics have no source in the pack, so those tasks will mostly come back `NOT IN SOURCES` until you add them. Add the NC agency page for each and re-run the affected batch:\n\n- Local zoning and ADA requirements (your county or city planning page; the app links https://www.ncacc.org/county-websites/)\n- Insurance requirements (NC Department of Insurance, https://www.ncdoi.gov/)\n- Banking and NCTracks EFT setup\n- NC HealthConnex participation\n- NC peer support specialist certification\n- NC State Fire Marshal and local health inspection\n- 10A NCAC 27G .0104 (definitions, including Qualified Professional)\n')
out.append('---\n\n## Chat instructions (paste into Configure chat, in both notebooks)\n\n````text\n' + MASTER + '\n````\n')
out.append('---\n\n## Prompt S: source audit (run first, in each notebook)\n\n````text\n' + AUDIT + '\n````\n')
out.append('---\n\n## Prompt V: verify the corrections already in the app\n\nRun in Notebook A. Items 20 and 21 need Notebook B, so run them there as a second message (copy those two lines).\n\n````text\n' + VERIFY + '\n````\n')
out.append('---\n\n## Prompt C: county to Tailored Plan map (Notebook B)\n\n````text\n' + COUNTY + '\n````\n')
out.append('---\n\n## Prompt H: H.R. 1 foundations (Notebook B)\n\n````text\n' + HR1 + '\n````\n')
for i, (g, hr1) in enumerate(batches, 1):
    label = f'BATCH {i}' + (' (H.R. 1)' if hr1 else '')
    text, keys, nb = batch_text(g, label, hr1)
    nums = [x['stepNumber'].replace('Step ', '') for x in g]
    rng = ('Steps ' + ', '.join(nums)) if len(nums) > 1 else ('Step ' + nums[0])
    out.append(f"---\n\n## Batch {i}{' (H.R. 1)' if hr1 else ''}: {rng} ({len(keys)} tasks) - Notebook {'/'.join(nb)}\n\n````text\n{text}\n````\n")
open('notebooklm_research_kit.md', 'w').write('\n'.join(out))
print('batches:', [(i + 1, sum(len(s['missing']) for s in g), 'HR1' if h else '') for i, (g, h) in enumerate(batches)])
print('A sources:', len(A), 'B sources:', len(B), '| master chars:', len(MASTER), '| tasks:', sum(len(s['missing']) for g, _ in batches for s in g))
