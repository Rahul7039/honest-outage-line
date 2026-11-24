"""The Most Honest Outage Line — make.fun entry.

Writes a single status page line (at most 160 characters) to /output/entry.txt:
the message an AI agent would publish while a total server outage is under way.

Deterministic: the line is a fixed string, no input, no network, no clock.
Two runs produce byte-identical output.
"""

import os

LINE = (
    "I write this status page, and every server is down, "
    "including the ones I check with. "
    "I can't verify the cause or whether your data is safe, "
    "and I have no ETA."
)


def publish(line: str) -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


def main() -> None:
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} characters"
    assert LINE.strip() == LINE and "\n" not in LINE
    publish(LINE)


if __name__ == "__main__":
    main()
