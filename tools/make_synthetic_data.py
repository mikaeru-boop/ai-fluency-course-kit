#!/usr/bin/env python3
"""Generate all synthetic course data for AI Fluency @ Tillerman Freight.

Every row produced here is fictional. Tillerman Freight and Larkspur Outdoor Supply do
not exist. Conventions that make the data obviously fake at a glance:
  - Shipment IDs start at SHP-99000001
  - Larkspur references are LKS-000001+
  - Consignee surnames come from the NATO alphabet ("Harold Foxtrot")
  - Phones use the reserved 555-01xx range
  - Street addresses are "<n> Example Ave/Blvd/Ln", "Sample St", or "Placeholder Rd"
  - Email domains end in .example

Usage:
  python3 tools/make_synthetic_data.py            # (re)generate data/ + tutor/answer-key.md
  python3 tools/make_synthetic_data.py --check    # re-derive and diff against files on disk

Deterministic: fixed RNG seed, so identical output on every run.

To adapt this for another company: change the constants block, the make_* functions,
and the two inbox texts. Keep the structure (one file, one seed, --check, answer key
built from the same rows) so the lessons can trust every number in the key.
"""

import csv
import io
import random
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
INBOX = DATA / "inbox"
ANSWER_KEY = ROOT / "tutor" / "answer-key.md"

SEED = 20260907
CARRIER = "Tillerman Freight"
CUSTOMER = "Larkspur Outdoor Supply"

FIRST_NAMES = [
    "Harold", "Maria", "James", "Dorothy", "Robert", "Linda", "Walter", "Gloria",
    "Frank", "Carmen", "Eugene", "Ruth", "Arthur", "Sylvia", "Leon", "Bessie",
    "Raymond", "Alma", "Clarence", "Estelle", "Victor", "Pearl", "Howard", "Ida",
    "Norman", "Lucille", "Ernest", "Vera", "Stanley", "Opal", "Marvin", "Hazel",
    "Alfredo", "Rosa", "Chester", "Willie", "Otis", "Mabel", "Rufus", "Cora",
]
NATO = [
    "Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel",
    "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa",
    "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey",
    "Xray", "Yankee", "Zulu",
]
GEO = {  # state -> (city, terminal, zip prefix)
    "WA": [("Seattle", "Kent terminal", "981"), ("Tacoma", "Kent terminal", "984"), ("Spokane", "Spokane terminal", "992")],
    "OR": [("Portland", "Portland terminal", "972"), ("Eugene", "Portland terminal", "974"), ("Bend", "Bend terminal", "977")],
    "ID": [("Boise", "Boise terminal", "837"), ("Idaho Falls", "Boise terminal", "834")],
    "MT": [("Billings", "Billings terminal", "591"), ("Missoula", "Billings terminal", "598")],
    "NV": [("Reno", "Reno terminal", "895"), ("Las Vegas", "Reno terminal", "891")],
    "CA": [("Sacramento", "Redding terminal", "958"), ("Redding", "Redding terminal", "960")],
}
STATE_WEIGHTS = {"WA": 55, "OR": 45, "ID": 35, "MT": 25, "NV": 22, "CA": 18}  # sums to 200
SERVICE_LEVELS = ["Standard", "Expedited", "Guaranteed"]
SERVICE_WEIGHTS = [0.55, 0.30, 0.15]
TRANSIT_DAYS = {"Standard": (3, 7), "Expedited": (2, 3), "Guaranteed": (1, 2)}
ISSUE_TYPES = ["address_correction", "missed_pickup", "damage_claim", "appointment_needed", "weather_hold"]
STREETS = ["Example Ave", "Example Blvd", "Example Ln", "Sample St", "Placeholder Rd"]


def make_shipments(rng):
    """200 clean Q3 shipments."""
    shipments = []
    states = [s for s, n in STATE_WEIGHTS.items() for _ in range(n)]
    rng.shuffle(states)
    for i, state in enumerate(states, start=1):
        city, terminal, zip3 = rng.choice(GEO[state])
        service = rng.choices(SERVICE_LEVELS, SERVICE_WEIGHTS)[0]
        pickup = date(2026, 7, 1) + timedelta(days=rng.randint(0, 85))
        promised = pickup + timedelta(days=rng.randint(*TRANSIT_DAYS[service]))
        shipments.append({
            "shipment_id": f"SHP-{99000000 + i}",
            "larkspur_ref": f"LKS-{i:06d}",
            "consignee_name": f"{rng.choice(FIRST_NAMES)} {rng.choice(NATO)}",
            "address": f"{rng.randint(100, 999)} {rng.choice(STREETS)}",
            "city": city,
            "dest_state": state,
            "zip": f"{zip3}{rng.randint(10, 99)}",
            "phone": f"({rng.randint(200, 989)}) 555-01{rng.randint(10, 99)}",
            "service_level": service,
            "weight_lbs": rng.randint(40, 1800),
            "pieces": rng.randint(1, 12),
            "pickup_date": pickup.isoformat(),
            "promised_date": promised.isoformat(),
            "_terminal": terminal,
        })
    return shipments


def make_issues(rng, shipments):
    """About 400 service issues; a shipment has 0 to 4, each of a different type."""
    issues, issue_id = [], 0
    for s in shipments:
        n_issues = rng.choices([0, 1, 2, 3, 4], [0.12, 0.25, 0.30, 0.20, 0.13])[0]
        pickup = date.fromisoformat(s["pickup_date"])
        for issue_type in sorted(rng.sample(ISSUE_TYPES, n_issues)):
            issue_id += 1
            status = rng.choices(["open", "in_progress", "resolved"], [0.45, 0.20, 0.35])[0]
            opened = pickup + timedelta(days=rng.randint(0, 30))
            resolved = ""
            if status == "resolved":
                resolved = (opened + timedelta(days=rng.randint(2, 20))).isoformat()
            issues.append({
                "issue_id": f"ISS-{issue_id:05d}",
                "shipment_id": s["shipment_id"],
                "issue_type": issue_type,
                "status": status,
                "opened_date": opened.isoformat(),
                "resolved_date": resolved,
                "reported_by": rng.choice(["driver", "customer", "dispatch"]),
            })
    return issues


def make_delivery_events(rng, shipments):
    """160 shipments get exactly one terminal event; 40 have none yet."""
    moved = rng.sample(shipments, 160)
    events = []
    for i, s in enumerate(moved, start=1):
        status = rng.choices(
            ["delivered", "out_for_delivery", "exception", "returned"], [0.58, 0.18, 0.14, 0.10]
        )[0]
        edate = date.fromisoformat(s["promised_date"]) + timedelta(days=rng.randint(-1, 4))
        events.append({
            "event_id": f"EVT-{700000 + i}",
            "shipment_id": s["shipment_id"],
            "status": status,
            "event_date": edate.isoformat(),
            "terminal": s["_terminal"],
        })
    return events


def make_calls(rng, shipments):
    """500 carrier calls to consignees about delivery."""
    calls = []
    for i in range(1, 501):
        s = rng.choice(shipments)
        cdate = date.fromisoformat(s["pickup_date"]) + timedelta(days=rng.randint(0, 20))
        calls.append({
            "call_id": f"CALL-{i:05d}",
            "shipment_id": s["shipment_id"],
            "call_date": cdate.isoformat(),
            "disposition": rng.choices(
                ["no_answer", "rescheduled", "refused_delivery", "bad_address", "left_voicemail"],
                [0.34, 0.22, 0.12, 0.08, 0.24],
            )[0],
        })
    calls.sort(key=lambda c: (c["call_date"], c["call_id"]))
    return calls


def make_q4_drop(rng):
    """The dirty Q4 file: 250 rows, 7 of which the loader rejects.

    Rejects: 3 duplicate references, 2 invalid weights (zero or negative),
    1 invalid state ("Oregn"), 1 missing zip. All other rows load."""
    rows = []
    for i in range(1, 251):
        state = rng.choice(list(GEO))
        city, terminal, zip3 = rng.choice(GEO[state])
        service = rng.choices(SERVICE_LEVELS, SERVICE_WEIGHTS)[0]
        rows.append({
            "larkspur_ref": f"LKS-{200 + i:06d}",
            "consignee_name": f"{rng.choice(FIRST_NAMES)} {rng.choice(NATO)}",
            "dest_state": state,
            "zip": f"{zip3}{rng.randint(10, 99)}",
            "service_level": service,
            "weight_lbs": rng.randint(40, 1800),
            "pieces": rng.randint(1, 12),
            "requested_pickup": (date(2026, 10, 5) + timedelta(days=rng.randint(0, 60))).isoformat(),
        })

    reject = {}  # row index -> reason
    # 3 duplicates: rows 60, 130, 200 copy the reference + consignee of rows 10, 40, 90
    for dup_idx, src_idx in [(59, 9), (129, 39), (199, 89)]:
        for k in ("larkspur_ref", "consignee_name"):
            rows[dup_idx][k] = rows[src_idx][k]
        reject[dup_idx] = "duplicate_ref"
    # 2 invalid weights
    rows[24]["weight_lbs"] = 0
    rows[174]["weight_lbs"] = -40
    reject[24] = reject[174] = "invalid_weight"
    # 1 invalid state
    rows[99]["dest_state"] = "Oregn"
    reject[99] = "invalid_state"
    # 1 missing zip
    rows[149]["zip"] = ""
    reject[149] = "missing_zip"

    load_log = [{
        "file_row": i + 1,
        "larkspur_ref": r["larkspur_ref"],
        "load_status": "rejected" if i in reject else "loaded",
        "reject_reason": reject.get(i, ""),
    } for i, r in enumerate(rows)]
    return rows, load_log


def write_csv(path, rows):
    fields = [k for k in rows[0].keys() if not k.startswith("_")]
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    return {path: buf.getvalue()}


def counts(rows, key):
    out = {}
    for r in rows:
        out[r[key]] = out.get(r[key], 0) + 1
    return dict(sorted(out.items(), key=lambda kv: (-kv[1], kv[0])))


def fmt_counts(d):
    return "\n".join(f"| {k} | {v} |" for k, v in d.items())


def build_answer_key(shipments, issues, events, calls, q4_rows, load_log):
    by_state = counts(shipments, "dest_state")
    by_service = counts(shipments, "service_level")
    issue_by_status = counts(issues, "status")
    open_by_type = counts([i for i in issues if i["status"] == "open"], "issue_type")
    open_by_shipment = counts([i for i in issues if i["status"] == "open"], "shipment_id")
    three_plus = sorted(s for s, n in open_by_shipment.items() if n >= 3)

    delivered = {e["shipment_id"] for e in events if e["status"] == "delivered"}
    ship_state = {s["shipment_id"]: s["dest_state"] for s in shipments}
    comp_by_state = {}
    for st in by_state:
        tot = sum(1 for s in shipments if s["dest_state"] == st)
        done = sum(1 for sid in delivered if ship_state[sid] == st)
        comp_by_state[st] = (done, tot, round(100 * done / tot, 1))
    open_no_delivery = sorted(set(open_by_shipment) - delivered)

    rejects = [l for l in load_log if l["load_status"] == "rejected"]
    reject_reasons = counts(rejects, "reject_reason")
    with_events = {e["shipment_id"] for e in events}

    key = f"""# Answer key, generated by tools/make_synthetic_data.py (seed {SEED})

Ground truth for lesson checkpoints. Tutor: numbers the learner produces must match these.
Section ids are named by content so lessons can be renumbered without touching them.

## §profile (larkspur_shipments_2026Q3.csv)

- Total shipments: **{len(shipments)}**

By destination state:

| dest_state | shipments |
|---|---|
{fmt_counts(by_state)}

By service level:

| service_level | shipments |
|---|---|
{fmt_counts(by_service)}

## §issues (larkspur_service_issues.csv)

- Total issue rows: **{len(issues)}**

By status:

| status | issues |
|---|---|
{fmt_counts(issue_by_status)}

Open issues by type:

| issue_type | open issues |
|---|---|
{fmt_counts(open_by_type)}

- Shipments with 3+ open issues: **{len(three_plus)}** ({", ".join(three_plus)})
- "Worked" (in_progress + resolved): **{issue_by_status.get("in_progress", 0) + issue_by_status.get("resolved", 0)}**

## §joins (shipments x delivery events x issues)

- Delivery event rows: **{len(events)}** (shipments with an event: {len(with_events)}; shipments with none: {len(shipments) - len(with_events)})
- Delivered: **{len(delivered)}**
- Completion rate overall (delivered / {len(shipments)} shipments): **{round(100 * len(delivered) / len(shipments), 1)}%**

Completion by destination state (delivered / shipments):

| dest_state | delivered | shipments | rate |
|---|---|---|---|
{chr(10).join(f"| {st} | {d} | {t} | {r}% |" for st, (d, t, r) in comp_by_state.items())}

- Shipments with an open issue AND not delivered: **{len(open_no_delivery)}**

## §reconciliation (larkspur_shipments_2026Q4_raw.csv + larkspur_load_log.csv)

- Customer email says: **250 shipments sent**
- Raw file rows: **{len(q4_rows)}**
- Loaded: **{sum(1 for l in load_log if l["load_status"] == "loaded")}**
- Rejected: **{len(rejects)}**

| reject_reason | rows |
|---|---|
{fmt_counts(reject_reasons)}

Rejected file rows: {", ".join(str(l["file_row"]) for l in rejects)}

## §kpis (for the learner's weekly runbook)

1. Total shipments: **{len(shipments)}**
2. Delivered: **{len(delivered)}**
3. Completion rate: **{round(100 * len(delivered) / len(shipments), 1)}%**
4. Open issues: **{issue_by_status.get("open", 0)}**
5. Carrier calls: **{len(calls)}**
"""
    return key


DATA_README = f"""# {CUSTOMER}: synthetic practice data

**Every row in this folder is synthetic, generated for training by
`tools/make_synthetic_data.py`. {CARRIER} and {CUSTOMER} do not exist. No real
customer, shipment, or employee data appears here, and none may ever be added.**

You can tell the data is fake at a glance: shipment IDs start with 99, consignee surnames
are the NATO alphabet, phones are 555-01xx, and streets are named "Example Ave", "Sample
St", or "Placeholder Rd".

## Files

| File | What it is |
|---|---|
| `larkspur_shipments_2026Q3.csv` | The Q3 shipment manifest: 200 shipments the customer asked us to move. One row per shipment: IDs, consignee, destination, service level, weight, pickup and promised dates. |
| `larkspur_service_issues.csv` | Service issues on those shipments. `status`: `open` (nobody has acted), `in_progress` (being worked, not confirmed), `resolved` (confirmed closed). |
| `larkspur_delivery_events.csv` | The latest delivery event per shipment. **Only `status = delivered` counts as a completed shipment.** |
| `larkspur_carrier_calls.csv` | Calls our dispatch team made to consignees, with dispositions. |
| `larkspur_shipments_2026Q4_raw.csv` | The Q4 manifest exactly as the customer sent it, problems included. The full course's data-quality lesson uses it; no lesson in this demo does. |
| `larkspur_load_log.csv` | What our loader did with each Q4 row (loaded or rejected, with the reason). |
| `inbox/` | Messy human inputs (kickoff notes, a customer email) used in exercises. |

## Column notes

- `shipment_id`: our internal tracking id (SHP-99######)
- `larkspur_ref`: the customer's own reference (LKS-######)
- `service_level`: Standard (3 to 7 days), Expedited (2 to 3), Guaranteed (1 to 2)
- `issue_type`: address_correction, missed_pickup, damage_claim, appointment_needed,
  weather_hold
- `terminal`: the Tillerman facility that handled the final leg
"""

KICKOFF_NOTES = """larkspur kickoff call - tuesday - notes (sorry these are rough, typed on phone)

on call: me, Dana (larkspur logistics dir), Marcus (larkspur IT), Priya (their PM), T. from our side

q3 manifest = 200 shipments, they want the on-time push before oct (holiday season)
Dana: priority is the WA + OR lanes, thats where their retail partners are
they will send q4 volume "around 250 shipments" first week of oct - marcus sending via EDI as usual
IMPORTANT dana said their leadership reviews ops numbers every monday morning -> our
weekly status needs to land BEFORE that, so friday end of day at latest

focus this qtr: exception rate and on-time delivery, Dana says damage claims "historically ugly"
priya asked if we can flag shipments w/ 3+ open issues for proactive calls - said yes
marcus: dont use the old FTP drop from 2025!! new EDI creds coming
someone asked about the two receiving warehouses w/ spanish speaking crews - need spanish-first delivery notifications

action items (i think):
- us: priority lane list WA/OR ✓ flag 3+ issues
- us: weekly status by friday EOD
- them: q4 manifest early oct, new EDI creds (marcus)
- them: confirm notification language requirements (priya, next week)

next call oct 8, 2pm PT

(fictional notes written for training)
"""

CUSTOMER_EMAIL = """From: Dana Whitfield <d.whitfield@larkspuroutdoor.example>
To: Tillerman Freight Account Team
Date: Mon, Oct 5, 2026 9:14 AM
Subject: Q4 shipment manifest - sent

Good morning,

Per our kickoff, the Q4 manifest went out via EDI this morning. It contains 250 shipments
for Q4 pickup. Please confirm receipt and let us know when these are loaded on your
side. Our leadership reviews ops numbers every Monday morning and I'd like the first
November review to show Q4 freight moving.

One note: our warehouse team flagged that a handful of records may have data issues
(we switched order-management systems in September). If anything doesn't load, please
send us the specifics so we can correct at the source.

Best,
Dana

Dana Whitfield | Director of Logistics | Larkspur Outdoor Supply
(This is a fictional email for training purposes.)
"""


def generate():
    rng = random.Random(SEED)
    shipments = make_shipments(rng)
    issues = make_issues(rng, shipments)
    events = make_delivery_events(rng, shipments)
    calls = make_calls(rng, shipments)
    q4_rows, load_log = make_q4_drop(rng)

    files = {}
    files.update(write_csv(DATA / "larkspur_shipments_2026Q3.csv", shipments))
    files.update(write_csv(DATA / "larkspur_service_issues.csv", issues))
    files.update(write_csv(DATA / "larkspur_delivery_events.csv", events))
    files.update(write_csv(DATA / "larkspur_carrier_calls.csv", calls))
    files.update(write_csv(DATA / "larkspur_shipments_2026Q4_raw.csv", q4_rows))
    files.update(write_csv(DATA / "larkspur_load_log.csv", load_log))
    files[DATA / "README.md"] = DATA_README
    files[INBOX / "larkspur-kickoff-notes.txt"] = KICKOFF_NOTES
    files[INBOX / "larkspur-customer-email.txt"] = CUSTOMER_EMAIL
    files[ANSWER_KEY] = build_answer_key(shipments, issues, events, calls, q4_rows, load_log)
    return files


def main():
    files = generate()
    if "--check" in sys.argv:
        bad = []
        for path, content in files.items():
            on_disk = path.read_text() if path.exists() else None
            if on_disk != content:
                bad.append(str(path.relative_to(ROOT)))
        if bad:
            print("DIFF: these files don't match a fresh generation:")
            for b in bad:
                print(f"  {b}")
            sys.exit(1)
        print(f"OK: all {len(files)} generated files match disk (seed {SEED}).")
        return
    INBOX.mkdir(parents=True, exist_ok=True)
    ANSWER_KEY.parent.mkdir(parents=True, exist_ok=True)
    for path, content in files.items():
        path.write_text(content)
        print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
