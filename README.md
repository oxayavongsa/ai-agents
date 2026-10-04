# notary-automation

Python tools that automate the real admin of my mobile notary business (Golden State Signature, Sacramento CA). This is a **learn-in-public** project — I'm teaching myself Python by automating my own busywork, one small script at a time. Plain Python only, no dependencies.

## What it does

| Script | Purpose |
|---|---|
| `morning_check.py` | The daily scan: last 3 ad topics (don't repeat them), today's 4 ad graphics ready-or-missing, plus an optional client quote |
| `rotation_tracker.py` | Reads `rotation.txt` and prints the last 3 ad topics so I never repeat one |
| `queue_checker.py` | Checks whether today's 4 ad files (`YYYY-MM-DD-fb/ig1/fb2/ig2.png`) exist yet |
| `quote_estimator.py` | Interactive quote: signatures + travel + after-hours fee, with military discount |

## Try it

```bash
# copy the sample rotation log next to the scripts, then run:
cp data/rotation_sample.txt rotation.txt
python3 morning_check.py
```

## Run it on your phone

Install **Pydroid 3** (free, Play Store), paste any script into a new file, tap run. Same code, no changes.

## Notes

- Rates in `quote_estimator.py` are from my own sheet — `MILEAGE_RATE` should be updated whenever the IRS updates the business mileage rate.
- Built week by week while learning: variables and strings → lists, loops, and files → functions and dicts → one combined pipeline.

*Learning Python by automating my real notary busywork — Sacramento, CA.*
