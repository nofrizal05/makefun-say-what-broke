"""Say What Actually Broke — make.fun entry.

Writes one line of brutally honest software error copy to /output/entry.txt.
Python standard library only.
"""

import os

LINE = (
    "Your file didn't save: the disk is full of crash reports from every "
    "other file that didn't save."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
