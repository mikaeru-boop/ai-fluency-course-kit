# Authoring a course for a company

This is the process behind the demo in this repository, written so a company can see what
an engagement involves and a practitioner can repeat it.

## 1. Discovery

Sit with the team that will learn. Collect three things: the recurring tasks they do by
hand (weekly summaries, reconciling a customer file, turning call notes into action items),
the files they actually receive (a manifest, an inbox of messy notes, a status export), and
the vocabulary they use for them. Ask which data classes must never enter a training
folder: personal data, payment data, health data, anything under contract. Pick two or
three pilot learners who are not technical.

## 2. Domain model

Invent a customer. Design four or five files that mirror the real ones, each with the one
business rule that matters most: which status means done, which flag lies, which count the
boss asks for. In the demo: a shipment manifest, service issues, delivery events (only
`delivered` counts), carrier calls, and a dirty second manifest with a load log. Real work
is full of rows that look fine and are not; the data should be too.

## 3. Synthetic data

One script generates every file and the answer key from the same rows, with a fixed seed,
so a run today matches a run next year. `--check` re-derives everything and diffs it
against disk; run it before every release. Make fake data obvious at a glance: IDs that
start with 99, surnames from the NATO alphabet, 555 phone numbers, streets named "Example
Ave". Every number a lesson expects comes from the generated key, never from a person's
memory. See `tools/make_synthetic_data.py`; its docstring says which parts to change.

## 4. Lessons

Each lesson is a Claude Code skill, invoked by a command like `/ai-1-1`, written from
`tutor/lesson-template.md`. The template's stage directions (STOP, USER, ACTION, bracketed
conditions) tell the tutor when to wait, what an acceptable answer looks like, and what it
does itself. Grading keys live only in the "Important Notes for Claude" section, never
next to the question. One deliverable per lesson. Teach each concept once and refer back
in a clause. The learner writes every prompt in their own words; the tutor offers a hint,
then a smaller step, then the exact prompt only if asked.

## 5. Sensitive data and tool boundaries

`.claude/rules/teaching-rules.md` carries the tutor's hard rules. Hard rule 2 is the
sensitive-data rule and has a customize marker: name the data classes and regulations that
bind the company, and what the tutor says when a learner pastes something real.
`allowed-tools` in each lesson's frontmatter is the security boundary. A lesson that
touches a live system (a database through an MCP server, for example) is the only place
those tools appear, and it opens with a prerequisite check and a data gate: the learner
restates the aggregate-only rule before any live query. If the check fails, the lesson
stops and offers a synthetic fallback.

## 6. Pilot and smoke test

Pilot with the learners from discovery and read the tutor's notes in their progress files.
Then run the smoke test in `MAINTENANCE.md`: fresh folder, no progress file, a novice
roleplay, seven checks. A scripted pass is cheap: copy the packaged folder to a scratch
directory and drive lessons with `claude -p` in a loop, reading the transcript afterward.
The first deployment's pilots found three defects that became rules: the tutor copied last
session's date forward into new files, it narrated its own setup ("let me kick off the
lesson"), and a learner's date-format preference leaked into the course's bookkeeping.
Each fix is one sentence in teaching-rules.md.

## 7. Trim and release

After the pilot, review every lesson for redundancy: concepts taught twice, stops spent on
mechanics the learner already knows, verbal quizzes that a later artifact tests anyway.
The first deployment went from 11 lessons to 8 and from 41 stops to 24 this way, with no
loss of coverage. Bump `course_version` in CLAUDE.md, tag the release, and ship either a
git clone or a zip with the learner state removed (see "Packaging" in MAINTENANCE.md).
