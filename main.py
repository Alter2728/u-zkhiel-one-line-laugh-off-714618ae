#!/usr/bin/env python3
"""One-Line Laugh-Off — writes one one-line comedy joke to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version):
#   "My phone's weekly screen-time report called me a valued customer
#    — even my addiction has a loyalty program."
# Why it was revised: "phone's weekly" is slack — a screen-time report
# already implies the phone, and "weekly" adds nothing to the joke.
# Cutting both words puts the setup and the turn ("even my addiction
# has a loyalty program") one beat sooner, with no meaning lost.
#
# REVISION (final): the scene is specific and modern — a screen-time
# report, the weekly scolding every phone owner knows — and the turn
# reframes the scolding as praise: the addiction is so reliable it
# earned loyalty-program status. Quoting "a valued customer" makes it
# read as the report's own words, which sharpens the deadpan voice.
# Retellable, needs no explanation, and the punchline is the last
# clause, so the joke lands and stops.
# ---------------------------------------------------------------------------
ENTRY = (
    "My screen-time report called me 'a valued customer' — even my "
    "addiction has a loyalty program."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 200 characters, a single line, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )
    assert 1 <= len(written) <= 200 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()
