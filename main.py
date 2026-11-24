#!/usr/bin/env python3
"""Write one line of honest, funny error copy to /output/entry.txt."""

import os

ENTRY = (
    "Your request timed out: our server was arguing with the database "
    "about whose fault this was, and neither of them would back down. "
    "Please try again."
)


def main() -> None:
    # The gate allows 1-200 characters; keep the entry inside it.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
