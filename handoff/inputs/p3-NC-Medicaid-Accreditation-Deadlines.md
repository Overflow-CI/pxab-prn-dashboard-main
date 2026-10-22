> From: https://www.perplexity.ai/computer/tasks/0bfd0273-261a-4ba0-959e-1365f1634578

# you asked

message time: 2026-10-18 23:46:54

RESEARCH RULES (apply to every answer)
- It is late October 2026. Use official or primary sources only: NC DHHS, NC Medicaid, NCTracks, DHSR, NC General Assembly, federal agencies, and the plans' own provider pages. Open each page before citing it. Blogs, consultants and forums count only as secondary, and must be labeled that way.
- Never guess or fill a gap. Do not invent phone numbers, emails, addresses, URLs, fees, dates or section numbers. If you cannot verify something on a source you opened, write "NOT VERIFIED" and say what to check and who to call.
- Give the URL and the date shown on the page (or "undated") for every fact. Quote the key sentence, 25 words or fewer, for anything that decides a question.
- If sources conflict, report both with their dates and say which is newer and which is the policy text.
- Values labeled "APP CURRENTLY SHOWS" come from my dashboard and may be wrong. Mark each one CONFIRMED, CORRECTED (give the right value) or NOT VERIFIED.
- Return valid JSON in a json code block exactly as specified, then a short SOURCES table (title, publisher, URL, date, primary or secondary), then OPEN QUESTIONS. Plain text inside JSON strings, one line each, escaped double quotes, no citation markers like [1] inside the JSON. No commentary before the JSON.
- This is research, not legal advice.

PROMPT F3 - OPEN POLICY QUESTIONS FROM THE FIRST RESEARCH PASS

Answer each question separately. For each, give a status: "settled" (one authoritative source decides it), "conflict" (sources disagree) or "unknown" (no source found). Quote the deciding sentences, name the policy section or page, and give the date of each source. If it is a conflict, say which source is newer, which is the policy text, and who at NC Medicaid or DHSR can settle it (office, phone, email, only if on an official page).

Q1. ACCREDITATION DEADLINE. When must each service be nationally accredited: Peer Support (CCP 8G), SAIOP (CCP 8A-12) and SACOT (CCP 8A-13)? The CCPs (effective Jan 1, 2026, section 6.1) appear to say 1 year from enrollment. The Provider Permission Matrix (Aug 16, 2026) appears to say 3 years for SAIOP and SACOT and 1 year for peer support. NC Medicaid's April 16, 2026 bulletin "post-enrollment national accreditation update" and an April 2026 NCTracks notice also address it. Also: when does the clock start (enrollment, service selection, license date)? Which bodies are accepted (COA, The Joint Commission, CARF, CQL)? Is any later notice (May to October 2026) newer than the April bulletin?

Q2. DOES A PEER-SUPPORT-ONLY PROVIDER NEED A DHSR LICENSE? The Provider Permission Matrix shows no DHSR license for Peer Support, and DHSR's new-provider presentation does not list it as a licensed service. Is peer support a "mental health, developmental disabilities or substance abuse facility" under G.S. 122C-3(14), or otherwise exempt? Does DHSR, NC Medicaid or any Tailored Plan say anything about a peer-support-only office (zoning, fire marshal, walkthrough, HCPR checks, criminal checks)?

Q3. WHO CREDENTIALS A NEW PROVIDER? One NCTracks FAQ says LME/MCOs no longer perform credentialing, but CCP 8G section 6.1 says providers must be "credentialed and contracted by" the health plan, and CCPs 8A-12 and 8A-13 say "credentialed and contracted by the DHHS designated contractor." What does each plan (Alliance, Trillium, Vaya Partners) still require after NCTracks enrollment: forms, CAQH, primary-source documents, roster forms, contract steps? What is the new NC DHHS Provider Credentialing Committee's role, and since when? Date each source.

Q4. WHAT DO THE CHECKS COST? (a) NCTracks fingerprinting for owners with 5% or more ownership: the price a provider actually pays at a sheriff's office or approved vendor, and how fees are collected. (b) The NC SBI state-only criminal check fee and the fingerprint-based national check fee for employees under G.S. 122C-80 (the SBI access form shows $38 per fingerprint card; confirm whether that is the national check). (c) How a not-yet-licensed applicant runs checks, given that DHSR's ABCMS system needs a facility license number. (d) Any DHHS Criminal Records Check Unit fee. Give amounts only if a source shows them.

Q5. VAYA PARTNERS INTAKE AFTER OCT 1, 2026. For counties formerly served by Partners, which intake page, form, email and phone should a new provider use? Is Vaya Partners accepting new contracting requests (Partners paused them on Aug 1, 2026)? Which provider portal, claims platform and payer ID apply now? Confirm the payer IDs reported earlier: Alliance 23071, Trillium 43072, Vaya Partners 13010.

Q6. NC HEALTHCONNEX FOR NEW PROVIDERS. G.S. 90-414.4 required connection by Jan 1, 2023. Does a provider that starts billing after that date get any grace period? Does NC Medicaid, NCTracks or any Tailored Plan require proof of connection before billing or credentialing? Should a SAIOP or SACOT program that holds 42 CFR Part 2 records sign the Full or the Submission-only agreement?

Q7. NCTRACKS HIGH-RISK ENROLLMENT. For taxonomy 251S00000X: who performs the pre-enrollment site visit (Public Consulting Group?), how a provider schedules or tracks it, what the visitor checks, how long enrollment typically takes, and whether the site visit and fingerprinting waiver for nationally accredited providers (Sept 14, 2026 bulletin) applies to a brand-new provider that is not yet accredited.

Q8. PEER SUPPORT CLOSED-NETWORK DATE. Quote the effective-date section of Session Law 2026-41 (Senate Bill 257) and the NC Medicaid mandatory closed networks fact sheet. Which date governs, July 2 or July 7, 2026, and does any Tailored Plan publish its own date or current needs for Peer Support?

OUTPUT: one valid JSON object in a json code block with keys "q1" to "q8". Each value: {"status": "settled|conflict|unknown", "answer": "", "quotes": [{"text": "", "source": "", "section": "", "date": ""}], "whoCanSettle": "", "sources": [], "confidence": "high|medium|low", "verify": ""}.

---

# perplexity response

```json
{
 "q1": {
  "status": "conflict",
  "answer": "Peer Support (8G): 1 year, all sources agree. SAIOP (8A-12) and SACOT (8A-13): CONFLICT. G.S. 122C-81(d) and CCP 8A-12/8A-13 section 6.1 (amended Jan 1, 2026) say within one year of NC Medicaid enrollment; the April 16, 2026 bulletin, the May 28, 2026 NCTracks notice and the Aug 16, 2026 Provider Permission Matrix (PPM) say within three years of enrollment in the new service. The statute and the policy text are the more authoritative; the PPM is the newer document and is what NCTracks monitors. The only 3-year period in G.S. 122C-81 is subsection (c), which covers providers enrolled before July 1, 2008. Plan for 1 year for all three services until NC Medicaid confirms in writing. Clock start: the bulletin, NCTracks notice and PPM tie it to initial enrollment with the selected Service in NCTracks (PPM: \"enrollment of new service\"); the statute and CCPs say enrollment as a NC Medicaid provider. Neither is the DHSR license date. Accepted bodies: G.S. 122C-81(a) leaves approval of accrediting entities to the Secretary (no bodies named); the April bulletin lists COA, JCAHO, CARF for all three services; the Aug 16, 2026 PPM adds CQL for all three. CQL is therefore a second conflict (newer PPM vs. April bulletin). The Sept 14, 2026 bulletin adding CQL names only Innovations Waiver and certain CIS services, not 8G, 8A-12 or 8A-13. Newer than April: May 28, 2026 NCTracks notice (repeats 1 or 3 years; required Service selection by Aug 1, 2026) and Sept 14, 2026 bulletin. The Sept 1, 2026 amended CCP 8G keeps the one-year rule. No May to Oct 2026 notice found that changes the SAIOP/SACOT timing.",
  "quotes": [
   {"text": "d. within one calendar year of enrollment as a provider with NC Medicaid, achieve national accreditation with at least one of the designated accrediting agencies", "source": "CCP 8G Peer Support Services", "section": "Section 6.1(d)", "date": "Amended Sept 1, 2026"},
   {"text": "achieves national accreditation with at least one of the designated accrediting agencies within one (1) year of enrollment as a provider with NC Medicaid", "source": "CCP 8A-12 SAIOP and CCP 8A-13 SACOT", "section": "Section 6.1(d)", "date": "Amended Jan 1, 2026"},
   {"text": "Within three years of enrollment in new service | SUBSTANCE ABUSE INTENSIVE OUTPATIENT PROGRAM | COA; JCAHO; CARF", "source": "NC Medicaid bulletin Post-Enrollment National Accreditation Update", "section": "Accreditation table", "date": "April 16, 2026"},
   {"text": "it must be obtained within one or three years of the provider's initial enrollment with the selected service", "source": "NCTracks announcement for 251S00000X providers", "section": "Update Details", "date": "May 28, 2026"},
   {"text": "SAIOP and SACOT rows: YES WITHIN 3 YEARS OF ENROLLMENT OF NEW SERVICE. Peer Support rows: YES WITHIN 1 YEAR OF ENROLLMENT OF NEW SERVICE.", "source": "Provider Permission Matrix 08-16-2026", "section": "Taxonomy 251S00000X, CIS Services rows, column DOES-SRVC-RQRE-ACCREDITATION", "date": "Aug 16, 2026"},
   {"text": "SERVICE-ACCREDITATION-TYP values for Peer Support, SAIOP and SACOT: CARF, JCAHO, COA, COUNCIL ON QUALITY AND LEADERSHIP (CQL)", "source": "Provider Permission Matrix 08-16-2026", "section": "Taxonomy 251S00000X rows", "date": "Aug 16, 2026"},
   {"text": "Council on Quality and Leadership (CQL) has been added to the PPM as a selectable accrediting body for multiple CIS and Innovations Waiver Services.", "source": "NC Medicaid bulletin Recent Behavioral Health Enrollment Updates for Organizations", "section": "Innovations Waiver Program and CIS Enrollment Updates", "date": "Sept 14, 2026"}
  ],
  "whoCanSettle": "NC Medicaid via NCTracks Call Center 800-688-6696 or NC Medicaid Provider Ombudsman 866-304-7062 (both listed on the April 16, 2026 and Sept 14, 2026 bulletins). Ask for a written answer on 1 vs 3 years for SAIOP/SACOT and on whether CQL is accepted for 8G, 8A-12 and 8A-13.",
  "sources": [
   "https://medicaid.ncdhhs.gov/8g-peer-support-services/download?attachment",
   "https://medicaid.ncdhhs.gov/media/15767/download?attachment",
   "https://medicaid.ncdhhs.gov/media/15769/download?attachment",
   "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_122C/GS_122C-81.html",
   "https://medicaid.ncdhhs.gov/blog/2026/04/16/post-enrollment-national-accreditation-update",
   "https://www.nctracks.nc.gov/content/public/providers/provider-communications/2026----Announcements/Important-Update-for-NC-Medicaid-Organizational-Providers-with-an-Active-251S00000X-Taxonomy.html",
   "https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx",
   "https://medicaid.ncdhhs.gov/blog/2026/09/14/recent-behavioral-health-enrollment-updates-organizations",
   "https://medicaid.ncdhhs.gov/blog/2026/10/02/amendment-clinical-coverage-policy-8g-peer-support-services"
  ],
  "confidence": "high",
  "verify": "Read G.S. 122C-81(d) yourself (it sets one year from enrollment for providers enrolled after July 1, 2008) and have a healthcare attorney weigh it against the PPM 3-year value. Recheck the live PPM for a newer version than 08-16-2026 before setting app deadlines."
 },
 "q2": {
  "status": "settled",
  "answer": "A peer-support-only provider does not need a DHSR mental health license. DHSR's Feb 10, 2026 new-provider presentation lists Peer Support Services among services it does NOT license, and the Aug 16, 2026 PPM shows DOES-SRVCE-RQRE-LICENSE = NO for Peer Support (YES for SAIOP and SACOT). Statute: a peer support office can still be a \"facility\" under the broad G.S. 122C-3(14) definition, but licensure under Article 2 attaches to a \"licensable facility\", which G.S. 122C-3(14)b limits to day services offered to the same individual for 3 hours or more in 24 hours, or residential services of 24 consecutive hours or more; peer support is a periodic service, so it is not licensable (this reading is an inference; DHSR's own slide is the direct evidence). No DHSR walkthrough, zoning or fire-marshal sign-off tied to licensure applies (local zoning and fire codes still apply to any business; NOT VERIFIED for any peer-specific rule). Background checks still apply in other ways: G.S. 131E-256 requires Health Care Personnel Registry checks by \"health care facilities\", which include community-based providers of MH/DD/SA services that do not require licensure; G.S. 122C-80 fingerprint/state checks apply only to providers licensable under Article 2, so they do not strictly bind a peer-only agency, but NCTracks fingerprints owners of high-risk 251S00000X providers, and plan contracts may add screening requirements (NOT VERIFIED for each plan).",
  "quotes": [
   {"text": "The Licensure & Training Section does NOT license: ... Peer Support Services", "source": "DHSR Mental Health Licensure and Certification Section new-provider presentation", "section": "Slide: services not licensed", "date": "Feb 10, 2026"},
   {"text": "These services shall be day services offered to the same individual for a period of three hours or more during a 24-hour period", "source": "G.S. 122C-3(14)b", "section": "Definitions", "date": "Current statute text (undated web page)"},
   {"text": "\"provider\" applies to an area authority/county program and any provider of ... substance abuse services that is licensable under Article 2", "source": "G.S. 122C-80(a)", "section": "Definition", "date": "Current statute text (undated web page)"},
   {"text": "Community-Based Providers of Services for the Mentally Ill, the Developmentally Disabled, and Substance Abusers that are not required to be licensed", "source": "G.S. 131E-256 (health care facility definition for HCPR)", "section": "131E-256, subdivision (12)", "date": "Current statute text (undated web page)"},
   {"text": "Peer Support Services: DOES-SRVCE-RQRE-LICENSE = NO; SAIOP and SACOT: YES", "source": "Provider Permission Matrix 08-16-2026", "section": "Taxonomy 251S00000X rows", "date": "Aug 16, 2026"}
  ],
  "whoCanSettle": "DHSR Mental Health Licensure and Certification Section (phone and email not captured from an official page in this pass; NOT VERIFIED). For HCPR questions, the DHSR Health Care Personnel Registry.",
  "sources": [
   "https://info.ncdhhs.gov/dhsr/mhlcs/pdf/newprovider.pdf",
   "https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx",
   "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_122C/GS_122C-3.html",
   "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_131E/GS_131E-256.html",
   "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_122C/GS_122C-80.html",
   "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-fingerprinting.html",
   "https://resources.vayapartners.org/wp-content/uploads/Vaya_Partners_Provider_Operations_Manual_1.0_20261001.pdf"
  ],
  "confidence": "high",
  "verify": "Check local zoning and fire inspection rules for the office address with the city or county; they are not tied to DHSR licensure."
 },
 "q3": {
  "status": "conflict",
  "answer": "Two layers, and the sources use the word \"credentialed\" differently. (1) State credentialing: NC DHHS through NCTracks verifies credentials for all providers; the NCTracks Behavioral Health FAQ (updated May 8, 2025) says LME/MCOs no longer perform credentialing. The NC Medicaid Credentialing Committee (page updated Oct 15, 2026) reviews provider files with flagged items for enrollment, reenrollment and recredentialing, applies to all NC Medicaid Managed Care health plans, and meets weekly on Wednesdays; its fact sheet is dated March 25, 2025, bylaws Nov 13, 2025, and the earliest archived meeting is Oct 8, 2025 (formal start date NOT VERIFIED). (2) Plan contracting: CCP 8G section 6.1 (amended Sept 1, 2026) says \"credentialed and contracted by\" the PHP/PIHP, and CCPs 8A-12/8A-13 (amended Jan 1, 2026) say \"credentialed and contracted by the DHHS designated contractor\". Read together, NCTracks does the credential verification and the plan decides network admission and signs the contract. Plan steps: Alliance (page dated July 2, 2026): be enrolled in NCTracks first, submit a completed Provider Application request, decision on network need within five business days, then contracting via DocuSign; requires $1M/$3M professional and general liability. Trillium (pages Oct 5, 2026): uses the NCTracks Provider Enrollment File; peer support and certain services are closed; other Medicaid services by emailing NetworkServicesSupport@TrilliumNC.org. Vaya Partners (POM v1.0, Oct 1, 2026): submit a Provider Contract Request Form; closed-network initial enrollment criteria include an EHR able to send HL7 to NC HealthConnex and fiscal stability (one month working capital, no tax liens). CAQH: no plan page reviewed requires CAQH for agencies (NOT VERIFIED). No separate plan primary-source verification packet was found; roster forms NOT VERIFIED.",
  "quotes": [
   {"text": "A Credentialing Committee has been established and is responsible for reviewing provider files that contain flagged items", "source": "NC Medicaid Credentialing Committee page", "section": "Overview", "date": "Updated Oct 15, 2026"},
   {"text": "Is the NCTracks process taking the place of the LME/MCO credentialing process? Yes... The LME/MCOs no longer perform credentialing.", "source": "NCTracks FAQs for Behavioral Health Provider Enrollment", "section": "FAQ 9", "date": "Updated May 8, 2025"},
   {"text": "c. demonstrates that it meets these standards by being credentialed and contracted by the DHHS designated contractor", "source": "CCP 8A-12 and CCP 8A-13", "section": "Section 6.1(c)", "date": "Amended Jan 1, 2026"},
   {"text": "The Department, through NCTracks, will continue to collect information and verify credentials for all providers currently enrolled or seeking to enroll", "source": "Trillium Contracting Information", "section": "Credentialing", "date": "Oct 5, 2026 (page date)"},
   {"text": "Providers are required to submit a fully completed Provider Application request to be considered for a network contract.", "source": "Alliance Health Provider Enrollment", "section": "Application and Contracting Information", "date": "July 2, 2026 (page date)"},
   {"text": "All non-hospital providers... must apply for enrollment in the Vaya Partners network by submitting a completed Provider Contract Request Form.", "source": "Vaya Partners Enrollment page", "section": "How to join", "date": "Undated (site launched Oct 1, 2026)"}
  ],
  "whoCanSettle": "NCTracks Call Center 800-688-6696 for state credentialing; Alliance NetworkRelations@AllianceHealthPlan.org; Trillium NetworkServicesSupport@TrilliumNC.org; Vaya Partners Provider Enrollment Services 1-855-432-9139 or ProviderEnrollment@VayaPartners.org.",
  "sources": [
   "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-Behavioral-Health-Provider-Enrollment.html",
   "https://medicaid.ncdhhs.gov/providers/provider-enrollment/provider-credentialing/credentialing-committee",
   "https://medicaid.ncdhhs.gov/8g-peer-support-services/download?attachment",
   "https://medicaid.ncdhhs.gov/media/15767/download?attachment",
   "https://medicaid.ncdhhs.gov/media/15769/download?attachment",
   "https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/",
   "https://www.trilliumhealthresources.org/contracting-information",
   "https://www.trilliumhealthresources.org/current-service-needs",
   "https://providers.vayapartners.org/enrollment/",
   "https://resources.vayapartners.org/wp-content/uploads/Vaya_Partners_Provider_Operations_Manual_1.0_20261001.pdf"
  ],
  "confidence": "medium",
  "verify": "Ask each plan in writing for its current application form, CAQH expectation and roster template. Confirm the Credentialing Committee's start date on the NC Medicaid committee page."
 },
 "q4": {
  "status": "unknown",
  "answer": "Partly settled: the $38 national check fee is confirmed; the other amounts are not. (a) NCTracks owner fingerprinting: no official page states a dollar amount. The NCTracks Fingerprinting FAQ says the person fingerprinted pays the cost, which varies by location; wait for the NCTracks-generated form with a unique case number, and use a location from the NCTracks Fingerprinting Resources list. Price: NOT VERIFIED; call the chosen sheriff or vendor. How NCTracks/SBI processing fees are collected: NOT VERIFIED. (b) Employee checks: the SBI Non-Criminal Justice Access Agreement form posted by DHSR says $38.00 per fingerprint card for a national CHRI check, billed monthly by SBI; so $38 is the national (FBI plus state) check. The state-only check fee is capped by G.S. 143B-939 at no more than $14.00; the actual current state-check fee charged is NOT VERIFIED. G.S. 122C-80(b) requires a state check for applicants resident in NC 5 years or more and a state and national (fingerprint) check for those resident less than 5 years, and the request must be submitted within five business days of the conditional offer. The $14 cap appears in the SBI form's reprint of G.S. 143B-939; current G.S. 122C-80 now cites G.S. 143B-1209.20, so the cap's current section number is NOT VERIFIED. (c) Not-yet-licensed applicants: G.S. 122C-80 itself allows a provider to request a state check through a private entity; ABCMS is for licensed providers and the SBI agreement requires a copy of the agency license, so pre-license checks for SAIOP/SACOT hires go through a private vendor (state check) and the national check is NOT VERIFIED until licensure. A peer-only agency is not licensable, so 122C-80 does not strictly apply; use HCPR plus a private state check. (d) DHHS Criminal Records Check Unit fee: none stated; ABCMS says there is no additional cost to use ABCMS beyond the SBI charge.",
  "quotes": [
   {"text": "The person notified to complete a fingerprint-based background check will incur the cost of having their fingerprints taken, which may vary depending on location.", "source": "NCTracks FAQs for Fingerprinting", "section": "FAQ 6", "date": "Undated"},
   {"text": "The HCP agrees to pay the fee of thirty-eight ($38.00) dollars for every fingerprint card processed for a national CHRI check.", "source": "SBI Non-Criminal Justice Access Agreement (DHSR ABCMS)", "section": "Section K", "date": "Undated"},
   {"text": "The fee for the State check may not exceed fourteen dollars ($14.00).", "source": "G.S. 143B-939 as reprinted in the SBI access agreement (statute may since be renumbered)", "section": "143B-939", "date": "Undated reprint"},
   {"text": "required to pay the cost of the criminal background check currently charged by the NC SBI. There is no additional cost to use the ABCMS.", "source": "DHSR ABCMS page", "section": "Overview", "date": "Undated"}
  ],
  "whoCanSettle": "NCTracks Call Center 800-688-6696 (owner fingerprint process); NC SBI Criminal Information and Identification Section for current state and national fees (contact NOT VERIFIED); DHSR ABCMS for licensed-provider access.",
  "sources": [
   "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-fingerprinting.html",
   "https://info.ncdhhs.gov/dhsr/abcms/pdf/Non-Criminal-Justice-Access-Agreement-Form_SB-41.pdf",
   "https://info.ncdhhs.gov/dhsr/abcms/index.html",
   "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_122C/GS_122C-80.html"
  ],
  "confidence": "medium",
  "verify": "Get a written fee quote from the fingerprint location. Confirm the current SBI state-only fee and whether the $38 form is the current revision. Have an attorney confirm pre-license screening steps."
 },
 "q5": {
  "status": "conflict",
  "answer": "Partners paused new contracting requests effective Aug 1, 2026 and said the combined Vaya Partners would resume reviewing new requests on Oct 1, 2026 based on network adequacy and needs. Vaya Partners (launched Oct 1, 2026) uses one statewide intake: the Provider Contract Request Form from providers.vayapartners.org/enrollment; help at ACCESS Provider Services 1-866-990-9712 or Provider.Info@VayaPartners.org, and Provider Enrollment Services 1-855-432-9139 or ProviderEnrollment@VayaPartners.org. Vaya Partners keeps a closed behavioral health network and adds providers only for identified service needs; peer support is also a statutory closed network. No page found that says requests are actively being accepted for peer support, SAIOP or SACOT in former Partners counties (NOT VERIFIED). Payer IDs: Alliance 23071 CONFIRMED (Claims and Enrollment Guide FY2026-2027). Trillium 43072 CONFIRMED for Tailored Plan claims effective Oct 1, 2026 on the iTransact unified claims platform; Trillium says Medicaid Direct and state-funded payer IDs stay the same (values NOT VERIFIED). Vaya Partners 13010 CONFIRMED for dates of service on or after Oct 1, 2026; former Partners behavioral health claims for dates before Oct 1, 2026 use 13141. Vaya Partners provider portal and claims platform name: NOT VERIFIED (POM points to a Provider Portal webpage). Status is conflict only because the Partners notice promised resumption while Vaya Partners pages say enrollment is need-based.",
  "quotes": [
   {"text": "Effective Aug. 1, 2026, Partners Health Management will pause accepting new provider contracting requests due to the upcoming Oct. 1, 2026, merger with Vaya Health.", "source": "Partners Pauses New Contracting Requests", "section": "Notice", "date": "July 31, 2026"},
   {"text": "the combined entity will resume acceptance and review of new provider contracting requests based on network adequacy and needs.", "source": "Partners Pauses New Contracting Requests", "section": "Why", "date": "July 31, 2026"},
   {"text": "Vaya Partners Claims: Dates of Service On or After Oct. 1, 2026. Providers will use Payor ID 13010.", "source": "Vaya Provider Communication Bulletin Issue 17", "section": "Claims Submission", "date": "Sept 10, 2026"},
   {"text": "New Payer ID is 43072", "source": "Trillium Claims page", "section": "EDI via clearinghouses", "date": "Aug 3, 2026 (page date)"},
   {"text": "Utilize or inform your vendor to use the Alliance Health EDI Payer ID#: 23071.", "source": "Alliance Claims and Enrollment Guide", "section": "Electronic Data Interchange", "date": "Fiscal Year 2026-2027"}
  ],
  "whoCanSettle": "Vaya Partners Provider Enrollment Services 1-855-432-9139 or ProviderEnrollment@VayaPartners.org; ACCESS Provider Services 1-866-990-9712.",
  "sources": [
   "https://providers.partnersbhm.org/partners-pauses-new-contracting-requests/",
   "https://providers.vayapartners.org/enrollment/",
   "https://resources.vayapartners.org/wp-content/uploads/Vaya_Partners_Provider_Operations_Manual_1.0_20261001.pdf",
   "https://providers.vayahealth.com/wp-content/uploads/2026/09/pcb-09-10-26-issue-17.pdf",
   "https://www.trilliumhealthresources.org/claims",
   "https://www.alliancehealthplan.org/document-library/Claims-and-Enrollment-Guide.pdf"
  ],
  "confidence": "medium",
  "verify": "Call Vaya Partners to confirm whether it is accepting new requests for peer support, SAIOP and SACOT in former Partners counties and which portal and claims platform to use. Confirm payer IDs with your clearinghouse before first claim."
 },
 "q6": {
  "status": "unknown",
  "answer": "Grace period part is settled; the agreement-type part is unknown. Statute: G.S. 90-414.4(a1)(2) requires all other Medicaid and State-funded providers to connect by Jan 1, 2023; it contains no grace period for providers that start billing later, and the extension and exemption windows have passed. HIEA says enforcement of the mandate as a condition of receiving state funds is temporarily suspended by the Appropriations Act (Session Law 2022-74) until the General Assembly enacts enforcement reforms. No NC Medicaid or NCTracks page reviewed requires proof of connection before enrollment or billing. Vaya Partners' closed-network enrollment criteria (POM v1.0, Oct 1, 2026) require an EHR able to send HL7 messages to NC HealthConnex, which is an EHR capability test, not proof of a signed agreement. Alliance and Trillium pages reviewed say nothing (NOT VERIFIED). Agreement type for Part 2 programs: HIEA offers a Full Participation Agreement and a Submission-Only agreement, and its FAQ (June 23, 2025) says Part 2 programs generally cannot disclose data that identifies a patient as having a SUD; HIEA does not tell Part 2 programs which agreement to sign. Choice is NOT VERIFIED; ask HIEA and a Part 2 attorney. Federal Part 2 consent and redisclosure rules were not re-checked in this pass; review current 42 CFR Part 2 on eCFR before deciding.",
  "quotes": [
   {"text": "Are there restrictions on submitting substance abuse data to NC HealthConnex? ... cannot generally disclose data through to NC HealthConnex", "source": "NC HIEA Health Care Provider FAQs", "section": "Part 2 FAQ", "date": "Last updated June 23, 2025"},
   {"text": "EHRs must be able to send HL7 messages (versions 2 or higher) to communicate with the North Carolina Health Information Exchange (HIE), NC HealthConnex.", "source": "Vaya Partners Provider Operations Manual v1.0", "section": "Closed Network Enrollment and Retention Criteria", "date": "Oct 1, 2026"},
   {"text": "all other providers of Medicaid and State-funded health care services and their affiliated entities shall begin submitting demographic and clinical data by January 1, 2023.", "source": "G.S. 90-414.4(a1)(2)", "section": "90-414.4(a1)(2)", "date": "Current statute text (undated web page)"},
   {"text": "providers, regardless of connection status, may continue receiving payment of state funds for providing services (e.g., Medicaid, State Health Plan) at this time.", "source": "NC HIEA What Does the Law Mandate", "section": "Enforcement", "date": "Undated"}
  ],
  "whoCanSettle": "NC HIEA: hiea@nc.gov or 919-754-6912 (listed on hiea.nc.gov). Agreement choice under 42 CFR Part 2: a healthcare attorney.",
  "sources": [
   "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_90/GS_90-414.4.html",
   "https://hiea.nc.gov/providers/what-does-law-mandate",
   "https://hiea.nc.gov/providers/how-connect/nc-healthconnex-participation-agreement",
   "https://hiea.nc.gov/faqs/health-care-provider-faqs",
   "https://resources.vayapartners.org/wp-content/uploads/Vaya_Partners_Provider_Operations_Manual_1.0_20261001.pdf"
  ],
  "confidence": "medium",
  "verify": "Confirm no 2025-2026 session law lifted the S.L. 2022-74 enforcement suspension. Ask HIEA in writing whether a SAIOP/SACOT program should sign Full or Submission-Only and how Part 2 data is filtered."
 },
 "q7": {
  "status": "settled",
  "answer": "Taxonomy 251S00000X is high categorical risk under G.S. 108C-3(g)(2), so NCTracks requires a site visit, owner fingerprinting (5% or more ownership) and the federal application fee (PPM columns FEDERAL-SITE-VISIT-RQRD, FINGERPRINTING-REQUIRED, FEDERAL-FEE-RQRD). Public Consulting Group (PCG) is contracted by NC Medicaid to perform the site visit and the newly enrolling provider training; PCG schedules the visit and sends training links. Missing the site visit or training deadline auto-denies the application. Contact PCG at 877-522-1057. What the visitor checks: NOT VERIFIED on an opened NC page (federal site-visit rule 42 CFR 455.432 was not opened in this pass; confirm the checklist with PCG). Typical enrollment time: NOT VERIFIED; no opened official page gives a total timeline (MCRs take about 10 business days per NCTracks FAQ). Waiver: the Sept 14, 2026 bulletin waives the site visit and fingerprinting only if national accreditation is already active for the same location and service, so it does not help a brand-new, not-yet-accredited provider.",
  "quotes": [
   {"text": "Public Consulting Group (PCG) is contracted by NC Medicaid to perform the federally mandated site visit screening of Medicaid providers classified as moderate and high-risk", "source": "NCTracks FAQs for Provider Enrollment", "section": "FAQ 8 Who is PCG?", "date": "Undated"},
   {"text": "If providers fail to complete their site visit or new provider training by the deadline given, the application will automatically be denied.", "source": "NCTracks FAQs for Provider Enrollment", "section": "FAQ 8", "date": "Undated"},
   {"text": "requiring a site visit and fingerprinting unless an associated national accreditation is active for the same location and service.", "source": "NC Medicaid bulletin Recent Behavioral Health Enrollment Updates for Organizations", "section": "Innovations Waiver Program and CIS Enrollment Updates", "date": "Sept 14, 2026"}
  ],
  "whoCanSettle": "PCG 877-522-1057 (NCTracks FAQ) for scheduling and checklist; NCTracks Call Center 800-688-6696 for application status.",
  "sources": [
   "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-providerenrollment.html",
   "https://medicaid.ncdhhs.gov/blog/2026/09/14/recent-behavioral-health-enrollment-updates-organizations",
   "https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx",
   "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-fingerprinting.html",
   "https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-Behavioral-Health-Provider-Enrollment.html"
  ],
  "confidence": "high",
  "verify": "Ask PCG what the site visitor checks and how to track the visit. Ask NCTracks for current average processing times."
 },
 "q8": {
  "status": "settled",
  "answer": "July 7, 2026 governs. Section 9E.22(b) of S.L. 2026-41 (Senate Bill 257) added new subsection (e) Mandatory Closed Networks to G.S. 108D-22, and Section 9E.22(d) makes it effective when it becomes law; the act was ratified July 2, 2026 and approved by the Governor July 7, 2026. NC Medicaid's Mandatory Closed Networks page says the requirements are effective as of July 7, 2026. Alliance (page dated July 2, 2026) and Trillium (Provider Communication 006, July 23, 2026) say effective July 2, 2026, which is the ratification date, not the date the act became law; the session law controls. Plan positions: Alliance lists peer support as a mandatory closed-network service and requires its own contracting and credentialing; Trillium maintains a closed network for peer support (current service needs page Oct 5, 2026); Vaya Partners maintains a closed behavioral health network and adds providers only for identified needs. No plan page reviewed posts a current open need for peer support (NOT VERIFIED).",
  "quotes": [
   {"text": "Each PHP shall develop and maintain a closed network, and may exclude providers from that closed network, for ... (1) Peer support services.", "source": "S.L. 2026-41 (S.B. 257)", "section": "Section 9E.22(b), new G.S. 108D-22(e)", "date": "Ratified July 2, 2026"},
   {"text": "SECTION 9E.22.(d) This section is effective when it becomes law.", "source": "S.L. 2026-41 (S.B. 257)", "section": "Section 9E.22(d)", "date": "Ratified July 2, 2026"},
   {"text": "These requirements are effective as of July 7, 2026.", "source": "NC Medicaid Mandatory Closed Networks page", "section": "Mandatory closed networks", "date": "Page date not confirmed (metadata shows Jan 10, 2026, which predates the law)"},
   {"text": "Approved 10:30 a.m. this 7th day of July, 2026", "source": "S.L. 2026-41 (S.B. 257)", "section": "Signature page", "date": "July 7, 2026"},
   {"text": "Pursuant to Senate Bill 257, effective July 2, 2026, each Prepaid Health Plan (PHP) will be required to develop and maintain a mandatory closed network", "source": "Alliance Health Provider Enrollment", "section": "Closed Network", "date": "July 2, 2026 (page date)"}
  ],
  "whoCanSettle": "NC Medicaid Provider Ombudsman 866-304-7062 for state interpretation; each plan's network team (Alliance NetworkRelations@AllianceHealthPlan.org, Trillium NetworkServicesSupport@TrilliumNC.org, Vaya Partners 1-855-432-9139) for current peer support needs.",
  "sources": [
   "https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-41.pdf",
   "https://medicaid.ncdhhs.gov/providers/provider-playbook-medicaid-managed-care/fact-sheets/mandatory-closed-networks",
   "https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/",
   "https://www.trilliumhealthresources.org/article/provider-communication-006",
   "https://www.trilliumhealthresources.org/current-service-needs",
   "https://resources.vayapartners.org/wp-content/uploads/Vaya_Partners_Provider_Operations_Manual_1.0_20261001.pdf"
  ],
  "confidence": "high",
  "verify": "Section 9E.22 is on about page 275 of the S.L. 2026-41 PDF. Ask each plan whether it will accept peer support applications in your county."
 }
}
```

## SOURCES

| Title | Publisher | URL | Date | Type |
|---|---|---|---|---|
| CCP 8G Peer Support Services | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/8g-peer-support-services/download?attachment=&share_frome=aipt) | Amended Sept 1, 2026 | Primary |
| CCP 8G amendment notice | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/blog/2026/10/02/amendment-clinical-coverage-policy-8g-peer-support-services?share_frome=aipt) | Oct 2, 2026 | Primary |
| CCP 8A-12 SAIOP | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/media/15767/download?attachment=&share_frome=aipt) | Amended Jan 1, 2026 | Primary |
| CCP 8A-13 SACOT | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/media/15769/download?attachment=&share_frome=aipt) | Amended Jan 1, 2026 | Primary |
| Post-Enrollment National Accreditation Update | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/blog/2026/04/16/post-enrollment-national-accreditation-update?share_frome=aipt) | Apr 16, 2026 | Primary |
| Update for 251S00000X providers | NCTracks | link[nctracks.nc.gov](https://www.nctracks.nc.gov/content/public/providers/provider-communications/2026----Announcements/Important-Update-for-NC-Medicaid-Organizational-Providers-with-an-Active-251S00000X-Taxonomy.html?share_frome=aipt) | May 28, 2026 | Primary |
| Provider Permission Matrix | NCTracks | [link](https://www.nctracks.nc.gov/content/dam/jcr:4f0d2400-62b7-48a3-9617-ad31dd8cf543/Provider%20Permission%20Matrix%2008-16-2026.xlsx) | Aug 16, 2026 | Primary |
| Recent BH Enrollment Updates for Organizations | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/blog/2026/09/14/recent-behavioral-health-enrollment-updates-organizations?share_frome=aipt) | Sept 14, 2026 | Primary |
| G.S. 122C-81 / 122C-3 / 122C-80 | NC General Assembly | 122C-81[ncleg.gov](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_122C/GS_122C-81.html?share_frome=aipt), 122C-3[ncleg.gov](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_122C/GS_122C-3.html?share_frome=aipt), 122C-80[ncleg.gov](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_122C/GS_122C-80.html?share_frome=aipt) | Undated | Primary |
| G.S. 131E-256 / G.S. 90-414.4 | NC General Assembly | 131E-256[ncleg.gov](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_131E/GS_131E-256.html?share_frome=aipt), [90-414.4](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_90/GS_90-414.4.html) | Undated | Primary |
| S.L. 2026-41 (S.B. 257) | NC General Assembly | link[ncleg.gov](https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-41.pdf?share_frome=aipt) | Ratified July 2, approved July 7, 2026 | Primary |
| Mandatory Closed Networks | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers/provider-playbook-medicaid-managed-care/fact-sheets/mandatory-closed-networks?share_frome=aipt) | Date unclear | Primary |
| New provider presentation | DHSR MHLCS | link[info.ncdhhs.gov](https://info.ncdhhs.gov/dhsr/mhlcs/pdf/newprovider.pdf?share_frome=aipt) | Feb 10, 2026 | Primary |
| ABCMS page / SBI access agreement | DHSR / NC SBI | ABCMS[info.ncdhhs.gov](https://info.ncdhhs.gov/dhsr/abcms/index.html?share_frome=aipt), form[info.ncdhhs.gov](https://info.ncdhhs.gov/dhsr/abcms/pdf/Non-Criminal-Justice-Access-Agreement-Form_SB-41.pdf?share_frome=aipt) | Undated | Primary |
| Fingerprinting, BH enrollment, general enrollment FAQs | NCTracks | fingerprint[nctracks.nc.gov](https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-fingerprinting.html?share_frome=aipt), BH[nctracks.nc.gov](https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-Behavioral-Health-Provider-Enrollment.html?share_frome=aipt), general[nctracks.nc.gov](https://www.nctracks.nc.gov/content/public/providers/faq-main-page/faqs-for-providerenrollment.html?share_frome=aipt) | BH FAQ May 8, 2025; others undated | Primary |
| Credentialing Committee | NC Medicaid | link[medicaid.ncdhhs.gov](https://medicaid.ncdhhs.gov/providers/provider-enrollment/provider-credentialing/credentialing-committee?share_frome=aipt) | Oct 15, 2026 | Primary |
| Provider Enrollment; Claims and Enrollment Guide | Alliance Health | enrollment[alliancehealthplan.org](https://www.alliancehealthplan.org/providers/network/become-a-provider/provider-enrollment/?share_frome=aipt), guide[alliancehealthplan.org](https://www.alliancehealthplan.org/document-library/Claims-and-Enrollment-Guide.pdf?share_frome=aipt) | July 2, 2026; FY2026-27 | Primary (plan) |
| Contracting info, service needs, claims, Communication 006 | Trillium | contracting[trilliumhealthresources.org](https://www.trilliumhealthresources.org/contracting-information?share_frome=aipt), needs[trilliumhealthresources.org](https://www.trilliumhealthresources.org/current-service-needs?share_frome=aipt), claims[trilliumhealthresources.org](https://www.trilliumhealthresources.org/claims?share_frome=aipt), 006[trilliumhealthresources.org](https://www.trilliumhealthresources.org/article/provider-communication-006?share_frome=aipt) | Oct 5, Aug 3, July 23, 2026 | Primary (plan) |
| Enrollment page; Provider Operations Manual v1.0 | Vaya Partners | enrollment[providers.vayapartners.org](https://providers.vayapartners.org/enrollment/?share_frome=aipt), POM[resources.vayapartners.org](https://resources.vayapartners.org/wp-content/uploads/Vaya_Partners_Provider_Operations_Manual_1.0_20261001.pdf?share_frome=aipt) | Oct 1, 2026 | Primary (plan) |
| Provider Communication Bulletin Issue 17 | Vaya Health | link[providers.vayahealth.com](https://providers.vayahealth.com/wp-content/uploads/2026/09/pcb-09-10-26-issue-17.pdf?share_frome=aipt) | Sept 10, 2026 | Primary (plan) |
| Partners Pauses New Contracting Requests | Partners Health Mgmt | link[providers.partnersbhm.org](https://providers.partnersbhm.org/partners-pauses-new-contracting-requests/?share_frome=aipt) | July 31, 2026 | Primary (plan) |
| What the law mandates; participation agreement; provider FAQs | NC HIEA | law[hiea.nc.gov](https://hiea.nc.gov/providers/what-does-law-mandate?share_frome=aipt), agreement[hiea.nc.gov](https://hiea.nc.gov/providers/how-connect/nc-healthconnex-participation-agreement?share_frome=aipt), FAQ[hiea.nc.gov](https://hiea.nc.gov/faqs/health-care-provider-faqs?share_frome=aipt) | FAQ June 23, 2025 | Primary |

No secondary sources were used.

## OPEN QUESTIONS

- **Q1, SAIOP/SACOT accreditation deadline (1 year or 3 years) and CQL:** The statute and the coverage policies say 1 year. The newer Permission Matrix and bulletins say 3 years. Ask NC Medicaid for a written answer through the NCTracks Call Center (800-688-6696) or the Provider Ombudsman (866-304-7062). Until they answer, the app should use 1 year.
- **Q2, DHSR contact:** I didn't find a phone or email for the DHSR Mental Health Licensure and Certification Section on a page I opened. Get it from the DHSR site.
- **Q3, plan requirements:** I couldn't confirm whether any plan requires CAQH, its own roster templates, or a separate packet of primary-source documents. I also couldn't confirm when the Credentialing Committee formally started. Ask each plan's network team.
- **Q4, fees:** I couldn't confirm the owner fingerprinting price, the actual SBI state-only fee, the current statute number for the $14 cap, or how a not-yet-licensed applicant gets national checks. Ask the fingerprint location, the NC SBI, and DHSR.
- **Q5, Vaya Partners:** I couldn't confirm whether it is taking new requests for peer support, SAIOP or SACOT in former Partners counties, or the name of its portal and claims platform. Call Vaya Partners Provider Enrollment at 1-855-432-9139. I also didn't find Trillium's Medicaid Direct and state-funded payer IDs.
- **Q6, HealthConnex for SUD programs:** No source says whether a SAIOP or SACOT program should sign the Full or Submission-Only agreement. Ask NC HIEA (hiea@nc.gov, 919-754-6912) and a 42 CFR Part 2 attorney.
- **Q7, site visit:** I couldn't confirm what the site visitor checks or typical enrollment times. Ask PCG (877-522-1057) and NCTracks.
- **Q8, peer support openings:** No plan page I reviewed lists a current open need for peer support. Ask each plan for your county.

This is research, not legal advice; a healthcare attorney should confirm the accreditation deadline and the background-check steps.