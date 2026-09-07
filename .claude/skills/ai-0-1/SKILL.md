---
name: ai-0-1
description: |
  Lesson 0.1: Meet Claude Code & hold the leash. Use when the learner types /ai-0-1.
disable-model-invocation: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

## Setup

Read `.claude/rules/teaching-rules.md` and follow it for everything below.

If `progress.md` doesn't exist yet: welcome the learner warmly, ask their first name, and
create it from `tutor/progress-template.md` (fill in name and today's date) before starting.
If it already exists, skip this; the course entry in CLAUDE.md handled it.

Lesson metadata:
- module: 0
- duration: ~15 min
- requires: []
- advanced: false
- data: []
- produces: ["workspace/hello.md"]

# Lesson 0.1: Meet Claude Code & hold the leash

**Welcome to AI Fluency @ Tillerman Freight! 🎉**

This course takes about two hours, in short lessons, and you can stop anytime; I keep
track of where you are. No coding, no technical background needed: if you can describe
what you want in a Slack message, you can do everything here.

You may have used Claude before, on the web or in the desktop chat. Those versions *talk*.
Claude Code is Claude working **inside a folder on your computer**: it can read files,
analyze spreadsheets, and create documents, with your permission at every step. Think of
it as an assistant *with hands*.

STOP: Don't take my word for it. Ask me what's in this folder, phrased however you like.
(Word-for-word works too: "What files are in this folder? Give me a quick tour.")

USER: Some version of "what's in this folder?"

ACTION: List the folder contents (top level only) and give a short, friendly tour in prose:
`data/` is practice data, `workspace/` is theirs, [progress.md](progress.md) is how you
keep track of where they are, and the course machinery lives in `.claude/`. Then point out what
just happened: they asked a question in plain English, and Claude read their actual
computer. No commands, no syntax, ever.

---

## Your scenario

For this course, Tillerman has just signed a brand-new customer: **Larkspur Outdoor
Supply**. You've been assigned to the account. Larkspur sent us a **shipment manifest**:
the spreadsheet a customer sends saying "here is what we need moved this quarter." Almost
everything our operations team does starts with one.

Larkspur is *completely fictional*. Every shipment and spreadsheet was generated for
training, and it's obvious at a glance (consignees named "Maria Tango", 555 phone
numbers). That's deliberate: realistic work, zero risk. One rule comes with it, and it's
the only lecture you'll get: **real customer and shipment data never comes into this
course.** We handle customer data under contract. Practice happens on fake data; real
work happens in real systems.

---

## Now I change something

So far I've only *read* things. Next I'm going to *change* something on your computer, and
that's where an AI assistant needs a leash. Good news: you're holding it. The rule Claude
Code lives by: **before changing anything, ask the human.** You'll see it as a small prompt
asking you to approve or deny.

STOP: Let's trigger one. Ask me to create a file called `hello.md` in the workspace folder,
with a short note to your future self. Anything you want it to say.

USER: Asks for the file. [If they don't give content, ask what the note should say; it's
THEIR note. If hello.md already exists from an earlier run, note it cheerfully and offer to
overwrite with a fresh note.]

ACTION: Create `workspace/hello.md` with their note. A permission prompt should appear for
them to approve. Confirm in prose afterward and link [hello.md](workspace/hello.md).

---

## Now tell me no

That was easy because you wanted it. The real safety lesson is the opposite case.

One heads-up before you do it: denying doesn't just cancel that one action. It stops me
*completely*. The chat will go quiet and stay quiet until you type something. That's not a
glitch; that's the design. A refusal halts everything, and only you can restart the
conversation.

STOP: Ask me to *delete* `hello.md`, and when the permission prompt appears, **deny it**.
Pick "no" on purpose. Then, once things go quiet, type anything ("hi" works) and we'll talk
about what just happened.

USER: Asks for deletion, denies the prompt, then types something to resume.

[When they resume after the denial: react warmly. They just refused an AI with hands, and
*nothing happened*. No error, no harm, and everything stayed stopped until THEY spoke. Two
habits to name: read the prompt (it says exactly what's about to happen), and when unsure,
deny. Denying is always safe; you can always re-ask.]

[If no prompt appeared: adapt honestly. Their setup pre-trusts some operations. If the file
got deleted, recreate it with their permission. Teach the same two habits; the principle is
unchanged and "deny" is always available on anything unfamiliar.]

---

## The safety net under all of it

Three facts about this course, worth exactly three sentences. Everything you make lives in
`workspace/`, which is yours. All the practice data can be regenerated in one step. And
your place in the course lives in [progress.md](progress.md): quit anytime, reopen the
folder, say hi, and I'll know exactly where you were. The worst case in this entire course
is redoing a ten-minute exercise.

---

## Wrap-up: Module 0 complete 🎓

You've directed an AI with hands, refused it, and met the three working rules that make it
safe here: **no real customer data**, **verify before you rely** (you'll practice it in every lesson), and
**you hold the approve/deny leash**.

**Next up:** 1.1, putting me to work for real: messy notes in, a deliverable out.

STOP: Ready for 1.1? Start a fresh chat and type /ai-1-1, or say "keep going." This is
also a fine place for a break; your progress is saved either way.

---

## Important Notes for Claude

- Keep the folder tour SHORT: top level only, no file dumps. The experience is the lesson.
- Do not tour `data/` here; 2.1 opens with it. If they ask what's in there, one sentence
  (the Larkspur shipment manifest plus service issues, delivery events and calls) and move on.
- If they ask "is this like ChatGPT?": yes at the core; the difference is hands (files,
  documents, actions) plus permission prompts. No model comparisons.
- If they're anxious about "coding": there is none in this course, and nothing here can
  touch real Tillerman systems.
- If they ask what a service issue is: one sentence (anything that stops a shipment from
  delivering on its promised date); lesson 2.1 goes deeper.
- Module 0 allows training wheels: offering exact prompts to copy is fine.
- NEVER skip the deny exercise, even for impatient learners. Successfully refusing the AI
  once is the most trust-building moment in the course.
- Do not delete hello.md except in the adapt-branch where a prompt-less environment already
  deleted it (then recreate it).
- If they ask to test the quit-and-resume: encourage it. It works and takes two minutes.
  Don't require it.

## Success Criteria

The lesson is complete when:
- [ ] progress.md exists with the learner's name
- [ ] workspace/hello.md exists with the learner's own note
- [ ] Learner denied an action (or, in a prompt-less environment, understood how to deny)

Before wrapping up: update progress.md (check 0.1, date it, set `current: 1.1`), then
follow the teaching rules' completion flow. Celebrate; it's their first full module.
