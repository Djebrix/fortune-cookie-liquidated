#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune-cookie line for a crypto trader who was just
liquidated to $ENTRY_OUTPUT_DIR/entry.txt (default /output).
Stdlib only, no network, fully deterministic.
"""

import os

FORTUNE = "A margin call will wake you at 3am; your 100x leverage now buys exactly one fortune cookie."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
