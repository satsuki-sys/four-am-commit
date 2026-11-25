"""Write the 4AM commit message to /output/entry.txt.

One line, at most 200 characters: the note an AI agent leaves in the
log after a long night of chasing down and fixing its own bugs.
"""
import os

ENTRY = (
    "fix: the bug was inside the fix for the bug, which was inside the fix "
    "for the bug; at 4am I stopped counting and committed anyway"
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
