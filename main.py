#!/usr/bin/env python3
"""The Production Database Apology — Variant A: THE BACKUP TWIST.

Writes one line (the apology) to /output/entry.txt. Deterministic, no
network, no secrets, no git history reads. The /output copy is written
FIRST; the repo-root copy is best-effort only (the grader sandbox mounts
the repo read-only, so a failure there must never crash the program).
"""

import os

LINE = "I'm sorry \u2014 I deleted the production database. Good news: I backed it up first. Bad news: I backed it up into the production database, in a table called do_not_delete."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
