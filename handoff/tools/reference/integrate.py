import json, re, sys

R = '/tmp/claude-0/-home-user-hello-world/91141d82-7be3-5ffc-bd0c-f501091745a6/scratchpad/research/'
P = '/home/user/hello-world/nc_medicaid_bh_dashboard.html'
s = open(P).read()


def once(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:100])
    s = s.replace(old, new)


# ------------------------------------------------------------------ 1. researched entries
entries = {}
entries.update(json.load(open(R + 'batches_1_5.json')))
entries.update(json.load(open(R + 'batches_6_8.json')))

# one extra entry derived from the H.R. 1 foundations answer (Batch 0B): comment period on NC draft frailty list
entries['step_28_sub_5'] = {
    'instructions': [
        'Open the NC Medicaid proposed policies page and download the draft medical frailty code list, draft policy HR-1 and the draft DSS-8209 attestation. Comments are open Oct 6 to Nov 5, 2026.',
        'Check which of your service and diagnosis codes appear. The draft Tier 1 list includes H0015 (SAIOP), H2035 (SACOT) and F1x.20 dependence codes. It does not include H0038 (peer support), F1x.21 in-remission codes or F10.10.',
        'Send written comments by Nov 5, 2026 on any code that would miss your clients, using the method shown on the page.',
        'Code diagnoses and services precisely from now on, because NC flags medical frailty from 12 months of claims.'
    ],
    'tips': [
        'AUDIT TRAP: Vague or inaccurate diagnosis and service coding can cost a client a medical frailty exemption, because NC uses claims data to find medically frail members.',
        'These are drafts. Final versions are expected in late November or early December 2026, so recheck the page before building workflows around them.'
    ],
    'contacts': ['NC Medicaid Contact Center: 888-245-0179 (https://medicaid.ncdhhs.gov/providers/federal-medicaid-changes-what-providers-need-know)'],
    'sources': [
        'https://medicaid.ncdhhs.gov/meetings-notices/proposed-medicaid-policies',
        'https://medicaid.ncdhhs.gov/media/16283/download?attachment',
        'https://medicaid.ncdhhs.gov/providers/medical-frailty-clinical-coverage-policy-and-comment-period'
    ],
    'confidence': 'medium',
    'verify': 'Based on the H.R. 1 foundations research only. Confirm the comment method, the deadline and the code list on the NC Medicaid page before relying on it.',
    'basis': 'recommended',
    'effective_date': '2026-11-05 (comment deadline)'
}

urls = []
for v in entries.values():
    for u in v['sources']:
        if u not in urls:
            urls.append(u)
idx = {u: i for i, u in enumerate(urls)}


def jsq(x):
    return json.dumps(x, ensure_ascii=False).replace('</', '<\\/')


lines = []
for k, v in entries.items():
    parts = [
        f'        instructions: {jsq(v["instructions"])}',
        f'        tips: {jsq(v["tips"])}',
        f'        contacts: {jsq(v["contacts"])}',
        f'        sources: {jsq([idx[u] for u in v["sources"]])}',
        f'        confidence: {jsq(v["confidence"])}',
        f'        verify: {jsq(v["verify"])}',
    ]
    if 'basis' in v:
        parts.append(f'        basis: {jsq(v["basis"])}')
        parts.append(f'        effectiveDate: {jsq(v["effective_date"])}')
    lines.append(f"      '{k}': {{\n" + ',\n'.join(parts) + '\n      }')

block = ("\n\n      // Researched instructions (Oct 2026). Each entry carries its sources, a confidence rating and what to verify.\n"
         + ',\n'.join(lines))

end = s.index('    const STORAGE_KEY')
close = s.rindex('\n    };', 0, end)
s = s[:close] + ',' + block + s[close:]
# the preceding entry ended with "}" followed by newline: fix "}\n," -> "},"
s = s.replace("      }\n,\n\n      // Researched instructions", "      },\n\n      // Researched instructions")

src_js = ('    // URLs cited by the researched instructions; entries refer to them by position\n'
          '    const DETAIL_SOURCES = ' + jsq(urls) + ';\n\n')
once('    const SUBTASK_DETAILS_MAP = {', src_js + '    const SUBTASK_DETAILS_MAP = {')

# ------------------------------------------------------------------ 2. step text corrections
def step_bounds(n):
    base = s.index('const MASTER_STEPS')  # region data above also has "id: 1..6" at this indent
    a = s.index(f'\n        id: {n},\n', base)
    nxt = s.find(f'\n        id: {n + 1},\n', a)
    b = nxt if nxt != -1 else s.index('\n    ];', a)
    return a, b


def jsstr(t):
    return "'" + t.replace('\\', '\\\\').replace("'", "\\'") + "'"


def set_field(n, field, value):
    global s
    a, b = step_bounds(n)
    blk = s[a:b]
    pat = re.compile(r"(\n        " + field + r": )'(?:[^'\\]|\\.)*'(,?)")
    assert len(pat.findall(blk)) == 1, (n, field)
    blk = pat.sub(lambda m: m.group(1) + jsstr(value) + m.group(2), blk)
    s = s[:a] + blk + s[b:]


def set_services(n, services):
    global s
    a, b = step_bounds(n)
    blk = s[a:b]
    pat = re.compile(r"(\n        services: )\[[^\]]*\]")
    assert len(pat.findall(blk)) == 1
    blk = pat.sub(lambda m: m.group(1) + '[' + ', '.join(jsstr(x) for x in services) + ']', blk)
    s = s[:a] + blk + s[b:]


def get_subs(n):
    a, b = step_bounds(n)
    blk = s[a:b]
    m = re.search(r"\n        subtasks: \[\n(.*?)\n        \]", blk, re.S)
    items = re.findall(r"'((?:[^'\\]|\\.)*)'", m.group(1))
    return [i.replace("\\'", "'").replace('\\\\', '\\') for i in items]


def put_subs(n, items):
    global s
    a, b = step_bounds(n)
    blk = s[a:b]
    pat = re.compile(r"(\n        subtasks: \[\n)(.*?)(\n        \])", re.S)
    body = ',\n'.join('          ' + jsstr(x) for x in items)
    blk = pat.sub(lambda m: m.group(1) + body + m.group(3), blk, count=1)
    s = s[:a] + blk + s[b:]


def set_sub(n, i, text):
    items = get_subs(n)
    items[i] = text
    put_subs(n, items)


def set_fee(n, fees):
    global s
    a, b = step_bounds(n)
    blk = s[a:b]
    pat = re.compile(r"(\n        statutoryFees: )\[.*\](,)")
    assert len(pat.findall(blk)) == 1, n
    blk = pat.sub(lambda m: m.group(1) + fees + m.group(2), blk)
    s = s[:a] + blk + s[b:]


# Step 4
set_field(4, 'description', 'Secure commercial day or outpatient premises sized for the client census. Get written zoning approval for an outpatient substance use day program; DHSR asks for the original zoning letter with the application. DHSR lists Group B Business Occupancy for adult SAIOP and SACOT, and adolescent day programs cannot be in a Business Occupancy. A peer-support-only site may not trigger DHSR zoning paperwork, so confirm with your plan.')
set_field(4, 'costEstimate', 'Varies by lease. Local zoning letter fees vary by city or county (Durham charges $28 to $58).')
set_fee(4, "[{ label: 'Local zoning letter (varies by jurisdiction)', min: 28, max: 200 }]")
set_field(4, 'resourceName', 'County and city planning offices (the NCACC link lists counties only)')
# Step 5
set_field(5, 'description', 'Bind commercial general liability, professional liability and workers compensation coverage. Limits come from your LME/MCO contracts (for example Alliance asks for $1M per occurrence and $3M aggregate), not from the DHSR application, so get each plan insurance requirements in writing.')
set_field(5, 'costEstimate', '$1,500 – $4,500 / year (estimate, not verified)')
set_sub(5, 3, 'Ensure certificates show your agency as the named insured and the LME/MCO as certificate holder (additional insured if the plan requires it), with primary and non-contributory wording where available')
# Step 6
set_field(6, 'description', 'Open a dedicated commercial bank account in the exact legal name of the entity for Medicaid electronic fund transfers (EFT). NCTracks takes EFT details keyed into the enrollment application; a voided check or bank letter is mainly requested by LME/MCOs.')
set_field(6, 'costEstimate', '$0 – $100 initial deposit (estimate, not verified)')
set_sub(6, 0, 'Establish a business checking account in the exact legal entity name and keep a voided check for LME/MCO EFT forms')
set_sub(6, 1, 'Obtain a bank letter verifying routing and account numbers for LME/MCO EFT forms (NCTracks takes EFT details online)')
# Step 7
set_field(7, 'description', 'Appoint the Facility Director named on the DHSR application and a Clinical Director. SAIOP and SACOT programs must be directed by an LCAS or CCS (on site at least 50% of SAIOP hours and 90% of SACOT hours, 10A NCAC 27G .4402 and .4502). Qualified Professional standards (27G .0104) apply to peer support program supervision and direct care staff.')
set_sub(7, 1, 'Designate the Facility Director named on the DHSR application and delegate management authority in writing (the license is issued to the entity, not the director)')
set_sub(7, 2, 'Appoint a Clinical Director who is an LCAS or CCS for SAIOP and SACOT, or a full-time QP for peer support (10A NCAC 27G .0104)')
# Step 8
set_field(8, 'title', 'LME/MCO Network Need Inquiry (a 27G .0406 Letter of Support is for residential facilities)')
set_field(8, 'description', 'Ask each Tailored Plan that covers your county whether it has a network need for your services. DHSR does not require an LME/MCO Letter of Support (10A NCAC 27G .0406) for day programs; that rule applies to 24-hour residential facilities. Peer support has been a closed-network service since July 7, 2026, so plans may decline new applicants. Vaya Health and Partners merged on Oct 1, 2026.')
set_field(8, 'timeWeeks', 'Varies by plan (Alliance answers provider applications in 5 business days)')
set_field(8, 'resourceName', 'NC DHHS LME/MCO directory')
set_field(8, 'resourceUrl', 'https://www.ncdhhs.gov/providers/lme-mco-directory')
set_sub(8, 0, 'Submit a program summary and county location to the Tailored Plan that covers your county and ask whether it is accepting new providers')
set_sub(8, 1, 'List the services you plan to offer (Peer Support, SAIOP, SACOT) and ask whether each is a current network need in your county')
set_sub(8, 2, 'Get the plan written network-need or contract-status response (a .0406 Letter of Support is only for residential facilities)')
# Step 9
set_field(9, 'description', 'Draft the policy and procedure manual from the DHSR Policy and Procedure Workbook, cross-referenced to 10A NCAC 27G, the DHHS Records Management and Documentation Manual (RMDM, effective July 8, 2025), 42 CFR Part 2 (compliance date Feb 16, 2026) and IRIS incident reporting. DHSR says not to send policies with the application; your consultant reviews them later.')
set_field(9, 'resourceName', 'DHSR Policy and Procedure Workbook')
set_field(9, 'resourceUrl', 'https://info.ncdhhs.gov/dhsr/mhlcs/pdf/PolicyProcedure-Workbook.pdf')
set_sub(9, 0, 'Draft governance, client rights and grievance procedures (10A NCAC 27G .0201, 27D and 27E)')
set_sub(9, 2, 'Incorporate 42 CFR Part 2 consent, notice and disclosure rules (compliance date Feb 16, 2026)')
# Step 10
set_field(10, 'description', 'Recruit and hire staff who meet the rules and the CCPs: an LCAS or CCS clinical supervisor (a Clinical Supervisor Intern is also allowed) for SAIOP and SACOT, Licensed or Certified Clinical Staff for groups, and NC Certified Peer Support Specialists (CPSS) supervised by a QP at 1:8.')
set_field(10, 'resourceName', 'NCASPPB (LCAS and CCS credentials) and the NC CPSS Program')
set_field(10, 'resourceUrl', 'https://www.ncsappb.org/credentialing/licensed-clinical-addiction-specialist/')
# Step 11
set_field(11, 'description', 'Perform pre-employment checks: the NC Health Care Personnel Registry (HCPR) under N.C.G.S. § 131E-256 and 10A NCAC 27G .0202(b)(4), state and national criminal history checks (G.S. 122C-80), and exclusion screening against the OIG LEIE, SAM.gov and the NC Medicaid exclusion list.')
# Step 12
set_field(12, 'description', 'Verify each Peer Support staff member holds an active NC CPSS certification from the NC Peer Support Specialist Certification Program (pss.unc.edu). Certification requires 18 months in recovery before training. CCP 8G (amended Sept 1, 2026) requires a roster of CPSS staff with certification and hire dates.')
set_sub(12, 1, 'File proof of training: Foundations of Peer Support (60 hours on Track A) or the approved 50-hour course (Track B), plus the 20-hour prerequisite training (3 hours of ethics and 17 related hours)')
# Step 13
set_field(13, 'description', 'Schedule and complete the local fire safety inspection and any county health department sanitation review. Fire and safety compliance is annual for licensure (10A NCAC 27G .0402(d)(3)); DHSR requires a sanitation report for day programs only if you serve food.')
set_field(13, 'costEstimate', '$75 – $250 inspection fees (estimate; varies by jurisdiction, not verified)')
set_sub(13, 1, 'Get local health department approval of water and sewage (10A NCAC 27G .0303) and a sanitation report if you serve any food')
set_sub(13, 2, 'Ask the fire code official for the maximum occupant load of each room and post signs if the official requires them')
# Step 14
set_field(14, 'dependencies', 'Steps 4 and 13 (zoning and fire approvals); keep Steps 9, 10 and 11 ready for your consultant')
set_sub(14, 1, 'Attach the original zoning approval and the fire marshal report, plus a sanitation report if you serve food (an LME/MCO letter applies only to residential facilities)')
set_sub(14, 2, 'Cross-walk the policy manual to 10A NCAC 27G with the DHSR workbook and keep it ready for your consultant (do not enclose it with the application)')
set_sub(14, 3, 'Prepare the staff roster with verified credentials for the consultant review, and enclose the $265 fee with the application')
# Step 15
set_field(15, 'description', 'Host the DHSR Licensure and Training consultant for the on-site walkthrough of the furnished site and review of personnel records, restrictive intervention training and policies. DHSR gives six months from first contact to meet all requirements.')
set_field(15, 'timeWeeks', 'Up to 6 months from first contact with the consultant')
set_sub(15, 2, 'Demonstrate knowledge of client rights and restrictive intervention policies (10A NCAC 27D and 27E .0101 to .0108; 27G .0209 is the medication rule)')
# Step 16
set_field(16, 'description', 'Return the Plan of Correction within 10 days of receiving any Statement of Deficiencies (confirm the deadline in your letter) and finish corrections inside the window counted from the exit date (23, 30, 45 or 60 days by finding type). DHSR may take up to 3 weeks to issue the license after compliance.')
# Step 17
set_field(17, 'description', 'Complete the NC HealthConnex participation agreement (a PDF emailed to hiea@nc.gov, not signed online; allow 6 to 8 weeks) and set up an EHR that can send HL7 version 2.0 or higher messages. Records covered by 42 CFR Part 2 are exempt from submission under G.S. 90-414.4(c).')
set_field(17, 'timeWeeks', '6–8 weeks')
set_field(17, 'dependencies', 'Step 1 (Entity formed); the DHSR license is not required first')
set_sub(17, 0, 'Complete and email the NC HealthConnex participation agreement to HIEA (it is not signed online)')
set_sub(17, 1, 'Select an EHR that can send HL7 v2.0 or higher messages to NC HealthConnex and can filter 42 CFR Part 2 records')
set_sub(17, 2, 'File written confirmation of your connection status from HIEA (no source found requires proof before billing; confirm with your plans)')
# Step 18
set_field(18, 'description', 'Submit the Organization Enrollment Application in NCTracks. The Office Administrator must be an owner or managing employee with an NCID. Select taxonomy 251S00000X and each service you offer. Finish the NC Medicaid New Provider Training within 15 calendar days of submitting.')
set_field(18, 'dependencies', 'Step 3 (NPI) and, for SAIOP and SACOT, Step 16 (DHSR license)')
set_sub(18, 2, 'Select taxonomy 251S00000X and add each service (Peer Support, SAIOP, SACOT) as the Provider Permission Matrix lists them')
set_sub(18, 3, 'Sign the W-9 attestation, enter EFT details online, and upload only the documents the application asks for (NCTracks verifies the DHSR license)')
# Step 19
set_services(19, ['8G', '8A-12', '8A-13'])
set_field(19, 'description', 'Complete fingerprint-based criminal history checks for owners with 5% or more ownership (managing employees are not required to be fingerprinted) under N.C.G.S. § 108C-3, and pass the NCTracks site visit. The Provider Permission Matrix lists peer support, SAIOP and SACOT as high risk. Per a Sept 14, 2026 NC Medicaid bulletin, the site visit and fingerprinting are waived only if you hold active national accreditation for the same location and service.')
set_sub(19, 0, 'Schedule LiveScan fingerprinting at an approved site after the NCTracks notice arrives, before the deadline in the notice')
set_sub(19, 1, 'Upload the NCTracks-generated fingerprint Release of Information forms in the portal (mailed forms are not processed)')
# Step 20
set_field(20, 'description', 'Check the enrollment effective date on the approval letter. If clinicians are enrolled as individual providers (for example an LCAS), the Office Administrator of each individual record affiliates them to your organization; CCS and QP are not NCTracks provider types.')
set_sub(20, 1, 'Have each individually enrolled clinician Office Administrator submit a Manage Change Request to affiliate to your organization NPI (confirm with NC Medicaid whether agency staff must be enrolled)')
# Step 21
set_field(21, 'description', 'Apply to and contract with each Tailored Plan that covers your county: Alliance, Trillium or Vaya Partners (Vaya Health and Partners merged on Oct 1, 2026). NCTracks enrollment comes first. Peer support is a closed-network service, so a plan may decline new applicants unless it has a posted need.')
set_field(21, 'resourceName', 'NC DHHS LME/MCO directory')
set_field(21, 'resourceUrl', 'https://www.ncdhhs.gov/providers/lme-mco-directory')
set_field(21, 'dependencies', 'Step 18 (NCTracks enrollment active) and, for SAIOP and SACOT, Step 16 (DHSR license)')
set_sub(21, 1, 'Submit each plan clinician roster or enrollment form with NCTracks records (no plan page found asks for CAQH IDs; confirm with each plan)')
# Step 22
set_field(22, 'description', 'Configure EHR clinical note templates that meet the DHHS Records Management and Documentation Manual (RMDM), including service start and end times, 15-minute units (H0038) for Peer Support, and same-episode service exclusion checks.')
set_field(22, 'costEstimate', '$150 – $400 / clinician / month (estimate, not verified)')
set_field(22, 'resourceName', 'EHR vendor (healthit.gov is general guidance, not a vendor list)')
set_sub(22, 1, 'Build billing rules that block SAIOP and SACOT in the same episode of care (except admission and discharge days) and block Peer Support at the same time of day as SAIOP or SACOT')
set_sub(22, 2, 'Configure Peer Support units: 15-minute H0038 units, 24 unmanaged units per episode, then 176 units per 60 days and no more than 88 per 30 days (CCP 8G); do not hard-code daily or weekly caps unless a plan requires them')
# Step 23
set_field(23, 'title', '24/7 Crisis Response Protocol & Clinical Training')
set_field(23, 'description', 'Train all staff on the 24-hour, seven-day crisis response required by CCP 8A-12 and CCP 8A-13 (section 6.1), delivered in person, by telehealth or by phone based on client need. Train on client rights and alternatives to restrictive interventions (10A NCAC 27E .0107; personnel training under 27G .0202(g)).')
set_field(23, 'resourceName', 'DMH/DD/SUS approved de-escalation curricula')
set_field(23, 'resourceUrl', 'https://www.ncdhhs.gov/divisions/mental-health-developmental-disabilities-and-substance-use-services/involuntary-commitment/training-requirements-use-non-restrictive-and-restrictive-intervention-strategies')
set_sub(23, 0, 'Publish a rotating 24/7 clinical crisis on-call schedule with LCAS or CCS backup')
# Step 24
set_field(24, 'description', 'Standardize intake: a comprehensive clinical assessment completed before service, ASAM level-of-care determination, a Service Order signed by a physician, physician assistant, nurse practitioner or licensed psychologist (confirm the signer list and term in each CCP; CCP 8G differs), and tracking of any authorization periods your plan requires. CCP 8A-12 and 8A-13 require no prior approval; CCP 8G authorizes up to 176 units per 60 days.')
# Step 25
set_field(25, 'timeWeeks', 'Ongoing (accreditation deadline runs from enrollment; see the instructions)')
set_field(25, 'costEstimate', '$8,000 – $14,000 (estimate, not verified; CARF says the fee depends on surveyors, survey days and travel)')

# ----- Phase 6: verified dates and facts (Batch 0B) and the researched task wording
set_field(26, 'description', 'H.R. 1 (Public Law 119-21, signed July 4, 2025) changes Medicaid eligibility, renewals, cost-sharing and program-integrity rules and created the Rural Health Transformation Program. Most of it binds the state and members, so providers mainly adapt. Verified dates: Oct 1, 2026 (many noncitizens lose Medicaid); Jan 1, 2027 (work requirement, six-month renewals for expansion adults, retroactive coverage cut to 1 month for expansion adults); July 1, 2027 (NC raises copays to the federal maximum); Oct 1, 2028 (federal cost-sharing, which excludes mental health and SUD services). NC has told CMS it is unlikely to fully implement the work requirement by Jan 1, 2027.')
set_sub(26, 0, 'Review H.R. 1 provisions and NC Medicaid H.R. 1 provider guidance that affect client eligibility, billing and documentation')
set_sub(26, 1, 'Assign H.R. 1 monitoring to your existing compliance officer, with a backup, and record it in governing body minutes')
set_field(27, 'description', 'Most expansion adults move to six-month eligibility renewals starting Jan 1, 2027, and many noncitizens lose coverage Oct 1, 2026, so more clients will lose coverage. NC Medicaid policy requires you to verify eligibility each time a service is rendered. Build intake and billing controls for that, and help clients keep their coverage without giving legal advice.')
set_sub(27, 0, 'Verify Medicaid eligibility and health plan at intake and on every date of service')
set_sub(27, 3, 'Track monthly Medicaid coverage lapses and their reasons for quality improvement and governing body review')
set_field(28, 'description', 'The work requirement (80 hours a month for expansion adults aged 19 to 64, from Jan 1, 2027) has exemptions, but they are not automatic. People with a substance use disorder or a disabling mental disorder count as medically frail, and people in a qualifying treatment program are excluded, but stable recovery of 5+ years is excluded from the SUD category, the condition must significantly impair compliance, and the program exclusion covers only nonprofit or public programs, so a for-profit SAIOP or SACOT may not qualify. NC has draft policy HR-1, a clinician-signed DSS-8209 attestation and a medically frail code list open for comment Oct 6 to Nov 5, 2026. Providers document; county DSS decides.')
set_sub(28, 0, 'Confirm NC Medicaid final medical frailty policy and DSS-8209 process; providers document, and county DSS decides')
set_sub(28, 2, 'Prepare clinicians to complete the NC DSS-8209 Medical Report for SUD treatment participation, SUD, disabling mental disorder or medical frailty exclusions')
set_sub(28, 3, 'Set up EHR reports showing each client program enrollment dates and active participation to support DSS-8209 and DSS verification requests')
put_subs(28, get_subs(28) + ['Review the NC draft medical frailty code list and send comments by Nov 5, 2026 (H0015 and H2035 are on it; H0038 is not)'])
set_field(29, 'description', 'Retroactive coverage drops to 1 month for expansion adults and 2 months for others for applications on or after Jan 1, 2027. Many noncitizens lose coverage Oct 1, 2026. Federal cost-sharing starts Oct 1, 2028 and excludes mental health and SUD services; NC raises its copays to the federal maximum on July 1, 2027. Update intake, financial-responsibility and billing rules so you do not deliver services you cannot get paid for or collect amounts you are not allowed to charge.')
set_sub(29, 1, 'Write a financial responsibility policy with client notices (including the Good Faith Estimate for uninsured and self-pay clients) and a sliding-fee option for people who lose or do not qualify for Medicaid')
set_sub(29, 2, 'Confirm with each Tailored Plan whether NC copays (from July 1, 2027) apply to peer support, SAIOP and SACOT; federal cost-sharing from Oct 1, 2028 excludes mental health and SUD services')
set_field(30, 'description', 'H.R. 1 adds death-record checks of provider enrollment (a state duty from Jan 1, 2028) and limits provider taxes and state directed payments, which can pressure Medicaid funding. Providers have no new filing, but monthly exclusion screening and accurate NCTracks records are already required. Plan for rate or volume changes.')
set_sub(30, 0, 'Add a monthly screen of every owner, manager and rendering provider against the OIG exclusion list, SAM.gov and the NC Medicaid exclusion list (a participation agreement requirement)')
set_field(31, 'title', 'Rural Health Transformation (NC ROOTS) Funding (optional)')
set_field(31, 'description', 'H.R. 1 funds $10 billion a year for FY2026 to FY2030 for state rural health plans; NC runs it as NC ROOTS (year 1 award about $213 million) through five regional hub leads. This is optional funding, not a provider obligation. The Rural Health Innovation Fund lists behavioral health providers as eligible, with the full application due Nov 16, 2026 (RHIF@nc.gov, 919-754-6733). CMS limits direct payments to providers to 15% of a state award.')

open(P, 'w').write(s)
print('entries added:', len(entries), '| unique sources:', len(urls))
