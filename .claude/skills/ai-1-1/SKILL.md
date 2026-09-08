---
name: ai-1-1
description: |
  Lesson 1.1: Files, your first task, and making it stick. Use when the learner types /ai-1-1.
disable-model-invocation: true
allowed-tools:
  - Read
  - Write
  - Edit
---

## Setup

Read `.claude/rules/teaching-rules.md` and follow it for everything below.

Lesson metadata:
- module: 1
- duration: ~20 min
- requires: ["0.1"]
- advanced: false
- data: ["data/inbox/larkspur-kickoff-notes.txt"]
- produces: ["workspace/module-1/kickoff-summary.md", "workspace/my-project/CLAUDE.md"]

# Lesson 1.1: Files, your first task, and making it stick

Module 0 was about trust. Module 1 is about work. Today you produce your first real
deliverable, the kind of thing you could actually send to a teammate.

Here's the situation: someone on the account team attended the Larkspur kickoff call and
took notes on their phone. The notes are… authentic. Buried inside them are real
commitments Tillerman needs to act on, and right now they're readable by exactly one
person. Maybe.

ACTION: Read [larkspur-kickoff-notes.txt](data/inbox/larkspur-kickoff-notes.txt) and share a
few representative lines: enough to show the mess (typos, phone-typing, buried decisions).
Don't dump the whole file; don't summarize it either. The learner does that next.

---

## Turning mess into a deliverable

Now the actual skill: you're going to direct me to turn that mess into something useful.
From here on, no copy-paste prompts. I'll tell you the *goal*, and you phrase the ask in
your own words. That's the muscle this whole course builds.

Your goal: a clean summary saved as a file in your workspace, organized so a teammate who
missed the call gets what they need in 60 seconds. Think about what sections would serve
that reader; at minimum you probably want the decisions and who-does-what.

STOP: Direct me. Tell me what to create, where to put it, and how to organize it.

USER: A prompt of their own construction: a summary of the notes, saved to workspace (any
reasonable filename/organization counts; sections like decisions/action items/deadlines
are the natural shape).

ACTION: Do exactly what they asked, no more. Create the file in `workspace/module-1/`
(suggest `kickoff-summary.md` if they didn't name it). If their instructions were vague and
the result shows it, that's the teachable moment, not a failure: show them the output and
ask if it serves the 60-second reader.

---

## Review it like it matters

STOP: Open [your summary](workspace/module-1/kickoff-summary.md) and read it as if you're
the teammate who missed the call. Two questions: is anything important missing? And is
anything in there that you can't actually find in the original notes?

USER: They check. If they spot a gap ("the deadline isn't in here") or want changes, they
direct a revision. Encourage one round of refinement in their own words.

[If they say "looks perfect" without really checking: gently push once. Name a category to
check ("did the deadline commitment make it in?") without revealing the answer.]

---

## What your prompt did

ACTION: Debrief THEIR first prompt in two or three sentences, once, no quiz. Name the trap
it brushed, or what made it tight, using their actual words:

- **vague**: named an output format but no question or reader ("a bullet point summary"),
  so I filled the gaps with guesses
- **mega**: several asks in one breath, and some got less attention than others
- **micromanager**: step-by-step instructions where naming the outcome would have done, so
  my ability to notice problems went unused

Then the knob behind all three: specify as tightly as you know what you want. Know the
exact output? Be tight. Exploring? Be open, and say so. If their prompt was already tight,
say what made it tight and name the other two traps in one clause each.

---

## Make it stick

The refinement you just asked for (more structure, shorter, headers, whatever it was) is a
preference. You shouldn't have to say it every time.

Ever notice you've never had to remind me what a shipment manifest is, or that this course
writes only in your workspace? That's not talent; it's a file.

ACTION: Read [CLAUDE.md](CLAUDE.md) and summarize in two sentences what it does: a
plain-text file of standing instructions, read at the start of every session in this
folder, and it's what turns any session here into your tutor. The punchline: the tutor
they've been talking to *is* one of these files. Anything they can write in plain English
can become standing instructions.

STOP: Now make your own. Create a project folder in your workspace with a CLAUDE.md
holding 2 or 3 standing preferences you'd actually want at work: how you like information
presented (tables? bullets? short answers?), date formats, anything real to you. Direct me
in your own words.

USER: Directs creation with their preferences.

ACTION: Create `workspace/my-project/CLAUDE.md` with their preferences. Then tell them:
from this moment, you'll honor those preferences, and in a real project folder any Claude
Code session would pick them up automatically.

---

## Wrap-up: Module 1 complete 🎓

That's the fundamental workflow you'll use forever: **point me at the input, describe the
output, review like the reader, refine.** And your preferences now travel with you. Messy
notes today; manifests, reports, and decks the same way later.

**Next up:** Module 2, automation. You'll write the business rules and the runbook for a
weekly Larkspur summary, then watch me run it and check what comes out.

STOP: Ready for 2.1? Fresh chat + /ai-2-1, or say "keep going." A break is fine too;
progress is saved.

---

## Important Notes for Claude

**GRADING KEY (commitments actually in the notes; never reveal as a list, use it to judge
their review):** weekly status must land before Larkspur's Monday leadership review
(so Friday end of day at the latest) · WA + OR lanes are priority (their retail partners)
· Q4 manifest (~250 shipments) arriving early Oct via EDI, new EDI credentials coming,
old FTP drop must not be used · focus on exception rate and on-time delivery, damage
claims "historically ugly" · flag shipments with 3+ open issues for proactive calls ·
Spanish-first delivery notifications for two receiving warehouses · next call Oct 8.

- A good summary needs MOST of that, not all; what matters is decisions + action items are
  findable. If a big one is missing (the Friday deadline is the most consequential), nudge
  with a category question, never the answer.
- The "nothing you can't find in the original" check is the anti-hallucination habit. If
  their summary contains an invented detail, that's the best teaching moment available.
- Hint ladder for prompt construction: "say what file, what output, what sections" → "start
  with: read the kickoff notes and…" → exact prompt only if they ask.
- Do NOT beautify beyond their instructions; the lesson depends on output matching what
  they actually asked for.
- Trap debrief: from their prompt, one sentence per point, no lecture, no quiz, and don't
  ask them to rewrite it (the refinement round already was the rewrite).
- CLAUDE.md preferences must be THEIRS. If they offer generic ones ("be accurate"), push
  once for something with observable effect ("what would I do differently if I followed
  it?").
- From the moment their CLAUDE.md exists, honor it for the rest of the session. The payoff
  (noticing a preference show up unprompted) lands in 2.1.
- Don't introduce data vocabulary here (manifest columns, service levels); lesson 2.1 owns it.

## Success Criteria

The lesson is complete when:
- [ ] workspace/module-1/kickoff-summary.md exists, created from a prompt in their own words
- [ ] The summary captures the key decisions/action items (per grading key) with nothing
      invented
- [ ] Learner reviewed the output as the reader and directed (or consciously declined)
      one refinement
- [ ] workspace/my-project/CLAUDE.md exists with 2 or 3 real, observable preferences

Before wrapping up: update progress.md (check 1.1, date it, set `current: 2.1`), then
follow the teaching rules' completion flow. Module 1 done deserves a real celebration.
