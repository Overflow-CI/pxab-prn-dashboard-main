# Handoff: NC Medicaid BH Operations Navigator

Written 2026-10-22 from Claude Code session `91141d82-7be3-5ffc-bd0c-f501091745a6`.

This document lets you (or a new Claude Code session in another account) continue the work with no gaps. It lists what exists, what you asked for, what is finished, what is open, and exactly how to move over.

**Contents**

1. [Where everything is](#1-where-everything-is)
2. [What the project is](#2-what-the-project-is)
3. [Everything you asked for, verbatim](#3-everything-you-asked-for-verbatim)
4. [What you gave me (files)](#4-what-you-gave-me-files)
5. [What was built, and the current state](#5-what-was-built-and-the-current-state)
6. [Outstanding questions and decisions for you](#6-outstanding-questions-and-decisions-for-you)
7. [Time-sensitive items](#7-time-sensitive-items)
8. [Step-by-step: move to another Claude Code account](#8-step-by-step-move-to-another-claude-code-account)
9. [Prompt to paste into the new session](#9-prompt-to-paste-into-the-new-session)
10. [How to run, test and rebuild](#10-how-to-run-test-and-rebuild)
11. [What does not transfer, and known limits](#11-what-does-not-transfer-and-known-limits)
12. [Working agreements learned in this session](#12-working-agreements-learned-in-this-session)
13. [File inventory](#13-file-inventory)

---

## 1. Where everything is

| Item | Value |
|---|---|
| GitHub repository | **`Overflow-CI/pxab-prn-dashboard-main`**. https://github.com/Overflow-CI/pxab-prn-dashboard-main. The repo is owned by the `Overflow-CI` organization (moved from the `tasha-a-coder` account on or before 2026-10-22). It was first named `hello-world`, then renamed `pxab-prn-dashboard-main`. |
| Old names and addresses | `tasha-a-coder/hello-world` and `tasha-a-coder/pxab-prn-dashboard-main`. GitHub redirects both to the current address. A clone made earlier may still show one of them as its remote. See step 9 in section 8. |
| Default branch | `master` |
| Branch used so far | `claude/code-review-optimize-dty0gi` (fully merged into `master`; start new work on a new branch from `master`) |
| Main deliverable | `nc_medicaid_bh_dashboard.html` (one self-contained file, about 440 KB, version 4.0) |
| Pull requests | #1 merged (v3 optimizations). #2 merged by squash (`11a8c97`, v4.0). #3 merged by merge commit (`3558167`, checklist and sources CSV). #5 merged by merge commit (`71546f0`, specification, quick start guide and handoff). Note: the PR numbers 1, 2, 3 and 5 are as GitHub reported them; #4 was not created in this session. |
| Documentation status | Specification, quick start guide, README placeholder and this `handoff/` folder were merged into `master` by PR #5. The only later changes are the repo-name fixes in this file and `conversation_context.json` (see git history). |
| Browser storage key | `NC_MEDICAID_NAVIGATOR_FULL_STATE_V3` (unchanged since v3, so saved progress carries over) |

## 2. What the project is

A single-file, offline dashboard that guides a new North Carolina provider through starting to bill NC Medicaid for **Peer Support (CCP 8G), SAIOP (CCP 8A-12) and SACOT (CCP 8A-13)**. It has 31 steps and 116 tasks in 6 phases, researched instructions for every task, progress tracking saved in the browser, fee and timeline calculations, county-based Tailored Plan contacts, NC ROOTS hub contacts, and a printable PDF plan. Full detail: `docs/SPECIFICATION.md`. User guide: `docs/QUICK_START.md`.

The researched content came from Perplexity research runs that **could not be independently verified** (NC government sites returned 403 from the build sandbox). That is why the verification checklist exists.

## 3. Everything you asked for, verbatim

Your messages, in order. Attached files appear as `@"path"`; those files are in `handoff/inputs/` (see section 4). Messages that only echoed a slash command are omitted.

1. `2026-09-23 09:19 UTC`

   > @"/root/.claude/uploads/91141d82-7be3-5ffc-bd0c-f501091745a6/5d3fd634-nc_medicaid_behavioral_health_operations_compliance_dashboard_v003.html" Review and optimize this code.

2. `2026-09-23 19:20 UTC`

   > A pull request was just created for this branch from the Claude Code UI: https://github.com/tasha-a-coder/hello-world/pull/1
   > 
   > You don't need to create one. Reference this PR going forward — pushing more commits to this branch will update it.

3. `2026-09-23 19:38 UTC`

   > Make the fees and timeline metrics calculate from the data.  Restore the code to a single HTML file.  Rename the repository "pxab-prn-dashboard-main"

4. `2026-09-27 00:59 UTC`

   > I've renamed it.

5. `2026-10-18 04:14 UTC`

   > Done

6. `2026-10-18 04:16 UTC`

   > Yes, update the PR description

7. `2026-10-18 04:20 UTC`

   > Yes, update the title too

8. `2026-10-18 04:20 UTC`

   > Merge the PR

9. `2026-10-18 04:56 UTC`

   > Add a print feature, that let's the user print their plan as an easy to follow PDF document reflecting the user's progress, status, and notes.  Then, improve the usability of the app, using a mobile first design.

10. `2026-10-18 05:26 UTC`

   > Yes, open a PR.  I want to make more changes, before committing this new version 4.0

11. `2026-10-18 05:28 UTC`

   > Add a button on each checklist row, that when clicked, displays instructions for that task.

12. `2026-10-18 05:35 UTC`

   > Write a comprehensive prompt for perplexity.ai to retrieve the 79 sets of instructions.

13. `2026-10-18 06:28 UTC`

   > I don't see the tasks to comply with the H.R. 1.  Please add those to the app.  Then, give me the prompts again.

14. `2026-10-18 11:13 UTC`

   > @"/root/.claude/uploads/91141d82-7be3-5ffc-bd0c-f501091745a6/e2ba9bfa-Verify-NC-Medicaid-Service-Foundations.json"

15. `2026-10-19 00:04 UTC`

   > We can't use perplexity for this research.  Let's use Gemini Notebook instead

16. `2026-10-19 03:01 UTC`

   > @"/root/.claude/uploads/91141d82-7be3-5ffc-bd0c-f501091745a6/b6578139-Batch-1.md" @"/root/.claude/uploads/91141d82-7be3-5ffc-bd0c-f501091745a6/c76eb3cc-Batch-2.md" @"/root/.claude/uploads/91141d82-7be3-5ffc-bd0c-f501091745a6/e2fc2fa1-Batch-3.md" @"/root/.claude/uploads/91141d82-7be3-5ffc-bd0c-f501091745a6/7f94bbb3-Batch-4.md" @"/root/.claude/uploads/91141d82-7be3-5ffc-bd0c-f501091745a6/67238f60-Batch-5.md" Perplexity finished the research.  Here is the first of 2 messages with the responses.

17. `2026-10-19 03:11 UTC`

   > Yes, write the follow-up prompt

18. `2026-10-19 03:48 UTC`

   > @"/root/.claude/uploads/91141d82-7be3-5ffc-bd0c-f501091745a6/fa1410a7-p1-North-Carolina-Tailored-Plan-County-Map.md" @"/root/.claude/uploads/91141d82-7be3-5ffc-bd0c-f501091745a6/cf31e7cb-p2-NC-Medicaid-Regions-and-ROOTS-Contacts.md" @"/root/.claude/uploads/91141d82-7be3-5ffc-bd0c-f501091745a6/85a87b71-p3-NC-Medicaid-Accreditation-Deadlines.md"

19. `2026-10-19 04:01 UTC`

   > Mark the PR ready and merge it

20. `2026-10-19 04:09 UTC`

   > Give me a comprehensive markdown checklist of information that needs to be verified with clear instructions on how to verify the information, who to contact, how, and what to say exactly in order to verify the information.  Then, give me a CSV file of all sources used in the app and in our research, organized logically.

21. `2026-10-19 04:38 UTC`

   > I'll allow the force push

22. `2026-10-19 04:47 UTC`

   > What's the benefit of opening a PR?  What purpose would it serve in this case?

23. `2026-10-19 04:53 UTC`

   > Merge it now.  When I answer the questions in the checklist, we'll create a PR to update the app and checklist in the same session.  Create a markdown document, with full technical specification of the app.  Also, create an instructional "quick start guide" document (in markdown) for the user with screenshots to guide the user. Then,  update the read.me file with a placeholder for the quick start guide's url.

24. `2026-10-22 01:23 UTC`

   > Give me the full context of our conversation as a json file that I can download.  Also list all of the files and instructions that I gave you. I also need any outstanding questions that I need to answer or decisions that I need to make.  I need to continue development in another Claude Code account.  Tell me step by step how to transition seamlessly.  No info gaps.

### 3.1 Your requests in plain terms, with status

| # | Request | Status |
|---|---|---|
| 1 | Review and optimize the uploaded HTML | Done (PR #1, merged). |
| 2 | Make fees and timeline metrics calculate from step data | Done. |
| 3 | Keep it a single HTML file | Done. Tailwind CSS is precompiled and inlined. |
| 4 | Rename the repo to `pxab-prn-dashboard-main` | Done by you. |
| 5 | Update the PR description and title, then merge PR #1 | Done. |
| 6 | Printable PDF plan with progress, status and notes | Done (v4.0, PR #2). |
| 7 | Mobile-first usability redesign | Done (v4.0, PR #2). |
| 8 | Open a PR for v4.0 as a draft | Done, then later marked ready and merged at your request. |
| 9 | Instructions button on every checklist row | Done, all 116 rows. |
| 10 | Perplexity prompt for the instruction research | Done (`handoff/prompts/perplexity_prompts_v2.md`). |
| 11 | Add H.R. 1 compliance tasks and re-issue prompts | Done (Phase 6: 6 steps, 26 tasks). |
| 12 | Switch research to Gemini/NotebookLM | Kit written (`handoff/prompts/notebooklm_research_kit_v1.md`). You then supplied Perplexity-format results anyway. See decision D3. |
| 13 | Integrate research Batches 0, 0B and 1 to 8 | Done. |
| 14 | Follow-up research prompts (county map, regions and hubs, open policy questions) | Done (`handoff/prompts/followup_research_prompts.md`). |
| 15 | Integrate the three follow-up results (F1, F2, F3) | Done: county-based plans, corrected hub and statewide contacts, step text changes. |
| 16 | Mark PR #2 ready and merge | Done. |
| 17 | Verification checklist (what to verify, who to contact, what to say) and a sources CSV | Done and merged (PR #3). |
| 18 | Allow the force push | Done: the branch was reset to `master` once. |
| 19 | Merge it now (PR #3) | Done. |
| 20 | Full technical specification, illustrated quick start guide, and a README placeholder for the guide's URL | Done and pushed to the branch. Not yet merged. |
| 21 | This handoff (JSON of the conversation, files and instructions, open questions, transition steps) | This document and the JSON files. |

**Standing instruction from you:** when you answer the checklist questions, you want **one PR that updates the app and the checklist together, in the same session.**

## 4. What you gave me (files)

All are copied into `handoff/inputs/` with the random upload prefix removed.

| File | What it is |
|---|---|
| `nc_medicaid_behavioral_health_operations_compliance_dashboard_v003.html` | Your original dashboard (v003, 126 KB). The starting point for everything. |
| `Verify-NC-Medicaid-Service-Foundations.json` | Perplexity "Batch 0" results: corrections to the foundation facts. 132 KB. |
| `Batch-1.md` to `Batch-8.md` | Perplexity results for the 79 (later 116) task instruction sets. |
| `Batch-0B.md` | Perplexity results for the H.R. 1 foundations. |
| `p1-North-Carolina-Tailored-Plan-County-Map.md` | Follow-up F1: which Tailored Plan covers each of the 100 counties, plan contact details, closed-network date. |
| `p2-NC-Medicaid-Regions-and-ROOTS-Contacts.md` | Follow-up F2: region county lists, NC ROOTS hub contacts, statewide contacts, open funding. |
| `p3-NC-Medicaid-Accreditation-Deadlines.md` | Follow-up F3: accreditation timing, peer-support licensing, credentialing, fees, HealthConnex, site visits. |

Treat these as **cited but unverified** research.

## 5. What was built, and the current state

### 5.1 In `master` (after PR #3)
- The dashboard v4.0 with all features and the corrected, researched content.
- `README.md` (feature description).
- `NC_Medicaid_Verification_Checklist.md` and `nc_medicaid_sources.csv`.
- A stray `pm_modal.png` in the repo root (a leftover screenshot from an earlier session).

### 5.2 Added by PR #5 (now in `master`)
- `docs/SPECIFICATION.md`, `docs/QUICK_START.md`, `docs/images/` (16 screenshots).
- A `README.md` update with a **placeholder** for the quick start guide URL: the text `QUICK_START_GUIDE_URL` appears twice in one line near the top (the link text and the link target). Replace both once the guide has a published address.
- This `handoff/` folder.

### 5.3 App facts to remember
- 31 steps (Phase 1: 8, Phase 2: 8, Phase 3: 4, Phase 4: 1, Phase 5: 4, Phase 6: 6), 116 tasks.
- Fees with all three services: $1,358 to $1,705, plus $73 to $113 per staff member. Schedule: 31 weeks.
- With peer support only (8G): 27 steps. Steps 14, 15 and 16 (DHSR application, survey, plan of correction) now apply to SAIOP and SACOT only.
- Tailored Plans are matched **by county**: Vaya Partners 47 counties, Trillium 46, Alliance 7.
- 242 distinct source URLs are cited in the app. Steps 1 to 3 (11 task entries) are labeled "Not yet checked against sources". 3 entries have low confidence.
- Contacts carry an as-of date of 2026-10-18.

### 5.4 Research corrections already applied
The Verification checklist and the PR #2 description list them. The main ones: the Provider Ombudsman number is 866-304-7062 (877-201-3750 is the member line); the Rural Health Innovation Fund year 1 is limited to primary care and safety-net providers; the closed-network effective date is July 7, 2026; the accreditation deadline is shown as a conflict with "plan for 1 year"; peer support does not need a DHSR license.

## 6. Outstanding questions and decisions for you

### 6.1 Questions that need outside answers (the verification checklist)
Full scripts, contacts and an answer log are in `NC_Medicaid_Verification_Checklist.md`. The decision-critical ones (Part A) are:

| ID | Question | Who answers | Why it matters |
|---|---|---|---|
| A1 | Is the SAIOP and SACOT accreditation deadline 1 year or 3 years, when does the clock start, and is CQL an accepted accreditor? | NC Medicaid Provider Ombudsman 866-304-7062 / Medicaid.ProviderOmbudsman@dhhs.nc.gov, or NCTracks 800-688-6696 | Sets a compliance deadline. The app says plan for 1 year. |
| A2 | Will Alliance, Trillium and Vaya Partners take your application for each service in each county? | Each plan's network team | Decides whether you can contract at all. |
| A3 | Does a peer-support-only office need any DHSR license, walkthrough or step? | DHSR 919-855-3795 | The app currently says no. |
| A4 | Does a new behavioral health provider qualify for the Rural Health Innovation Fund? | RHIF@nc.gov | Application due Nov 16, 2026. |
| A5 | Which portal and claims platform does Vaya Partners use after Oct 1, 2026? | Vaya Partners 1-866-990-9712 | Needed before the first claim. |

Parts B to H of the checklist hold the remaining items (NCTracks, plans, background checks, local fire and zoning, HealthConnex, accreditation fees, H.R. 1 items), and Part I lists the estimates that are not yet backed by real quotes.

### 6.2 Decisions only you can make

| ID | Decision | Options and my recommendation |
|---|---|---|
| D1 | **Which services will you actually offer, and in which counties?** | Not stated anywhere in the conversation. It decides which steps matter and which plan intake status applies. Recommendation: say so in the next session and I will set the filters in the checklist scripts. |
| D2 | **How to deliver the next round of changes** | Answers to the checklist will update the app and the checklist (your instruction: one PR, same session). Recommendation: start a new branch from `master`. |
| D3 | **Which research tool to use for the next research round.** | You said Perplexity could not be used and asked for Gemini/NotebookLM, then supplied Perplexity-format results. A NotebookLM kit exists. Please confirm which you will use. |
| D4 | ~~Merge the documentation branch?~~ | Done: merged by PR #5. |
| D5 | **Where to publish the quick start guide, so the README placeholder can be filled.** | Options: link to `docs/QUICK_START.md` on GitHub, publish with GitHub Pages, or host elsewhere. Tell me the URL. |
| D6 | **Where to host the app itself** (optional). | Today you open the HTML file locally. GitHub Pages would give users a link. Not requested yet. |
| D7 | **Keep the planning assumption "plan for 1 year" for accreditation until NC Medicaid answers?** | Recommended. Confirm. |
| D8 | **Remove the stray `pm_modal.png` from the repo root?** | Recommended. Not done because you did not ask. |
| D9 | **Commit the test scripts to the repo?** | They are in `handoff/tools/`. Keep them there, or move them to a `tests/` folder. |
| D10 | **Research Steps 1 to 3** (11 task entries from your original file, never checked against sources). | A fourth research batch would close the gap. Not requested yet. |
| D11 | **Open or resolve the 3 low-confidence entries** (Step 5 Trillium and Partners insurance wording; Step 13 posted occupancy signs; Step 25 CARF demonstration period). | Covered by checklist parts C2, E1 and G1. |

### 6.3 Open factual gaps (also in the checklist)
Owner fingerprinting price; current SBI state check fee (only the $38 national fee is confirmed); whether Vaya Partners accepts new requests in the former Partners counties; Full versus Submission-Only HealthConnex agreement for a Part 2 program; Trillium ROOTS mailbox spelling (Region2NCRootsHub@ versus Region2RootsHub@); several hub phone numbers and named contacts that are not published; Provider Ombudsman hours.

## 7. Time-sensitive items

Dates from the research. Today is 2026-10-22.

| Date | Item | Days left |
|---|---|---|
| 2026-11-05 | NC draft medical frailty policy, DSS-8209 attestation and code list: public comment closes (see Step 28). | 14 |
| 2026-11-16, 11:59 p.m. | Rural Health Innovation Fund application deadline. | 25 |
| 2027-01-01 | H.R. 1 work requirement and six-month renewals begin for expansion adults. | |
| 2027-07-01 | NC raises copays to the federal maximum. | |

## 8. Step-by-step: move to another Claude Code account

Do these in order. Steps 1 to 4 are on the account you use now. Steps 5 to 15 are on the new account.

### On the current account

**Step 1. Get all work into GitHub.**
Everything must be pushed because the cloud session's disk is temporary.
- Everything is merged into `master` (PR #5). The branch `claude/code-review-optimize-dty0gi` is fully merged.
- The repo-name corrections in this file are committed after PR #5. If they are not in `master` yet, merge them (or tell the new session to start from the branch that holds them).

**Step 2. Download the handoff files.**
Download these three files from this chat (they were also sent as file attachments), or from the repo under `handoff/`:
- `handoff/HANDOFF.md` (this document)
- `handoff/conversation_context.json` (structured context)
- `handoff/conversation_transcript.json` (every message from this session)

**Step 3. Save your own copy of the files you uploaded.**
They are already in `handoff/inputs/`. If your repository is private, that is fine. If it is public, remember that the research files are now public too.

**Step 4. Export your app progress, if you have any.**
Open the dashboard, tap **Export**, and keep the downloaded JSON. Progress lives in your browser, not in the repo.

### On the new account

**Step 5. Make sure the new account can reach the repository.**
- *Same GitHub user on both Claude accounts:* connect GitHub at https://claude.ai/connect-github in the new Claude account, and install the Claude GitHub App on the repo at https://github.com/apps/claude/installations/select_target.
- *Different GitHub user:* in GitHub, go to the repo, **Settings → Collaborators**, and add the new user with **Write** access. Then have that user accept the invite, connect GitHub in the new Claude account, and install the Claude app on the repo. If you will not grant write access, have them **fork** the repo, and work in the fork.
- *The repo is now owned by the `Overflow-CI` organization.* Whichever GitHub user the new Claude account connects must be a member or outside collaborator of `Overflow-CI` with write access to this repo, and an organization owner may need to approve the Claude GitHub App. Ask an owner of `Overflow-CI` for this. Without it, the new account cannot read or push to the repo.

**Step 6. Start a new Claude Code session on that repo.**
- On the web: go to https://claude.ai/code, choose the repository `Overflow-CI/pxab-prn-dashboard-main`, and choose the branch (see step 1). Use `master`, since the documentation is merged. Start the session.
- Or in a terminal: `git clone https://github.com/Overflow-CI/pxab-prn-dashboard-main.git`, then `cd pxab-prn-dashboard-main`, then run `claude`. You are on `master`, which has everything. Create a new branch for new work.

**Step 7. Paste the starter prompt (section 9)** as your first message. It tells the new session to read this file, the specification and the checklist before doing anything.

**Step 8. Attach the answers to your questions.**
If you already have answers to checklist items, paste them in the first message, or add them to the checklist file's answer log and commit. The new session will update the app and the checklist in one PR.

**Step 9. Fix the git remote on any older clone.**
If a clone was made before the rename: `git remote set-url origin https://github.com/Overflow-CI/pxab-prn-dashboard-main.git`. A fresh clone does not need this.

**Step 10. Check the tools work.**
- Needs Node 18 or later, Python 3, and Chromium. The Claude Code web environment has Chromium at `/opt/pw-browsers/chromium`. For a local machine, install Chromium and set `CHROMIUM=/path/to/chromium`.
- Install dependencies once: `cd handoff/tools && npm install`.
- Run a test: `node t_p6.js`. It should print results ending with `errors []`.

**Step 11. Set the permissions you used here.**
The previous session needed a permission to **force-push** after a squash merge. A new account will start with its own permission settings. If you will need force pushes, grant them in that account's settings. A safer habit: merge pull requests with **merge commits** (not squash) when you plan to keep working on the same branch, so no force-push is needed.

**Step 12. Check network access for research.**
The NC government sites (ncdhhs.gov, medicaid.ncdhhs.gov, nctracks.nc.gov) returned **403** from the old sandbox, so none of the sources could be checked first-hand. In the new environment, test one of them. If they are blocked, look at the environment's network policy (in Claude Code on the web: the environment settings, then network access) and allow those hosts if your plan lets you. This lets the new session verify sources itself.

**Step 13. Decide the model.**
This session ran on `claude-sonnet-5-5` (selected with `/model claude-sonnet-5-5` on 2026-10-18). The new session will use its account's default. Pick the model you want with `/model`.

**Step 14. Do not rebuild old context by hand.**
The new session has no memory of this conversation. It learns everything from the repo: this file, `docs/SPECIFICATION.md`, `NC_Medicaid_Verification_Checklist.md`, `nc_medicaid_sources.csv`, and `handoff/conversation_transcript.json` if it needs the exact history.

**Step 15. Confirm the transition worked.**
Ask the new session to report, without changing anything: the current branch and latest commit; the number of steps (31) and tasks (116); the result of `node t_main.js` and `node t_details.js` (both end with no errors); and the list of open decisions from section 6. If any of these differ, stop and compare with this document.

## 9. Prompt to paste into the new session

```
I am continuing work from another Claude Code account. The repository is
Overflow-CI/pxab-prn-dashboard-main. Start on the master branch and create a
new branch for new work (the old branch claude/code-review-optimize-dty0gi is fully merged).

Before doing anything, read these files in order:
1. handoff/HANDOFF.md  (what exists, what I asked for, open decisions, how to test)
2. docs/SPECIFICATION.md  (technical specification of the app)
3. NC_Medicaid_Verification_Checklist.md  (facts that still need verifying)
4. handoff/conversation_context.json  (structured summary)
Only open handoff/conversation_transcript.json if you need exact earlier wording.

Then report back, without changing anything: the branch and latest commit, the app
counts (31 steps, 116 tasks), and the list of open decisions from section 6 of
HANDOFF.md. Wait for my answers.

Rules I want you to keep:
- The app stays ONE self-contained HTML file (nc_medicaid_bh_dashboard.html).
- New Tailwind classes need the CSS rebuilt (handoff/tools/rebuild.py).
- Do not change the localStorage key NC_MEDICAID_NAVIGATOR_FULL_STATE_V3.
- When I give you answers to the verification checklist, update the app AND the
  checklist in ONE pull request, in the same session.
- Do not mark facts as verified unless an official source was actually opened.
  Say "NOT VERIFIED" otherwise.
- Do not create a pull request, merge, or force-push unless I ask.
```

## 10. How to run, test and rebuild

All commands run from the repo root unless noted.

**Open the app:** double-click `nc_medicaid_bh_dashboard.html`. No server or build is needed.

**Install tools (once):** `cd handoff/tools && npm install` (installs `playwright-core` and `tailwindcss`).

**Run tests** (from `handoff/tools`; each prints results and ends with `errors []`):

| Script | What it checks |
|---|---|
| `node t_main.js` | Phone layout: filters, step cards, row taps, dialogs, touch target sizes, no horizontal scroll. |
| `node t_desk.js` | Desktop layout, keyboard handling, note escaping, partial import, reset and reload. |
| `node t_p6.js` | Phase 6, tabs and pager, 8G-only filter, print report. |
| `node t_instr.js` | The Instructions button on every row, on phone and desktop. |
| `node t_details.js` | All 116 instruction dialogs: content, links, confidence pills. |
| `node t_print.js` | Print dialog and report. |
| `node t_plans.js` | Plan, hub and statewide cards for sample counties. |
| `node qs_shots.js` | Regenerates the quick start screenshots into `docs/images/`. |

Environment variables: `CHROMIUM` (path to a Chromium binary, default `/opt/pw-browsers/chromium`) and `APP_URL` (default: the HTML file in the repo root).

Expected values you can check against: `t_p6.js` prints `0 / 31 Steps Done`, `of 116 items`, and `8G only: steps` as `0 / 27 Steps Done`. `t_details.js` should report `dialogs opened` 116, `missing review block` as an empty list, `generic note shown (should be none)` as an empty list, and a confidence-pill count of 11 for "Not yet checked against sources", 41 high, 61 medium and 3 low.

**Rebuild the inlined Tailwind CSS** (needed only after adding new Tailwind classes): `cd handoff/tools && python3 rebuild.py`. Equivalent documented command: `npx tailwindcss@3 --content nc_medicaid_bh_dashboard.html --minify -o tw.css`, then paste the output into the first `<style>` block.

**Regenerate the sources CSV:** `handoff/tools/reference/mksrc.py` (reference only; it read research files from the old session paths and needs its paths edited).

**Reference scripts** in `handoff/tools/reference/` (`integrate*.py`, `gen_*.py`, `mksrc.py`, `mk_transcript.py`) are the one-off scripts used to apply research and generate prompts. They contain absolute paths from the old session. Use them to understand how changes were made, not as a ready tool.

## 11. What does not transfer, and known limits

| Does not transfer | What to do |
|---|---|
| The conversation memory and the model's working context | Use this handoff and the transcript. |
| The raw session log (21 MB, includes tool output) | Not included. `conversation_transcript.json` has all user and assistant text, with tool calls listed briefly. |
| The session scratchpad (temp files) | Everything useful was copied into `handoff/`. The rest was disposable (intermediate PDFs, screenshots). |
| Permissions and settings (force-push allowance, model choice) | Set again in the new account. See steps 11 and 13. |
| GitHub PR subscriptions and scheduled check-ins | None are active. All three PRs are merged. |
| Your browser-saved progress in the app | Use Export in the old browser and Import in the new one. |

**Known limits of the content and tests:** research is unverified (see section 2); only headless Chromium was tested, not real phones or a real print dialog; page numbers in print need Chrome or Edge; some tests need the Chromium path set.

**Not in this handoff, and why:** the original contents of the Perplexity web pages (the research files in `inputs/` are what you pasted, not the live pages); your account email (redacted from the transcript on purpose); and anything said outside this session.

## 12. Working agreements learned in this session

- Keep the dashboard one HTML file.
- A pull request is only opened when you ask. You asked for PR #2 to be a **draft** until you were ready. You later told me to mark it ready and merge it.
- Merge pull requests on your instruction only. PR #2 was merged by squash, and PR #3 by merge commit.
- Facts from research must be labeled with confidence, and unverified facts must say "NOT VERIFIED" and who to ask.
- Commit messages in this session ended with `Co-Authored-By` and `Claude-Session` trailers. The new account's session will add its own.
- Before a force-push, ask. You approved one force-push, for resetting the branch after the squash merge.

## 13. File inventory

### Repo root
| File | Purpose |
|---|---|
| `nc_medicaid_bh_dashboard.html` | The app. |
| `README.md` | Overview, quick start (with the guide-URL placeholder), file list, feature list. |
| `NC_Medicaid_Verification_Checklist.md` | What to verify, with contacts and scripts. |
| `nc_medicaid_sources.csv` | 642 source URLs (242 cited in the app, 400 from research only), categorized. |
| `pm_modal.png` | Stray old screenshot. See decision D8. |

### `docs/`
`SPECIFICATION.md`, `QUICK_START.md`, and `images/` (16 PNGs).

### `handoff/`
| Path | Purpose |
|---|---|
| `HANDOFF.md` | This document. |
| `conversation_context.json` | Structured summary of the project, decisions, state and open items. |
| `conversation_transcript.json` | Every user and assistant message from the session, in order. |
| `inputs/` | Files you provided (14). |
| `prompts/` | The three research prompt documents written for you. |
| `research/` | Structured research data used for integration (batches, corrections, regions, counties). |
| `tools/` | Test scripts, screenshot script, Tailwind rebuild script, and `reference/` one-off scripts. |
