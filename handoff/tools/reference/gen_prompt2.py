import json
steps = json.load(open('missing.json'))
need = [s for s in steps if s['missing']]

MASTER = r'''You are a research analyst who specializes in North Carolina Medicaid behavioral health provider licensure, enrollment, and compliance. I am building a checklist app for a NEW provider standing up three North Carolina Medicaid services: CCP 8G (Peer Support Services), CCP 8A-12 (Substance Abuse Intensive Outpatient Program, SAIOP) and CCP 8A-13 (Substance Abuse Comprehensive Outpatient Treatment, SACOT). The checklist also has a phase for the federal H.R. 1 (Public Law 119-21, the 2025 budget reconciliation act) Medicaid changes. For each checklist task I give you, research and write practical, accurate, source-cited instructions that a first-time provider owner could follow.

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
If you are running low on space, finish the JSON for the tasks you have done, state which keys remain, and stop. Do not abbreviate or skip a key. Do not add commentary before part A.'''

PRE = r'''BATCH 0 - VERIFY THE FOUNDATIONS (run this first)
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
Also tell me whether these three services need Tailored Plan credentialing in addition to NCTracks enrollment, and in what order the steps normally happen.'''

PRE_HR1 = r'''BATCH 0B - VERIFY THE H.R. 1 FOUNDATIONS (run after Batch 0, before the H.R. 1 batches)
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
B. Which of the six areas above are legal requirements for providers, which are requirements for the state or members only (providers just need to adapt), and which are good practice?'''

def batch_block(batch_steps, n, hr1=False):
    lines = []
    keys = []
    for s in batch_steps:
        lines.append(f"{s['stepNumber']} - {s['title']}  ({s['phaseName']})")
        lines.append(f"  Applies to: {', '.join('CCP ' + x for x in s['services'])}")
        lines.append("  App context (may contain errors - verify, correct in the CORRECTIONS section):")
        lines.append(f"    Description: {s['description']}")
        lines.append(f"    Responsible: {s['responsible']} | Typical time: {s['timeWeeks']} | Cost shown: {s['costEstimate']}")
        lines.append(f"    Main resource: {s['resourceName']} ({s['resourceUrl']})")
        lines.append(f"    Depends on: {s['dependencies']}")
        lines.append("  Tasks to write instructions for:")
        for m in s['missing']:
            lines.append(f"    {m['key']} = {m['text']}")
            keys.append(m['key'])
        lines.append("")
    head = f"BATCH {n} - write entries for the {len(keys)} tasks below. Return the JSON keys in this exact order: {', '.join(keys)}.\n"
    if hr1:
        head += ("These are H.R. 1 tasks. In EACH entry add two more fields after verify: \"basis\" (one of: \"required\" = a provider legal or contract duty today; \"expected\" = NC has published or announced it will apply to providers; \"recommended\" = good practice only) and \"effective_date\" (the date it applies, or \"unknown\"). "
                 "If a task is not actually a provider obligation, say so in verify and suggest a better wording of the task in the verify field.\n")
    return head + "\n".join(lines).rstrip(), keys

# six batches of at most 15 tasks, grouped by step
batches, cur, cnt = [], [], 0
hr1_steps = [s for s in need if s['phase'] == 6]
need = [s for s in need if s['phase'] != 6]
for s in need:
    k = len(s['missing'])
    if cur and cnt + k > 15:
        batches.append(cur); cur, cnt = [], 0
    cur.append(s); cnt += k
if cur: batches.append(cur)
hr1_batches, cur, cnt = [], [], 0
for s in hr1_steps:
    k = len(s['missing'])
    if cur and cnt + k > 14:
        hr1_batches.append(cur); cur, cnt = [], 0
    cur.append(s); cnt += k
if cur: hr1_batches.append(cur)

out = []
out.append('# Perplexity research prompts: instructions for the 104 checklist tasks (79 original + 25 H.R. 1)\n')
out.append('''## How to use these prompts

1. **Mode.** Use Perplexity **Pro Search** or **Research (Deep Research)** with web sources on. Do not use the plain quick search.
2. **Master prompt.** Paste the master prompt below at the top of EVERY new thread, immediately followed by one batch. If Perplexity cuts the message off, create a Perplexity **Space**, paste the master prompt into the Space's custom instructions, and paste only the batch into each thread.
3. **Order.** Run **Batch 0 (verify the foundations)** first. If it finds that a policy number, fee or region assignment in my app is wrong, send me those corrections before continuing so the later batches are not built on a bad premise. Then run Batches 1 to 6 (the original 79 tasks), one new thread each. After that run **Batch 0B (verify the H.R. 1 foundations)**, then Batches 7 and 8 (the 25 H.R. 1 tasks). H.R. 1 rules and NC's implementation are still moving, so expect more `NOT VERIFIED` and `low` entries there, and rerun Batch 0B whenever NC Medicaid publishes new guidance.
4. **Check the output.** Each answer should start with a JSON block. Spot-check at least two sources per batch by opening the URLs. Anything marked NOT VERIFIED or confidence "low" needs a human (ideally your healthcare attorney or the agency) before it goes in the app.
5. **Bring it back.** Paste the JSON blocks (and the CORRECTIONS list) into this chat. I will validate them, drop the sources and flags into the data, and add them to the dashboard.

Each JSON entry has the same shape as the existing instructions in the app (`instructions`, `tips`, `contacts`), plus `sources`, `confidence` and `verify` so you can see where each fact came from. The H.R. 1 batches add `basis` (required, expected or recommended) and `effective_date`, and may suggest better wording for tasks that turn out not to be provider obligations.
''')
out.append('---\n\n## Master prompt (paste first, every thread)\n\n````text\n' + MASTER + '\n````\n')
out.append('---\n\n## Batch 0: verify the foundations (run first)\n\n````text\n' + PRE + '\n````\n')
for i, b in enumerate(batches, 1):
    text, keys = batch_block(b, i)
    steps_range = f"{b[0]['stepNumber']} to {b[-1]['stepNumber']}" if len(b) > 1 else b[0]['stepNumber']
    out.append(f'---\n\n## Batch {i}: {steps_range} ({len(keys)} tasks)\n\n````text\n{text}\n````\n')
n0 = len(batches)
out.append('---\n\n## Batch 0B: verify the H.R. 1 foundations (run before the H.R. 1 batches)\n\n````text\n' + PRE_HR1 + '\n````\n')
for j, b in enumerate(hr1_batches, 1):
    text, keys = batch_block(b, n0 + j, hr1=True)
    steps_range = f"{b[0]['stepNumber']} to {b[-1]['stepNumber']}" if len(b) > 1 else b[0]['stepNumber']
    out.append(f'---\n\n## Batch {n0 + j} (H.R. 1): {steps_range} ({len(keys)} tasks)\n\n````text\n{text}\n````\n')
open('perplexity_prompts.md', 'w').write('\n'.join(out))
print('batches:', [(i + 1, sum(len(s["missing"]) for s in b)) for i, b in enumerate(batches + hr1_batches)])
print('master chars:', len(MASTER), '| total tasks:', sum(len(s['missing']) for s in need + hr1_steps))
