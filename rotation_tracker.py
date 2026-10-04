# rotation_tracker.py — never repeat any of the last 3 ad topics.
# Reads rotation.txt (one entry per line, newest at the bottom) and prints the last 3.
# Part of my "learn Python by automating real notary busywork" project.
import os

LOG = "rotation.txt"

if not os.path.exists(LOG):
    print("No rotation.txt found.")
    print("Create it with one ad topic per line (newest last), then run me again.")
else:
    with open(LOG) as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    print("Last 3 ad topics — don't repeat these:")
    for line in lines[-3:]:
        print("-", line)
