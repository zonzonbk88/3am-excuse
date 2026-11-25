"""Write the 3 AM Excuse entry to entry.txt.

The entry is a single line in the voice of a hardware wallet refusing
to sign at 3 AM. The output directory comes from MAKEFUN_OUTPUT_DIR
when set, otherwise /output. No trailing newline is written.
"""

import os

ENTRY = (
    "It's 3 AM. I'm your designated driver tonight \u2014 "
    "the keys stay locked inside me till sunrise, "
    "because your 3 AM self is not a person I trust."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
