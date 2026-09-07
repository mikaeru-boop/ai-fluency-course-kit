# Larkspur Outdoor Supply: synthetic practice data

**Every row in this folder is synthetic, generated for training by
`tools/make_synthetic_data.py`. Tillerman Freight and Larkspur Outdoor Supply do not exist. No real
customer, shipment, or employee data appears here, and none may ever be added.**

You can tell the data is fake at a glance: shipment IDs start with 99, consignee surnames
are the NATO alphabet, phones are 555-01xx, and streets are named "Example Ave."

## Files

| File | What it is |
|---|---|
| `larkspur_shipments_2026Q3.csv` | The Q3 shipment manifest: 200 shipments the customer asked us to move. One row per shipment: IDs, consignee, destination, service level, weight, pickup and promised dates. |
| `larkspur_service_issues.csv` | Service issues on those shipments. `status`: `open` (nobody has acted), `in_progress` (being worked, not confirmed), `resolved` (confirmed closed). |
| `larkspur_delivery_events.csv` | The latest delivery event per shipment. **Only `status = delivered` counts as a completed shipment.** |
| `larkspur_carrier_calls.csv` | Calls our dispatch team made to consignees, with dispositions. |
| `larkspur_shipments_2026Q4_raw.csv` | The Q4 manifest exactly as the customer sent it, problems included. Used in the data-quality lesson. |
| `larkspur_load_log.csv` | What our loader did with each Q4 row (loaded or rejected, with the reason). |
| `inbox/` | Messy human inputs (kickoff notes, a customer email) used in exercises. |

## Column notes

- `shipment_id`: our internal tracking id (SHP-99######)
- `larkspur_ref`: the customer's own reference (LKS-######)
- `service_level`: Standard (3 to 7 days), Expedited (2 to 3), Guaranteed (1 to 2)
- `issue_type`: address_correction, missed_pickup, damage_claim, appointment_needed,
  weather_hold
- `terminal`: the Tillerman facility that handled the final leg
