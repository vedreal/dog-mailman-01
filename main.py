"""Dog reviews the mailman.

A one-line review written in the dog's own voice: a loyal guard dog who
has watched the same mailman arrive every single day, rattle the gate,
and never once play fetch. The review is one tight line with a turn at
the end -- the grievance is not the visit, it is the unthrown ball.
"""

import os

ENTRY = (
    "One star. He comes every day, teases me with the gate, "
    "and leaves without ever once throwing the ball."
)


def main() -> None:
    line = ENTRY.strip()
    size = len(line.encode("utf-8"))
    if not 1 <= size <= 200:
        raise ValueError(f"entry must be 1-200 UTF-8 chars, got {size}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
