# morning_check.py — the daily admin scan, all in one place.
# 1) rotation: last 3 ad topics (don't repeat)
# 2) queue: today's 4 ad files — ready or missing
# 3) optional: run a client quote
import os
from datetime import date

print("=== 1. ROTATION: last 3 topics (don't repeat) ===")
LOG = "rotation.txt"
if os.path.exists(LOG):
    with open(LOG) as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    for line in lines[-3:]:
        print("-", line)
else:
    print("(rotation.txt not found — create one with one topic per line, newest last)")

print()
today = date.today().isoformat()
missing = 0
print("=== 2. TODAY'S AD FILES (%s) ===" % today)
for slot in ["fb", "ig1", "fb2", "ig2"]:
    name = "%s-%s.png" % (today, slot)
    if os.path.exists(name):
        print("READY  :", name)
    else:
        print("MISSING:", name)
        missing += 1

print()
if missing == 0:
    print("All ads ready.")
else:
    print("%d ad(s) still need work." % missing)

print()
if input("=== 3. Run a client quote? (y/n) ").lower().startswith("y"):
    from quote_estimator import quote
    sigs = int(input("Number of signatures: "))
    miles = float(input("One-way miles: "))
    day = input("Weekday or weekend? ")
    hour = int(input("Appointment hour (0-23): "))
    mil = input("Military/veteran discount? (y/n) ").lower().startswith("y")
    print("Quote: $%.2f" % quote(sigs, miles, day, hour, mil))
