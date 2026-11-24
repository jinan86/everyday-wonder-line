#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line - make.fun entry.

Writes a single sentence (at most 200 characters) about a small
everyday moment made strange and new to /output/entry.txt.

The sentence was chosen after a field survey of the 51 entries
already on the bounty page: shadows arriving late or ahead, lifts
and elevators, kettles, toasters, spider webs, handrails, bus-stop
benches, fridge hum, clocks at midnight, dragonflies, shoelaces on
escalators, pigeons, cracked phone screens, rainbows in a glass of
water, rain on one side of the street, puddles, sparrows, doors
opening before you arrive and laundry were all already taken, so
this entry turns to a tap that will not quite stop dripping.
"""

import os

ENTRY = (
    "The tap drips once after I shut it off, "
    "as if the sink were finishing my sentence."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
