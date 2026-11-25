#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

Writes the final text message a phone sends at one percent battery
(under 200 characters, in the phone's own voice) to /output/entry.txt,
deterministically.

Craft note: no low-battery pun and no generic warning — the joke is
the phone's dying act itself, a last favour with a wink (deleting the
search history), delivered in short punchy text-message beats. The
voice stays the phone's from first word to last, and the last word
lands the goodbye.
"""

import os

ENTRY = (
    "This is my last text. I deleted your search history, by the way. "
    "You're welcome. Goodbye."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
