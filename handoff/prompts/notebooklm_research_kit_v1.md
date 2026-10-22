# NotebookLM research kit: instructions for the 104 checklist tasks

This kit replaces the Perplexity prompts. It assumes **Google NotebookLM** (the Gemini-powered notebook that answers from sources you add). If you meant a different Google product, tell me and I will adjust.

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

---

## Source pack

**Naming matters.** Start each source name with its ID (for example "S03 CCP 8A-12 SAIOP"). You can rename a source in NotebookLM. The prompts and the evidence quotes refer to sources by ID.

**Tips for adding sources**

- Use **Add source, Website**. NotebookLM imports only that single page, not the pages it links to. Some sites import as an empty or partial page; if the source audit shows that, open the page, print it to PDF (or download the PDF), and upload the PDF.
- The two **spreadsheets** (S17, S24) may not import. Open them in Google Sheets and download as PDF, then upload the PDF, or copy the relevant rows into a Google Doc.
- Some links came from another tool's answer and I have not opened them. Three are flagged in their name: S42 (derived address), S43 (Public Law link not checked) and S47 (short link). If one fails, search the title on the agency site.
- If your NotebookLM has **Discover sources** or deep research, you can use it to find extra documents, but add only official government or agency pages.

### Notebook A: services, licensure, enrollment and fees (S01 to S27)

| ID | Name to give the source | Link | Used for |
|---|---|---|---|
| S01 | CCP 8G Peer Support Services | https://medicaid.ncdhhs.gov/8g-peer-support-services/open | Peer support: staffing ratios, units, authorization, telehealth, enrollment requirements |
| S02 | NC Medicaid bulletin - amendment to CCP 8G (Oct 2, 2026) | https://medicaid.ncdhhs.gov/blog/2026/10/02/amendment-clinical-coverage-policy-8g-peer-support-services | What changed in 8G effective Sept 1, 2026 |
| S03 | CCP 8A-12 SAIOP | https://medicaid.ncdhhs.gov/media/15767/download | SAIOP: hours, billing, staffing, prior approval, accreditation |
| S04 | CCP 8A-13 SACOT | https://medicaid.ncdhhs.gov/media/15769/download | SACOT: hours, billing code, ratios, prior approval, accreditation |
| S05 | NC Medicaid behavioral health CCP updates (Jan 7, 2026) | https://medicaid.ncdhhs.gov/blog/2026/01/07/behavioral-health-clinical-coverage-policy-updates | When 8A-12 and 8A-13 became stand-alone policies |
| S06 | 10A NCAC 27G .0201 Governing Body Policies | http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/10a%20ncac%2027g%20.0201.pdf | Governing body and policy requirements |
| S07 | 10A NCAC 27G .4501 (SAIOP/SACOT facility rules) | http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/10a%20ncac%2027g%20.4501.html | Facility licensure rules for the day programs |
| S08 | DHSR MHLCS - establishing a facility | https://info.ncdhhs.gov/dhsr/mhlcs/establish.html | Licensure process, order of steps, time limits |
| S09 | DHSR initial licensure application packet (MHL5001) | https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf?ver=2 | Application contents, exhibits, fees |
| S10 | DHHS Records Management and Documentation Manual - page | https://www.ncdhhs.gov/divisions/mental-health-developmental-disabilities-and-substance-use-services/records-management-and-documentation-manual | Service note and record rules (replaces APSM 45-2 references) |
| S11 | DHHS Records Management and Documentation Manual (July 2025) | https://www.ncdhhs.gov/rmdmjuly-2025/download | Full manual text |
| S12 | NCTracks provider recredentialing | https://www.nctracks.nc.gov/content/public/providers/provider-recredentialing.html | 5-year revalidation |
| S13 | NCTracks changes to re-credentialing and reverification (2018) | https://www.nctracks.nc.gov/content/public/providers/provider-communications/2018-announcements/Changes-to-Re-credentialing-and-Reverification-Process.html | Notice schedule, suspension and termination |
| S14 | NC Medicaid provider enrollment and recredentialing | https://medicaid.ncdhhs.gov/providers/provider-enrollment/provider-enrollment-recredentialing | Enrollment overview |
| S15 | NCTracks behavioral health provider enrollment FAQs | https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-Behavioral-Health-Provider-Enrollment.html | Taxonomy, credentialing split, enrollment questions (undated) |
| S16 | NCTracks 2026 federal application fee notice | https://www.nctracks.nc.gov/content/public/providers/provider-communications/2025-Announcements/Federal-Provider-Enrollment-Application-Fee-Increase-for-Year-2026.html | Federal fee amount for 2026 |
| S17 | NCTracks state and federal fee amounts by year (spreadsheet) | https://www.nctracks.nc.gov/content/dam/jcr:5088259c-ab17-4c01-bf6d-c64786be1da4/State%20and%20Federal%20Fee%20Amounts%20by%20Year.xlsx | Fee history |
| S18 | NCTracks FAQs - application fee | https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-ACA-application-fee.html | When the fee applies |
| S19 | NCTracks FAQs - fingerprinting | https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-fingerprinting.html | Who is fingerprinted, how, cost |
| S20 | SBI non-criminal justice access agreement (SB-41) | https://info.ncdhhs.gov/dhsr/abcms/pdf/Non-Criminal-Justice-Access-Agreement-Form_SB-41.pdf | Background check fees and process |
| S21 | NC Medicaid bulletin - recent behavioral health enrollment updates (Sept 14, 2026) | https://medicaid.ncdhhs.gov/blog/2026/09/14/recent-behavioral-health-enrollment-updates-organizations | High-risk screening and waiver |
| S22 | NC Medicaid bulletin - post-enrollment national accreditation update (Apr 16, 2026) | https://medicaid.ncdhhs.gov/blog/2026/04/16/post-enrollment-national-accreditation-update | Accreditation deadlines and bodies |
| S23 | NC Medicaid provider enrollment 2026 summer and fall series 1 (PowerPoint) | https://medicaid.ncdhhs.gov/provider-enrollment-2026-summer-and-fall-series-1-powerpoint/open | Credentialing committee, enrollment changes |
| S24 | NCTracks Provider Permission Matrix (Aug 16, 2026) (spreadsheet) | https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx | Which taxonomy, license and screening each service needs |
| S25 | NC Secretary of State business registration fees | https://www.sosnc.gov/fees/by_title/_Business_Registration/ | Filing fees |
| S26 | G.S. 143B-1209.20 (SBI check fee) | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_143B/GS_143B-1209.20.html | State criminal check fee cap |
| S27 | G.S. 122C-80 (criminal history checks) | https://ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_122C/GS_122C-80.html | Who must be checked |

One link per line, in case your version accepts several at once:

````text
https://medicaid.ncdhhs.gov/8g-peer-support-services/open
https://medicaid.ncdhhs.gov/blog/2026/10/02/amendment-clinical-coverage-policy-8g-peer-support-services
https://medicaid.ncdhhs.gov/media/15767/download
https://medicaid.ncdhhs.gov/media/15769/download
https://medicaid.ncdhhs.gov/blog/2026/01/07/behavioral-health-clinical-coverage-policy-updates
http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/10a%20ncac%2027g%20.0201.pdf
http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/10a%20ncac%2027g%20.4501.html
https://info.ncdhhs.gov/dhsr/mhlcs/establish.html
https://info.ncdhhs.gov/dhsr/mhlcs/pdf/mhiapp.pdf?ver=2
https://www.ncdhhs.gov/divisions/mental-health-developmental-disabilities-and-substance-use-services/records-management-and-documentation-manual
https://www.ncdhhs.gov/rmdmjuly-2025/download
https://www.nctracks.nc.gov/content/public/providers/provider-recredentialing.html
https://www.nctracks.nc.gov/content/public/providers/provider-communications/2018-announcements/Changes-to-Re-credentialing-and-Reverification-Process.html
https://medicaid.ncdhhs.gov/providers/provider-enrollment/provider-enrollment-recredentialing
https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-Behavioral-Health-Provider-Enrollment.html
https://www.nctracks.nc.gov/content/public/providers/provider-communications/2025-Announcements/Federal-Provider-Enrollment-Application-Fee-Increase-for-Year-2026.html
https://www.nctracks.nc.gov/content/dam/jcr:5088259c-ab17-4c01-bf6d-c64786be1da4/State%20and%20Federal%20Fee%20Amounts%20by%20Year.xlsx
https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-ACA-application-fee.html
https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-fingerprinting.html
https://info.ncdhhs.gov/dhsr/abcms/pdf/Non-Criminal-Justice-Access-Agreement-Form_SB-41.pdf
https://medicaid.ncdhhs.gov/blog/2026/09/14/recent-behavioral-health-enrollment-updates-organizations
https://medicaid.ncdhhs.gov/blog/2026/04/16/post-enrollment-national-accreditation-update
https://medicaid.ncdhhs.gov/provider-enrollment-2026-summer-and-fall-series-1-powerpoint/open
https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx
https://www.sosnc.gov/fees/by_title/_Business_Registration/
https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_143B/GS_143B-1209.20.html
https://ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_122C/GS_122C-80.html
````

### Notebook B: Tailored Plans, H.R. 1 and rural funding (S30 to S53)

| ID | Name to give the source | Link | Used for |
|---|---|---|---|
| S30 | SL 2026-1 (HB 696) | https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-1.pdf | Medicaid changes law: open and closed networks, credentialing plan |
| S31 | SL 2026-41 (SB 257) | https://www3.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-41.pdf | Closed-network authority cited by Alliance |
| S32 | NC Medicaid Plans - get answers (plans by county) | https://www.ncmedicaidplans.gov/en/get-answers | Which Tailored Plan covers which county |
| S33 | NCDHHS LME/MCO directory | https://www.ncdhhs.gov/providers/lme-mco-directory | Plan counties and contacts |
| S34 | NC Medicaid health plans | https://medicaid.ncdhhs.gov/about-nc-medicaid/health-plans | Plan provider-network contacts |
| S35 | NC Medicaid - contracting with Tailored Plans | https://medicaid.ncdhhs.gov/contracting-tailored-plans/download | Whether providers must contract with every plan |
| S36 | Vaya and Partners merger provider FAQ | https://www.vayahealth.com/wp-content/uploads/2026/07/Merger_Provider_FAQ.pdf | Merger effective date and provider impact |
| S37 | Partners - Vaya and Partners announce merger | https://providers.partnersbhm.org/vaya-health-and-partners-health-management-announce-merger/ | Merger announcement |
| S38 | Alliance Health - become a provider | https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/ | Alliance enrollment and network rules |
| S39 | Trillium Provider Manual (older edition) | https://www.trilliumhealthresources.org/sites/default/files/docs/Provider-documents/Provider-Manual/Trillium-Provider-Manual.pdf | Trillium credentialing and contracting |
| S40 | NCDHHS - NC ROOTS hub leads | https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-organizations-orchestrating-transformation-sustainability-roots-hub-leads | Hub leads by region |
| S41 | NCDHHS press release - NC ROOTS hub leads (May 1, 2026) | https://www.ncdhhs.gov/news/press-releases/2026/05/01/ncdhhs-selects-nc-roots-hub-leads-strengthen-rural-health-care-across-north-carolina | What ROOTS is and who runs it |
| S42 | NCDHHS Rural Health Transformation Program (parent page) - link derived, may need correcting | https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program | Funding opportunities and deadlines |
| S43 | Public Law 119-21 (H.R. 1) - link not yet checked | https://www.congress.gov/119/plaws/publ21/PLAW-119publ21.pdf | Statute text (Medicaid sections and the Rural Health Transformation Program) |
| S44 | 42 U.S.C. 1396a (Cornell LII) | https://www.law.cornell.edu/uscode/text/42/1396a | State plan law as amended by H.R. 1 |
| S45 | NC legislative deck on H.R. 1 | https://webservices.ncleg.gov/ViewDocSiteFile/104990 | What NC says is in and out of scope |
| S46 | CMS fact sheet - community engagement interim final rule | https://www.cms.gov/newsroom/fact-sheets/medicaid-community-engagement-requirement-certain-individuals-interim-final-rule-comment-period-cms | Federal rule summary and exemptions |
| S47 | Federal Register 2026-11094 (CMS-2454-IFC) - short link, may need the PDF instead | https://www.federalregister.gov/d/2026-11094 | Interim final rule text |
| S48 | Medicaid.gov - community engagement (H.R. 1) | https://www.medicaid.gov/resources-for-states/working-families-tax-cut-legislation/community-engagement | CMS guidance bulletin |
| S49 | NC Medicaid - work and community engagement requirement | https://medicaid.ncdhhs.gov/beneficiaries/impact-hr-1-and-federal-changes-medicaid/work-and-community-engagement-requirement | NC start date, exemptions, member steps |
| S50 | NC Medicaid is changing | https://medicaid.ncdhhs.gov/beneficiaries/medicaid-is-changing | Retroactive coverage and renewal changes |
| S51 | NC Medicaid - prior approval and due process (providers) | https://medicaid.ncdhhs.gov/providers/programs-and-services/prior-approval-and-due-process | Verifying eligibility on the date of service |
| S52 | HHS fact sheet - 42 CFR Part 2 final rule | https://www.hhs.gov/hipaa/for-professionals/regulatory-initiatives/fact-sheet-42-cfr-part-2-final-rule/index.html | Consent and disclosure of SUD records |
| S53 | HHS announcement - Part 2 civil enforcement | https://www.hhs.gov/press-room/hhs-announce-civil-enforcement-program-sud-patient-records.html | Enforcement start date |

One link per line:

````text
https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-1.pdf
https://www3.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-41.pdf
https://www.ncmedicaidplans.gov/en/get-answers
https://www.ncdhhs.gov/providers/lme-mco-directory
https://medicaid.ncdhhs.gov/about-nc-medicaid/health-plans
https://medicaid.ncdhhs.gov/contracting-tailored-plans/download
https://www.vayahealth.com/wp-content/uploads/2026/07/Merger_Provider_FAQ.pdf
https://providers.partnersbhm.org/vaya-health-and-partners-health-management-announce-merger/
https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/
https://www.trilliumhealthresources.org/sites/default/files/docs/Provider-documents/Provider-Manual/Trillium-Provider-Manual.pdf
https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program/rural-organizations-orchestrating-transformation-sustainability-roots-hub-leads
https://www.ncdhhs.gov/news/press-releases/2026/05/01/ncdhhs-selects-nc-roots-hub-leads-strengthen-rural-health-care-across-north-carolina
https://www.ncdhhs.gov/about/department-initiatives/rural-health-transformation-program
https://www.congress.gov/119/plaws/publ21/PLAW-119publ21.pdf
https://www.law.cornell.edu/uscode/text/42/1396a
https://webservices.ncleg.gov/ViewDocSiteFile/104990
https://www.cms.gov/newsroom/fact-sheets/medicaid-community-engagement-requirement-certain-individuals-interim-final-rule-comment-period-cms
https://www.federalregister.gov/d/2026-11094
https://www.medicaid.gov/resources-for-states/working-families-tax-cut-legislation/community-engagement
https://medicaid.ncdhhs.gov/beneficiaries/impact-hr-1-and-federal-changes-medicaid/work-and-community-engagement-requirement
https://medicaid.ncdhhs.gov/beneficiaries/medicaid-is-changing
https://medicaid.ncdhhs.gov/providers/programs-and-services/prior-approval-and-due-process
https://www.hhs.gov/hipaa/for-professionals/regulatory-initiatives/fact-sheet-42-cfr-part-2-final-rule/index.html
https://www.hhs.gov/press-room/hhs-announce-civil-enforcement-program-sud-patient-records.html
````

### Documents the pack does not have yet

These topics have no source in the pack, so those tasks will mostly come back `NOT IN SOURCES` until you add them. Add the NC agency page for each and re-run the affected batch:

- Local zoning and ADA requirements (your county or city planning page; the app links https://www.ncacc.org/county-websites/)
- Insurance requirements (NC Department of Insurance, https://www.ncdoi.gov/)
- Banking and NCTracks EFT setup
- NC HealthConnex participation
- NC peer support specialist certification
- NC State Fire Marshal and local health inspection
- 10A NCAC 27G .0104 (definitions, including Qualified Professional)

---

## Chat instructions (paste into Configure chat, in both notebooks)

````text
You are a research assistant for a new North Carolina Medicaid behavioral health provider standing up CCP 8G (Peer Support Services), CCP 8A-12 (SAIOP) and CCP 8A-13 (SACOT). It is October 2026. The notebook may also cover the federal H.R. 1 (Public Law 119-21) Medicaid changes.

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
If you run out of space, finish the JSON for the keys you completed, list the keys remaining, and stop. Do not add commentary before part A.
````

---

## Prompt S: source audit (run first, in each notebook)

````text
SOURCE AUDIT
List every source in this notebook as a table: name | publisher | date, version or "last updated" shown in the document | what it covers | problems (empty, cut off, looks like a navigation page, or older than 2026). Then list the topics from this list that no source covers at all: local zoning and ADA, insurance requirements, banking and EFT setup, NC HealthConnex participation, peer support specialist certification, fire marshal inspection, Tailored Plan credentialing forms.
````

---

## Prompt V: verify the corrections already in the app

Run in Notebook A. Items 20 and 21 need Notebook B, so run them there as a second message (copy those two lines).

````text
VERIFY THE CORRECTIONS ALREADY IN THE APP
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
22. SBI state criminal check fee is capped at $14 by G.S. 143B-1209.20. What do the sources say about the cost of fingerprint-based national checks for NCTracks and for staff?
````

---

## Prompt C: county to Tailored Plan map (Notebook B)

````text
COUNTY TO TAILORED PLAN MAP
Using only the NC Medicaid Plans, NCDHHS LME/MCO directory, NC Medicaid health plans and Vaya/Partners merger sources, tell me which Tailored Plan covers each North Carolina county.
Return (A) one valid JSON object in a json code block where each key is a county name exactly as written in my list below and each value is the plan name exactly as the sources write it. Use "UNASSIGNED" if a source lists the county but names no plan. Use "NOT IN SOURCES" if no source mentions the county. If two sources disagree, use the value "CONFLICT: <plan from source A> vs <plan from source B>" and name the sources. No other keys.
Then (B) a table of each plan: plan name | counties covered (count) | provider-network phone and email | the source and section. Only give contacts that appear in a source. Note any difference between the NCDHHS directory and the NC Medicaid Plans page, and say which is newer.
My county list (100): Alamance, Alexander, Alleghany, Anson, Ashe, Avery, Beaufort, Bertie, Bladen, Brunswick, Buncombe, Burke, Cabarrus, Caldwell, Camden, Carteret, Caswell, Catawba, Chatham, Cherokee, Chowan, Clay, Cleveland, Columbus, Craven, Cumberland, Currituck, Dare, Davidson, Davie, Duplin, Durham, Edgecombe, Forsyth, Franklin, Gaston, Gates, Graham, Granville, Greene, Guilford, Halifax, Harnett, Haywood, Henderson, Hertford, Hoke, Hyde, Iredell, Jackson, Johnston, Jones, Lee, Lenoir, Lincoln, Macon, Madison, Martin, McDowell, Mecklenburg, Mitchell, Montgomery, Moore, Nash, New Hanover, Northampton, Onslow, Orange, Pamlico, Pasquotank, Pender, Perquimans, Person, Pitt, Polk, Randolph, Richmond, Robeson, Rockingham, Rowan, Rutherford, Sampson, Scotland, Stanly, Stokes, Surry, Swain, Transylvania, Tyrrell, Union, Vance, Wake, Warren, Washington, Watauga, Wayne, Wilkes, Wilson, Yadkin, Yancey.
````

---

## Prompt H: H.R. 1 foundations (Notebook B)

````text
H.R. 1 FOUNDATIONS
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
B. Which of those areas are legal requirements on providers, which apply only to the state or members, and which are good practice?
````

---

## Batch 1: Steps 4, 5, 6 (10 tasks) - Notebook A

````text
BATCH 1: write entries for the 10 tasks below, using only this notebook. Return the JSON keys in this exact order: step_4_sub_0, step_4_sub_1, step_4_sub_2, step_5_sub_0, step_5_sub_1, step_5_sub_2, step_5_sub_3, step_6_sub_0, step_6_sub_1, step_6_sub_2.
Step 4 - Facility Site Selection & Municipal Zoning Approval  (Phase 1: Business & Legal Foundation)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: None in the pack (local zoning and ADA). Add your county or city planning page and the ADA standards page, or expect NOT IN SOURCES.
  App context (unverified claims, check them):
    Description: Secure commercial day/outpatient premises sized for client census. Obtain written municipal/county zoning approval explicitly authorizing an outpatient behavioral health day facility.
    Responsible: Facility Director | Typical time: 3–6 weeks | Cost shown: Varies by lease + $50–$200 zoning fee
    Main resource the app links to: Local County/City Planning & Zoning Office (https://www.ncacc.org/county-websites/) - add it as a source if the answer needs it
    Depends on: Step 1 (Entity formed)
  Tasks:
    step_4_sub_0 = Execute lease or purchase agreement with confidentiality/counseling room partitions
    step_4_sub_1 = Request formal Zoning Determination Letter from city/county planning department
    step_4_sub_2 = Verify physical site meets ADA accessibility requirements

Step 5 - Commercial, General & Professional Liability Insurance  (Phase 1: Business & Legal Foundation)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: None in the pack. Add NC Department of Insurance pages, or expect NOT IN SOURCES. Check S01, S03 and S04 for any insurance requirement.
  App context (unverified claims, check them):
    Description: Bind mandatory commercial general liability, professional malpractice liability, and workers compensation coverage required by DHSR and LME/MCOs.
    Responsible: Owner / Risk Manager | Typical time: 1–2 weeks | Cost shown: $1,500 – $4,500 / year (deposit)
    Main resource the app links to: Commercial Healthcare Insurance Broker (https://www.ncdoi.gov/) - add it as a source if the answer needs it
    Depends on: Step 4 (Site lease secured)
  Tasks:
    step_5_sub_0 = Procure $1M / $3M professional malpractice liability policy
    step_5_sub_1 = Procure commercial general liability & property coverage
    step_5_sub_2 = Procure NC statutory Workers Compensation insurance
    step_5_sub_3 = Ensure certificates of insurance name the agency as primary insured

Step 6 - Dedicated Business Bank Account & EFT Setup  (Phase 1: Business & Legal Foundation)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S19 (EFT and enrollment context). Otherwise none: add the NCTracks EFT / banking page.
  App context (unverified claims, check them):
    Description: Open a dedicated commercial bank account for Medicaid electronic fund transfers (EFT) and operational separation.
    Responsible: Owner / Treasurer | Typical time: 1–2 business days | Cost shown: $0 – $100 initial deposit
    Main resource the app links to: Commercial Banking Institution (https://www.fdic.gov/) - add it as a source if the answer needs it
    Depends on: Step 1, 2, 3 (Entity, EIN, NPI)
  Tasks:
    step_6_sub_0 = Establish business checking account with voided check for NCTracks EFT
    step_6_sub_1 = Obtain bank letter verifying routing and account numbers
    step_6_sub_2 = Establish segregated payroll holding ledger
````

---

## Batch 2: Steps 7, 8 (7 tasks) - Notebook A

````text
BATCH 2: write entries for the 7 tasks below, using only this notebook. Return the JSON keys in this exact order: step_7_sub_0, step_7_sub_1, step_7_sub_2, step_7_sub_3, step_8_sub_0, step_8_sub_1, step_8_sub_2.
Step 7 - Governing Body Appointment & Key Clinical Leadership  (Phase 1: Business & Legal Foundation)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S06, S07, S08. Add 10A NCAC 27G .0104 (definitions) if not in the notebook.
  App context (unverified claims, check them):
    Description: Appoint Facility Director (named on license) and Clinical Director / Supervisor meeting Qualified Professional (QP) standards under 10A NCAC 27G .0104.
    Responsible: Governing Board / Owner | Typical time: 1–3 weeks | Cost shown: $0 (Internal governance)
    Main resource the app links to: 10A NCAC 27G .0104 Definitions (https://www.oah.nc.gov/) - add it as a source if the answer needs it
    Depends on: Step 1 (Corporate governance)
  Tasks:
    step_7_sub_0 = Document Board of Directors / Advisory Committee minutes
    step_7_sub_1 = Designate Facility Director as legal responsible party
    step_7_sub_2 = Appoint Clinical Director meeting QP requirements under 10A NCAC 27G .0104
    step_7_sub_3 = Draft organizational chart showing lines of clinical and administrative supervision

Step 8 - LME/MCO Letter of Support (10A NCAC 27G .0406)  (Phase 1: Business & Legal Foundation)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S08, S35, S38, S39, S30
  App context (unverified claims, check them):
    Description: Formally request the mandatory Letter of Support from the LME/MCO governing the facility county footprint. Mandatory attachment for the DHSR license application.
    Responsible: Facility Director | Typical time: 2–6 weeks | Cost shown: $0 (Administrative)
    Main resource the app links to: Assigned LME/MCO (Alliance, Partners, Trillium, or Vaya) (https://medicaid.ncdhhs.gov/transformation/tailored-plans) - add it as a source if the answer needs it
    Depends on: Step 4 & 7 (Facility site & leadership)
  Tasks:
    step_8_sub_0 = Submit program summary and county location to assigned LME/MCO Provider Network desk
    step_8_sub_1 = Include intended CCP services: Peer Support, SAIOP, and/or SACOT
    step_8_sub_2 = Obtain formal signed Letter of Support citing 10A NCAC 27G .0406
````

---

## Batch 3: Steps 9, 10 (9 tasks) - Notebook A

````text
BATCH 3: write entries for the 9 tasks below, using only this notebook. Return the JSON keys in this exact order: step_9_sub_0, step_9_sub_1, step_9_sub_2, step_9_sub_3, step_9_sub_4, step_10_sub_0, step_10_sub_1, step_10_sub_2, step_10_sub_3.
Step 9 - Statutory Policies & Procedures Engineering  (Phase 2: DHSR Licensure (10A NCAC 27G))
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S06, S07, S10, S11, S52, S01, S03, S04
  App context (unverified claims, check them):
    Description: Draft comprehensive P&P manual cross-referenced to 10A NCAC 27G, the DHHS Records Management and Documentation Manual (RMDM, effective July 8, 2025), modernized 42 CFR Part 2 rules, and NC IRIS 72-hour critical incident reporting.
    Responsible: Clinical Director / Compliance Consultant | Typical time: 3–6 weeks | Cost shown: $0 – $3,500 (consultant optional)
    Main resource the app links to: NC DHSR MHLCS Policy Review Tool (https://info.ncdhhs.gov/dhsr/mhlcs/establish.html) - add it as a source if the answer needs it
    Depends on: Step 7 & 8 (Leadership named, Letter of Support in progress)
  Tasks:
    step_9_sub_0 = Draft governance, client rights & grievance procedures (10A NCAC Subchapters D & E)
    step_9_sub_1 = Integrate RMDM service note requirements cited in CCP 8G, 8A-12 and 8A-13
    step_9_sub_2 = Incorporate 42 CFR Part 2 modernized consent and disclosure restrictions
    step_9_sub_3 = Establish Incident Response Improvement System (IRIS) 72-hour reporting workflow (.0600)
    step_9_sub_4 = Draft Fraud, Waste & Abuse (FWA) / False Claims Act compliance plan

Step 10 - Core Clinical & Peer Support Staff Recruitment  (Phase 2: DHSR Licensure (10A NCAC 27G))
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S01, S03, S04, S02
  App context (unverified claims, check them):
    Description: Recruit and hire staff meeting regulatory ratios: LCAS/CCS clinical supervisor for SAIOP/SACOT, Qualified Professionals for group therapy, and NC Certified Peer Support Specialists (CPSS).
    Responsible: Clinical Director / HR | Typical time: 4–8 weeks | Cost shown: Recruitment costs / Staff payroll
    Main resource the app links to: NCASPPB / UNC NCCPSS Portal (https://pss.unc.edu/) - add it as a source if the answer needs it
    Depends on: Step 7 & 9 (P&P and leadership established)
  Tasks:
    step_10_sub_0 = Hire LCAS (Licensed Clinical Addictions Specialist) or CCS for SUD supervision
    step_10_sub_1 = Verify SACOT staffing: at least 1 clinical staff for every 10 or fewer beneficiaries in group counseling (CCP 8A-13 section 6.2)
    step_10_sub_2 = Verify Peer Support staffing: 1 QP per 8 CPSS, and CPSS to beneficiary ratios of 1:15 individual and 1:12 group (CCP 8G section 6.2.1)
    step_10_sub_3 = Execute signed employment agreements with defined job descriptions
````

---

## Batch 4: Steps 11, 12 (8 tasks) - Notebook A

````text
BATCH 4: write entries for the 8 tasks below, using only this notebook. Return the JSON keys in this exact order: step_11_sub_0, step_11_sub_1, step_11_sub_2, step_11_sub_3, step_12_sub_0, step_12_sub_1, step_12_sub_2, step_12_sub_3.
Step 11 - Mandatory Pre-Hire Screenings (HCPR & Exclusion Checks)  (Phase 2: DHSR Licensure (10A NCAC 27G))
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S26, S27, S19, S20
  App context (unverified claims, check them):
    Description: Perform mandatory pre-employment checks: NC Health Care Personnel Registry (HCPR) under N.C.G.S. § 131E-256, NC Sex Offender Registry, and federal OIG/SAMHSA exclusion logs.
    Responsible: HR Director / Compliance Officer | Typical time: 1–2 weeks | Cost shown: $35 – $75 per candidate (estimate; the SBI state check is capped at $14 by statute and no national check price is published)
    Main resource the app links to: NC Health Care Personnel Registry (HCPR) (https://info.ncdhhs.gov/dhsr/hcpr/index.html) - add it as a source if the answer needs it
    Depends on: Step 10 (Candidates identified)
  Tasks:
    step_11_sub_0 = Execute and file NC Health Care Personnel Registry (HCPR) check PRIOR to hire date
    step_11_sub_1 = Conduct state and national criminal history checks with fingerprints
    step_11_sub_2 = Screen staff and 5%+ owners against OIG LEIE, SAM.gov, and NC Exclusion database
    step_11_sub_3 = Establish recurring monthly OIG exclusion audit calendar

Step 12 - CPSS Credential & Lived-Experience Verification  (Phase 2: DHSR Licensure (10A NCAC 27G))
  Applies to: CCP 8G
  Most likely sources: S01, S02 (CPSS roster and certification). Add the NC peer support certification program page.
  App context (unverified claims, check them):
    Description: Verify all Peer Support staff hold active NCCPSS certification from UNC School of Social Work, documenting 18+ months lived recovery and ethics coursework.
    Responsible: Clinical Director / HR | Typical time: 1–2 weeks | Cost shown: $0 (Online verification)
    Main resource the app links to: UNC NCCPSS Program Office (https://pss.unc.edu/) - add it as a source if the answer needs it
    Depends on: Step 10 (CPSS hired)
  Tasks:
    step_12_sub_0 = Verify active credential on NCCPSS registry
    step_12_sub_1 = File proof of 50-hour Foundations course + 20 hours continuing education
    step_12_sub_2 = Verify lived experience attestation in HR record
    step_12_sub_3 = Set 2-year certification renewal reminder
````

---

## Batch 5: Steps 13, 14, 15 (10 tasks) - Notebook A

````text
BATCH 5: write entries for the 10 tasks below, using only this notebook. Return the JSON keys in this exact order: step_13_sub_0, step_13_sub_1, step_13_sub_2, step_14_sub_0, step_14_sub_1, step_14_sub_2, step_14_sub_3, step_15_sub_0, step_15_sub_1, step_15_sub_2.
Step 13 - Local Fire Marshal & Sanitation Facility Clearances  (Phase 2: DHSR Licensure (10A NCAC 27G))
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S08, S09. Add the NC State Fire Marshal and local health department pages.
  App context (unverified claims, check them):
    Description: Schedule and complete fire safety inspection and county health department sanitation inspections for day treatment occupancy.
    Responsible: Facility Director | Typical time: 2–4 weeks | Cost shown: $75 – $250 inspection fees
    Main resource the app links to: Local Municipal Fire Marshal & County Health Dept (https://www.ncdhhs.gov/divisions/public-health/county-health-departments) - add it as a source if the answer needs it
    Depends on: Step 4 (Site secured)
  Tasks:
    step_13_sub_0 = Pass annual Fire Marshal inspection with stamped approval certificate
    step_13_sub_1 = Pass sanitation inspection for day facility restrooms and water supply
    step_13_sub_2 = Post approved maximum room occupancy signs in group rooms

Step 14 - DHSR MHLCS Initial Licensure Application Submission  (Phase 2: DHSR Licensure (10A NCAC 27G))
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S08, S09, S24
  App context (unverified claims, check them):
    Description: Submit formal Initial Licensure Application packet to DHSR Mental Health Licensure and Certification Section (MHLCS) in Raleigh with all required statutory exhibits. Peer support only: the NCTracks Provider Permission Matrix (Aug 16, 2026) does not require a DHSR license for peer support, but whether it is licensable at your site is unconfirmed, so call DHSR at 919-855-3795 before skipping licensure.
    Responsible: Facility Director | Typical time: 1–2 weeks to assemble | Cost shown: $265 base fee for a non-residential facility, no per-capacity fee; licenses renew yearly
    Main resource the app links to: DHSR MHLCS Application Section (https://info.ncdhhs.gov/dhsr/mhlcs/establish.html) - add it as a source if the answer needs it
    Depends on: Steps 4, 8, 9, 10, 11, 13
  Tasks:
    step_14_sub_0 = Complete DHSR Initial Licensure Application PDF
    step_14_sub_1 = Attach LME/MCO Letter of Support, Zoning Letter, and Fire/Sanitation reports
    step_14_sub_2 = Attach complete P&P manual cross-walked to 10A NCAC 27G
    step_14_sub_3 = Attach staff roster with verified credentials and fee payment

Step 15 - DHSR On-Site Initial Licensure Survey  (Phase 2: DHSR Licensure (10A NCAC 27G))
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S08, S09, S07
  App context (unverified claims, check them):
    Description: Undergo comprehensive on-site survey by DHSR inspectors reviewing physical plant, HR personnel files, restrictive intervention training, and clinical policies.
    Responsible: Facility Director & Clinical Director (Mandatory on-site) | Typical time: 4–8 weeks queue wait | Cost shown: $0 (Included in filing)
    Main resource the app links to: DHSR Survey Team (https://info.ncdhhs.gov/dhsr/mhlcs/) - add it as a source if the answer needs it
    Depends on: Step 14 (Application accepted by DHSR)
  Tasks:
    step_15_sub_0 = Host DHSR inspector walkthrough of physical day facility
    step_15_sub_1 = Provide 100% compliant personnel files with pre-hire HCPR checks
    step_15_sub_2 = Demonstrate knowledge of client rights and restrictive intervention policies (10A NCAC 27G .0209)
````

---

## Batch 6: Steps 16, 17, 18 (10 tasks) - Notebook A

````text
BATCH 6: write entries for the 10 tasks below, using only this notebook. Return the JSON keys in this exact order: step_16_sub_0, step_16_sub_1, step_16_sub_2, step_17_sub_0, step_17_sub_1, step_17_sub_2, step_18_sub_0, step_18_sub_1, step_18_sub_2, step_18_sub_3.
Step 16 - Plan of Correction (POC) & License Issuance  (Phase 2: DHSR Licensure (10A NCAC 27G))
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S08, S09
  App context (unverified claims, check them):
    Description: Respond to any Statement of Deficiencies within 10–15 calendar days with a systemic Plan of Correction. Receive official DHSR facility license.
    Responsible: Facility Director / Clinical Director | Typical time: 2–4 weeks | Cost shown: $0
    Main resource the app links to: DHSR MHLCS Licensure Desk (https://info.ncdhhs.gov/dhsr/mhlcs/) - add it as a source if the answer needs it
    Depends on: Step 15 (Survey findings received)
  Tasks:
    step_16_sub_0 = Draft Plan of Correction identifying root cause, systemic change, and monitoring frequency
    step_16_sub_1 = Submit POC to DHSR within required deadline
    step_16_sub_2 = Receive official DHSR Mental Health / SUD Facility License with service designations

Step 17 - NC HealthConnex (HIE) Participation Agreement & Integration  (Phase 3: NCTracks & State Integration)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: None in the pack. Add the NC HealthConnex participation pages.
  App context (unverified claims, check them):
    Description: Execute mandatory full participation agreement with NC Health Information Exchange Authority (NC HIEA) per N.C.G.S. § 90-414.4 and configure EHR interface.
    Responsible: EHR Administrator / Compliance Officer | Typical time: 3–6 weeks | Cost shown: $0 state fee (EHR interface fee varies)
    Main resource the app links to: NC HealthConnex / NC HIEA (https://hiea.nc.gov/) - add it as a source if the answer needs it
    Depends on: Step 16 (DHSR license issued)
  Tasks:
    step_17_sub_0 = Execute NC HealthConnex Full Participation Agreement online
    step_17_sub_1 = Select EHR certified for NC HealthConnex HL7/FHIR encounter data exchange
    step_17_sub_2 = File proof of active connection or approved HIEA extension before billing

Step 18 - NCTracks Organization Provider Enrollment Application  (Phase 3: NCTracks & State Integration)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S12, S14, S15, S16, S17, S18, S21, S23, S24
  App context (unverified claims, check them):
    Description: Submit Organization Enrollment Application in NCTracks. Designate authorized Office Administrator with NCID, attach DHSR license, and assign taxonomy codes.
    Responsible: Office Administrator | Typical time: 1–2 weeks to submit | Cost shown: $100 NC state fee + $750 federal application fee (2026 amount; the 2027 amount applies from Jan 1, 2027)
    Main resource the app links to: NCTracks Provider Portal (https://www.nctracks.nc.gov/content/public/providers/provider-enrollment.html) - add it as a source if the answer needs it
    Depends on: Step 3, 16, 17 (NPI, DHSR License, HIE connection)
  Tasks:
    step_18_sub_0 = Obtain NCID for designated Office Administrator
    step_18_sub_1 = Complete NCTracks Organization Enrollment Application
    step_18_sub_2 = Select correct taxonomies aligned with Provider Permission Matrix (PPM)
    step_18_sub_3 = Upload DHSR license, W-9, and banking EFT documentation
````

---

## Batch 7: Steps 19, 20, 22 (10 tasks) - Notebook A

````text
BATCH 7: write entries for the 10 tasks below, using only this notebook. Return the JSON keys in this exact order: step_19_sub_0, step_19_sub_1, step_19_sub_2, step_20_sub_0, step_20_sub_1, step_20_sub_2, step_22_sub_0, step_22_sub_1, step_22_sub_2, step_22_sub_3.
Step 19 - Moderate/High Risk Fingerprinting & Site Screening  (Phase 3: NCTracks & State Integration)
  Applies to: CCP 8A-12, CCP 8A-13
  Most likely sources: S19, S20, S21, S24
  App context (unverified claims, check them):
    Description: Complete mandatory fingerprint criminal history checks for 5%+ owners and managing employees under N.C.G.S. § 108C-3; complete NCTracks on-site review. Per a Sept 14, 2026 NC Medicaid bulletin, the site visit and fingerprinting are waived only if you hold active national accreditation for the same location and service.
    Responsible: 5%+ Owners / Managing Employees | Typical time: 3–5 weeks | Cost shown: $38 per person (SBI/FBI electronic fingerprinting; NCTracks says the cost varies by location, so confirm)
    Main resource the app links to: Local Sheriff’s Office & NCTracks Screening (https://www.nctracks.nc.gov/) - add it as a source if the answer needs it
    Depends on: Step 18 (NCTracks notification received)
  Tasks:
    step_19_sub_0 = Schedule electronic LiveScan fingerprinting within 30-day notice window
    step_19_sub_1 = Submit Fingerprint Verification Forms to NCTracks Provider Screening Unit
    step_19_sub_2 = Pass NCTracks physical site visit verification

Step 20 - NCTracks Approval & Effective Date Alignment  (Phase 3: NCTracks & State Integration)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S12, S13, S14, S15, S23
  App context (unverified claims, check them):
    Description: Receive approved NCTracks enrollment letter. Link individual rendering providers (LCAS, CCS, QP) to the organizational billing NPI.
    Responsible: Office Administrator | Typical time: 2–4 weeks | Cost shown: $0
    Main resource the app links to: NCTracks Provider Record (https://www.nctracks.nc.gov/) - add it as a source if the answer needs it
    Depends on: Step 18 & 19 (Enrollment and screening approved)
  Tasks:
    step_20_sub_0 = Verify billing effective date aligns with credentials
    step_20_sub_1 = Submit Manage Change Request (MCR) to affiliate rendering clinicians to organizational NPI
    step_20_sub_2 = Test electronic claims submission and ERA 835 delivery

Step 22 - EHR Clinical Setup & Service Note (RMDM) Scrubber  (Phase 5: Launch & Ongoing Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S01, S03, S04, S10, S11, S02
  App context (unverified claims, check them):
    Description: Configure EHR clinical note templates that meet the DHHS Records Management and Documentation Manual (RMDM), including service start and end times, 15-minute units (H0038) for Peer Support, and same-day service exclusion checks.
    Responsible: Clinical Director & Billing Specialist | Typical time: 2–4 weeks | Cost shown: $150 – $400 / clinician / month (EHR SaaS)
    Main resource the app links to: Behavioral Health EHR Vendor (https://www.healthit.gov/) - add it as a source if the answer needs it
    Depends on: Step 9 & 17 (P&P and HIE interface ready)
  Tasks:
    step_22_sub_0 = Configure service note templates that meet RMDM requirements, including start and end times
    step_22_sub_1 = Build automated billing rules blocking concurrent SAIOP + SACOT same-day claims
    step_22_sub_2 = Configure 20-unit (5 hr) daily and 80-unit (20 hr) weekly billing limits for Peer Support
    step_22_sub_3 = Configure 3-hr daily minimum for SAIOP (H0015, one event per day) and 4-hr daily minimum for SACOT (H2035, one unit per hour)
````

---

## Batch 8: Steps 23, 24 (7 tasks) - Notebook A

````text
BATCH 8: write entries for the 7 tasks below, using only this notebook. Return the JSON keys in this exact order: step_23_sub_0, step_23_sub_1, step_23_sub_2, step_24_sub_0, step_24_sub_1, step_24_sub_2, step_24_sub_3.
Step 23 - 24/7/365 First-Responder Crisis Protocol & Clinical Training  (Phase 5: Launch & Ongoing Compliance)
  Applies to: CCP 8A-12, CCP 8A-13
  Most likely sources: S03, S04, S01, S07
  App context (unverified claims, check them):
    Description: Train all staff on mandatory 24/7/365 crisis first-responder coverage required by CCP 8A-12 and CCP 8A-13; conduct restrictive intervention & client rights training (10A NCAC 27G .0209).
    Responsible: Clinical Director | Typical time: 1–2 weeks | Cost shown: Staff training hours
    Main resource the app links to: Internal Clinical Training (https://www.oah.nc.gov/) - add it as a source if the answer needs it
    Depends on: Step 10 & 22 (Staff hired & EHR ready)
  Tasks:
    step_23_sub_0 = Publish rotating 24/7/365 clinical crisis on-call schedule with LCAS/CCS backup
    step_23_sub_1 = Document staff training on client rights, confidentiality, and de-escalation
    step_23_sub_2 = File signed training completion certificates in personnel records

Step 24 - Intake, Assessment, PCP & Authorization Protocol  (Phase 5: Launch & Ongoing Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S01, S03, S04, S10, S11, S52
  App context (unverified claims, check them):
    Description: Standardize intake: Comprehensive Clinical Assessment (CCA) within 1 year, ASAM level-of-care determination, Service Order signed by physician/NP/PA, and tracking of any authorization periods your plan requires. CCP 8A-12 and 8A-13 require no prior approval; CCP 8G authorizes up to 176 units per 60 days.
    Responsible: Clinical Supervisor / Intake Coordinator | Typical time: 1–2 weeks | Cost shown: $0 (Clinical workflow)
    Main resource the app links to: NC Medicaid Person-Centered Plan (PCP) Manual (https://medicaid.ncdhhs.gov/) - add it as a source if the answer needs it
    Depends on: Step 21 & 22 (Network contract and EHR active)
  Tasks:
    step_24_sub_0 = Verify CCA contains required ASAM 6-dimension assessment (Level 2.1 SAIOP / Level 2.5 SACOT)
    step_24_sub_1 = Ensure Service Order is executed prior to or on Day 1 of service
    step_24_sub_2 = Set up automated tracking of Peer Support authorization periods (176 units per 60 days, no more than 88 per 30 days) and confirm with each Tailored Plan whether SAIOP or SACOT need any authorization
    step_24_sub_3 = Execute modernized 42 CFR Part 2 and HIPAA consent documentation at intake
````

---

## Batch 9: Step 25 (4 tasks) - Notebook A

````text
BATCH 9: write entries for the 4 tasks below, using only this notebook. Return the JSON keys in this exact order: step_25_sub_0, step_25_sub_1, step_25_sub_2, step_25_sub_3.
Step 25 - National Accreditation Roadmap & NCTracks 5-Yr Reverification  (Phase 5: Launch & Ongoing Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S22, S21, S03, S04, S01, S12, S13, S24
  App context (unverified claims, check them):
    Description: Plan for national accreditation within 1 year of enrollment. CCP 8A-12 and 8A-13 say 1 year; the Provider Permission Matrix says 3 years for SAIOP and SACOT and 1 year for peer support, so plan for 1 year until NC Medicaid clarifies. Accepted bodies are COA, The Joint Commission and CARF. Establish a compliance calendar for annual DHSR renewal, 2-yr CPSS renewal, and 5-yr NCTracks revalidation.
    Responsible: Quality Director / CEO | Typical time: Ongoing (Survey window months 9–12) | Cost shown: $8,000 – $14,000 (CARF survey fee)
    Main resource the app links to: CARF International Behavioral Health (https://www.carf.org/) - add it as a source if the answer needs it
    Depends on: Step 20 & 21 (Operational and billing Medicaid)
  Tasks:
    step_25_sub_0 = Select an accepted accreditation body (CARF, COA or The Joint Commission)
    step_25_sub_1 = Run continuous 6-month demonstration period with QI Committee and chart peer reviews
    step_25_sub_2 = Calendar NCTracks 5-year revalidation (first notice 70 days out, reminders at 50, 20 and 5 days; a missed deadline means suspension, then termination)
    step_25_sub_3 = Calendar monthly OIG/SAM exclusion screenings and 2-year CPSS renewals
````

---

## Batch 10: Step 21 (4 tasks) - Notebook B

````text
BATCH 10: write entries for the 4 tasks below, using only this notebook. Return the JSON keys in this exact order: step_21_sub_0, step_21_sub_1, step_21_sub_2, step_21_sub_3.
Step 21 - Regional Tailored Plan / LME-MCO Network Participation  (Phase 4: Tailored Plan Contracting)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S30, S31, S32, S33, S34, S35, S36, S37, S38, S39
  App context (unverified claims, check them):
    Description: Execute network participation agreements with assigned regional Tailored Plans (Alliance, Partners, Trillium, or Vaya) for Medicaid and State-Funded benefit packages.
    Responsible: Executive Director / Contracting Officer | Typical time: 6–12 weeks | Cost shown: $0 (Contracting)
    Main resource the app links to: Regional LME/MCO Contracting Portal (https://medicaid.ncdhhs.gov/transformation/tailored-plans) - add it as a source if the answer needs it
    Depends on: Step 16 (DHSR License) & Step 18 (NCTracks submitted)
  Tasks:
    step_21_sub_0 = Submit network participation applications to applicable regional plans
    step_21_sub_1 = Submit roster attestation with clinician CAQH IDs and NCTracks records
    step_21_sub_2 = Establish Electronic Data Interchange (EDI) testing with plan clearinghouses
    step_21_sub_3 = Complete Utilization Management (UM) portal training for prior authorizations
````

---

## Batch 11 (H.R. 1): Steps 26, 27 (8 tasks) - Notebook B

````text
BATCH 11 (H.R. 1): write entries for the 8 tasks below, using only this notebook. Return the JSON keys in this exact order: step_26_sub_0, step_26_sub_1, step_26_sub_2, step_26_sub_3, step_27_sub_0, step_27_sub_1, step_27_sub_2, step_27_sub_3.
These are H.R. 1 tasks. In EACH entry add two fields after verify: "basis" (one of "required" = a provider legal or contract duty today; "expected" = NC has published or announced it will apply to providers; "recommended" = good practice only) and "effective_date" (the date it applies, or "unknown"). If a task is not really a provider obligation, say so in verify and suggest better wording for the task.
Step 26 - H.R. 1 Impact Review & Compliance Owner  (Phase 6: H.R. 1 Medicaid Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S43, S44, S45, S48, S49, S50
  App context (unverified claims, check them):
    Description: H.R. 1 (Public Law 119-21, the 2025 federal budget reconciliation act) changes Medicaid eligibility, renewals, cost-sharing and program-integrity rules, and created the Rural Health Transformation Program. Work out which provisions reach your service lines and name one accountable owner. Dates to confirm against current NC Medicaid guidance: Oct 2026 (immigrant eligibility), Dec 2026 (six-month renewals for expansion adults), Jan 2027 (community engagement and shorter retroactive coverage), Oct 2028 (cost-sharing).
    Responsible: Compliance Officer / Owner | Typical time: 1–2 weeks | Cost shown: $0 (Internal)
    Main resource the app links to: H.R. 1 (119th Congress) bill text (https://www.congress.gov/bill/119th-congress/house-bill/1) - add it as a source if the answer needs it
    Depends on: Step 1 (Entity formed)
  Tasks:
    step_26_sub_0 = Read the H.R. 1 Medicaid provisions and the NC Medicaid guidance that apply to outpatient behavioral health
    step_26_sub_1 = Name an H.R. 1 compliance owner and a backup in the governing body minutes
    step_26_sub_2 = Subscribe to NC Medicaid bulletins and each Tailored Plan provider notice list for H.R. 1 updates
    step_26_sub_3 = Build a dated H.R. 1 calendar of effective dates, each with an internal deadline and an owner

Step 27 - Eligibility Verification & Six-Month Renewal Readiness  (Phase 6: H.R. 1 Medicaid Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S50, S49, S51, S45
  App context (unverified claims, check them):
    Description: Expansion adults are moving to eligibility renewals every six months, so more clients will lose coverage for paperwork reasons. Build intake and billing controls that check eligibility before every billing period, and help clients keep their coverage without giving legal advice.
    Responsible: Billing Manager / Intake Lead | Typical time: 2–4 weeks | Cost shown: $0 (Internal workflow)
    Main resource the app links to: NCTracks (eligibility verification) (https://www.nctracks.nc.gov/) - add it as a source if the answer needs it
    Depends on: Step 18 (NCTracks enrollment) & Step 22 (EHR setup)
  Tasks:
    step_27_sub_0 = Add a Medicaid eligibility check to intake and again before each billing period or authorization renewal
    step_27_sub_1 = Create a claim-hold and follow-up workflow for clients whose eligibility lapses during treatment
    step_27_sub_2 = Train staff to remind clients about renewal notices and refer them to their county DSS or NC Medicaid for help
    step_27_sub_3 = Track coverage-loss reasons monthly and report trends to the governing body
````

---

## Batch 12 (H.R. 1): Steps 28, 29 (9 tasks) - Notebook B

````text
BATCH 12 (H.R. 1): write entries for the 9 tasks below, using only this notebook. Return the JSON keys in this exact order: step_28_sub_0, step_28_sub_1, step_28_sub_2, step_28_sub_3, step_28_sub_4, step_29_sub_0, step_29_sub_1, step_29_sub_2, step_29_sub_3.
These are H.R. 1 tasks. In EACH entry add two fields after verify: "basis" (one of "required" = a provider legal or contract duty today; "expected" = NC has published or announced it will apply to providers; "recommended" = good practice only) and "effective_date" (the date it applies, or "unknown"). If a task is not really a provider obligation, say so in verify and suggest better wording for the task.
Step 28 - Community Engagement Requirement & Exemption Documentation  (Phase 6: H.R. 1 Medicaid Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S43, S44, S46, S47, S48, S49, S52, S53
  App context (unverified claims, check them):
    Description: H.R. 1 requires many expansion adults to show work, community service, school or a similar activity. Exemptions may cover people in substance use disorder treatment, people with a disabling mental disorder and people who are medically frail. Prepare to document treatment participation and exemptions accurately, with proper client consent, once NC Medicaid sets its process.
    Responsible: Clinical Director / Compliance Officer | Typical time: 3–4 weeks | Cost shown: $0 (Internal)
    Main resource the app links to: NC Medicaid (NC DHHS) (https://medicaid.ncdhhs.gov/) - add it as a source if the answer needs it
    Depends on: Step 26 (Impact review) & Step 24 (Intake and assessment)
  Tasks:
    step_28_sub_0 = Confirm with NC Medicaid and each Tailored Plan who must meet the requirement, which exemptions apply and how providers submit documentation
    step_28_sub_1 = Add a client consent form for sharing treatment participation or exemption information, including the 42 CFR Part 2 rules for substance use disorder records
    step_28_sub_2 = Create a clinician-signed template letter for exemptions such as SUD treatment, disabling mental disorder or medical frailty
    step_28_sub_3 = Set up EHR reports that show each client attendance hours in SAIOP, SACOT or peer support for verification requests
    step_28_sub_4 = Train staff on what they may tell clients about the requirement and when to refer them to NC Medicaid or county DSS

Step 29 - Coverage Changes, Billing & Cost-Sharing Controls  (Phase 6: H.R. 1 Medicaid Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S50, S49, S45, S43
  App context (unverified claims, check them):
    Description: Shorter retroactive coverage, new immigrant eligibility rules and future cost-sharing for some expansion adults change what you can bill and collect. Update intake, financial-responsibility and billing rules so you do not deliver services you cannot get paid for or collect amounts you are not allowed to charge.
    Responsible: Billing Manager / Compliance Officer | Typical time: 2–3 weeks | Cost shown: $0 (Internal policy work)
    Main resource the app links to: NC Medicaid (NC DHHS) (https://medicaid.ncdhhs.gov/) - add it as a source if the answer needs it
    Depends on: Step 26 (Impact review) & Step 20 (NCTracks approval)
  Tasks:
    step_29_sub_0 = Update the intake and billing policy for shorter retroactive coverage: confirm eligibility before services rather than relying on back-dated approval
    step_29_sub_1 = Write a financial responsibility and sliding-fee policy, with client notices, for people who lose or do not qualify for Medicaid
    step_29_sub_2 = Ask each Tailored Plan in writing whether member cost-sharing will apply to peer support, SAIOP and SACOT, and when, then set front-desk scripts
    step_29_sub_3 = Update billing system edits for new eligibility categories and immigration-status changes, and test claims before launch
````

---

## Batch 13 (H.R. 1): Steps 30, 31 (8 tasks) - Notebook B

````text
BATCH 13 (H.R. 1): write entries for the 8 tasks below, using only this notebook. Return the JSON keys in this exact order: step_30_sub_0, step_30_sub_1, step_30_sub_2, step_30_sub_3, step_31_sub_0, step_31_sub_1, step_31_sub_2, step_31_sub_3.
These are H.R. 1 tasks. In EACH entry add two fields after verify: "basis" (one of "required" = a provider legal or contract duty today; "expected" = NC has published or announced it will apply to providers; "recommended" = good practice only) and "effective_date" (the date it applies, or "unknown"). If a task is not really a provider obligation, say so in verify and suggest better wording for the task.
Step 30 - Program Integrity, Provider Screening & Funding Risk  (Phase 6: H.R. 1 Medicaid Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S43, S45, S12, S13, S23
  App context (unverified claims, check them):
    Description: H.R. 1 tightens Medicaid program-integrity rules, including more frequent checks of provider enrollment data against exclusion and death records, and it limits some state financing tools that help fund provider payments. Keep enrollment data clean and plan for rate or volume changes.
    Responsible: Compliance Officer / CFO | Typical time: 3–4 weeks | Cost shown: $0 (Internal)
    Main resource the app links to: OIG Exclusions Database (LEIE) (https://oig.hhs.gov/exclusions/) - add it as a source if the answer needs it
    Depends on: Step 20 (NCTracks approval) & Step 25 (Compliance calendar)
  Tasks:
    step_30_sub_0 = Add a monthly screen of every owner, manager and rendering provider against the OIG exclusion list, SAM.gov and the death records NC Medicaid requires
    step_30_sub_1 = Calendar NCTracks updates for ownership, address, license, NPI and taxonomy changes, with the reporting deadline for each
    step_30_sub_2 = Build a reimbursement-risk budget that shows cash needs if Medicaid volume or rates fall 10 to 20 percent
    step_30_sub_3 = Set a cash reserve target and a review date tied to NC Medicaid rate and Tailored Plan contract notices

Step 31 - Rural Health Transformation (NC ROOTS) Funding  (Phase 6: H.R. 1 Medicaid Compliance)
  Applies to: CCP 8G, CCP 8A-12, CCP 8A-13
  Most likely sources: S40, S41, S42, S43
  App context (unverified claims, check them):
    Description: H.R. 1 created a multi-year Rural Health Transformation Program that funds state plans, which NC runs as NC ROOTS. Providers in rural counties may be able to apply for sub-awards or join hub networks. Find out what NC has opened and whether your counties and services qualify.
    Responsible: Owner / Grants Lead | Typical time: 4–8 weeks | Cost shown: $0 (Internal)
    Main resource the app links to: NC Department of Health and Human Services (https://www.ncdhhs.gov/) - add it as a source if the answer needs it
    Depends on: Step 1 (Entity formed) & county selection in Setup
  Tasks:
    step_31_sub_0 = Find NC rural health transformation (NC ROOTS) announcements, funding notices and eligibility rules from NC DHHS
    step_31_sub_1 = Contact the hub lead for each of your counties (see Regional contacts) and ask how providers join or apply
    step_31_sub_2 = Prepare a one-page capability statement with services, counties served, peer workforce and expected outcomes
    step_31_sub_3 = Calendar application deadlines, reporting requirements and any data or technology conditions
````
