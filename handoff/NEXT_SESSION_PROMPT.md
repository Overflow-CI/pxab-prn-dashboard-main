# Prompt for the next Claude Code session

Paste the block below as your **first message** in the new account, in a session opened on the repository `Overflow-CI/pxab-prn-dashboard-main`, branch `master` (or the branch named in the "If something is missing" note).

Before you paste it, make sure the new account can reach the repository (see `handoff/HANDOFF.md`, section 8, steps 5 to 7). The GitHub user connected to that account needs write access to the `Overflow-CI` organization's repo, and an organization owner may need to approve the Claude GitHub App.

---

## The prompt

```
I am continuing a project from another Claude Code account. All context is in
this repository. Please read it before doing anything else.

Repository: Overflow-CI/pxab-prn-dashboard-main (default branch: master)

STEP 1. Read, in this order:
  1. CLAUDE.md  (project rules; Claude Code loads it automatically)
  2. handoff/HANDOFF.md  (what I asked for, verbatim; what is done; what is open;
     deadlines; how to run and test)
  3. docs/SPECIFICATION.md  (technical specification of the app)
  4. NC_Medicaid_Verification_Checklist.md  (facts still to verify, contacts, scripts)
  5. handoff/conversation_context.json  (the same context, structured)
Open handoff/conversation_transcript.json and handoff/inputs/ only if you need exact
earlier wording or the raw research files. nc_medicaid_sources.csv lists every source.

STEP 2. Without changing anything, check the state and report it to me:
  - the current branch and the latest commit
  - that master contains CLAUDE.md, handoff/, docs/, the checklist and the sources CSV
  - the app counts: 31 steps, 116 tasks, 242 distinct source URLs
  - the result of: cd handoff/tools && npm install && node t_main.js and node t_details.js
    (both should end with errors [])
  - whether the NC government sites (ncdhhs.gov, medicaid.ncdhhs.gov, nctracks.nc.gov)
    are reachable from this environment. They returned 403 in the last one.
If anything differs from what HANDOFF.md says, stop and tell me.

STEP 3. Give me a short list of:
  - the open decisions (HANDOFF.md section 6.2, D1 to D11) with your recommendation for each
  - the verification questions I should answer first (checklist Part A)
  - the deadlines that are coming up (HANDOFF.md section 7)
Then wait for my answers.

RULES (also in CLAUDE.md):
  - The app stays ONE self-contained HTML file: nc_medicaid_bh_dashboard.html.
  - Do not change the localStorage key NC_MEDICAID_NAVIGATOR_FULL_STATE_V3.
  - New Tailwind classes need the CSS rebuilt (handoff/tools/rebuild.py).
  - When I answer the verification checklist, update the app AND the checklist together
    in ONE pull request, in the same session. Also update docs/QUICK_START.md and
    docs/SPECIFICATION.md if the change affects them.
  - Never mark a fact as verified unless you opened an official source. Otherwise write
    NOT VERIFIED and say who to ask.
  - Do not open or merge a pull request, and do not force-push, until I ask.
  - Use a new branch from master for new work.

WHAT I AM LIKELY TO ASK NEXT (do not start these until I say so):
  - Update the app from my answers to the checklist.
  - Fill in the QUICK_START_GUIDE_URL placeholder in README.md.
  - Research Steps 1 to 3 (11 task entries never checked against sources).
  - Check the Rural Health Innovation Fund deadline (2026-11-16) and the medical frailty
    comment deadline (2026-11-05).
```

---

## If something is missing

- **The new account cannot see `CLAUDE.md` or `handoff/NEXT_SESSION_PROMPT.md` on `master`.** They were added on the branch `claude/code-review-optimize-dty0gi` and become part of `master` only when that branch is merged. Until then, open the session on that branch instead, or ask for the merge first.
- **The repository cannot be found or accessed.** The repo is owned by the `Overflow-CI` organization. Add the new account's GitHub user with write access, connect GitHub at https://claude.ai/connect-github in the new Claude account, and install the Claude GitHub App at https://github.com/apps/claude/installations/select_target.
- **Tests will not start.** Run `npm install` in `handoff/tools` first, and set `CHROMIUM=/path/to/chromium` if Chromium is not at `/opt/pw-browsers/chromium`.
- **The NC sites are blocked (403).** Research cannot be checked first-hand. Look at the environment's network settings in Claude Code on the web and allow those hosts if the plan permits.

## What the new session should do after you answer

1. Create a new branch from `master`.
2. For each checklist item you answered: change the app text, contacts or dates; update the checklist's answer log and status; update the quick start guide and specification if affected; update the sources CSV for any new source.
3. Run the test scripts in `handoff/tools`.
4. Open **one** pull request containing the app and checklist changes, when you ask for it.
