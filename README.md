# AI Fluency Course Kit

A course where Claude Code is the tutor. A learner opens a folder in Claude Code, types
`start`, and Claude teaches them to work with AI by doing real work on realistic,
synthetic data: summarizing messy notes, checking numbers, writing the rules and runbook
for a recurring report. No videos, no manual, no technical background. Each lesson is 15
to 20 minutes and the learner can stop and resume at any time.

This repository holds the reusable teaching engine and a three-lesson demo course for a
fictional carrier, Tillerman Freight. Clone it and run the demo, or read
[AUTHORING.md](AUTHORING.md) to see how a course gets built for a specific company.

## What the full course teaches

A full engagement is eight lessons in four modules, about two hours of learner time, built
on the company's own kind of data and vocabulary.

| Module | What the learner can do afterward |
|---|---|
| Getting Started | Direct an AI that can read and change files, approve and deny its actions, know the working rules |
| Fundamentals | Turn messy inputs into a deliverable, write prompts that work, make standing preferences permanent |
| Data Analysis | Analyze a spreadsheet with verification built in, query a live system safely behind a data gate, turn findings into a deliverable |
| Automation | Write business rules and a runbook, add a review loop that catches wrong numbers, automate a task of their own |

Every number a learner produces is checked against an answer key generated from the same
code that generated the data. The tutor never marks a lesson complete as a courtesy.

## The demo in this repository

Three lessons, about 50 minutes: 0.1 Meet Claude Code and hold the leash; 1.1 Files, your
first task, and making it stick; 2.1 Rules and your first runbook. The learner joins the
operations team at Tillerman Freight, a fictional regional carrier, on the day it signs a
new shipper, Larkspur Outdoor Supply, also fictional. All data is synthetic and regenerated
by one script.

## Run it

1. Install Claude Code (the desktop app is enough).
2. Download or clone this repository.
3. Open Claude Code, choose Open folder, pick `ai-fluency-course-kit`.
4. Type `start` and press enter.

The tutor writes only inside `workspace/` and `progress.md`. Nothing else on your computer
is touched.

## How a course gets customized

The engine stays; the domain changes. Discovery finds the recurring tasks, the files
people actually receive, and the data that must never enter a training folder. A fictional
customer and four or five synthetic files mirror the real ones. Lessons are written against
that data, piloted with two or three learners, smoke-tested, trimmed, and released as a
folder people open. [AUTHORING.md](AUTHORING.md) walks through each step.

## Credits and license

Built by Misael Rosado. The method was first built and piloted for an operations team in a
regulated industry, then generalized into this kit. MIT license; see [LICENSE](LICENSE).
Tillerman Freight, Larkspur Outdoor Supply, and every person and number in `data/` are
fictional.
