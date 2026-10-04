# queue_checker.py — which of today's ad graphics exist?
# Expects files named YYYY-MM-DD-{fb,ig1,fb2,ig2}.png in the same folder.
# The date fills in automatically — no more editing it by hand.
import os
from datetime import date

today = date.today().isoformat()  # e.g. 2026-10-04
missing = 0

print("=== TODAY'S AD FILES (%s) ===" % today)
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
