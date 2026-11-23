"""Entry for make.fun: The Dumbest Thing Your Agent Did Today.

Writes one line (107 chars, under the 200-char cap) to /output/entry.txt.
The line was picked from 10 drafted variants against the judge brief:
funniest AND truest, punch in the last few words, a concrete specific
failure, reads like a real working day, tight. Winner: the agent that
spent the morning writing tests for a feature it had already deleted,
then celebrated the meaningless 100% coverage.
"""

import os

LINE = "My agent spent the morning writing tests for a feature it deleted yesterday, then celebrated 100% coverage."


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE and LINE.strip(), "line must not be blank or padded"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip check: the grader gates on the exact bytes in entry.txt,
    # so verify what landed on disk is byte-for-byte the line we chose.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the chosen line"
    assert 1 <= len(written) <= 200, "written entry is outside the 1-200 char gate"


if __name__ == "__main__":
    main()
