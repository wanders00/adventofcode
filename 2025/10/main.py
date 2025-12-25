from dataclasses import dataclass
from collections import deque
import re


@dataclass
class Machine:
    lights: int
    buttons: list[int]
    joltage: list[int]
    width: int


machines: list[Machine] = []


def parse_machine_line(line: str) -> Machine:
    line = line.strip()
    lights_match = re.search(r"\[([^\]]*)\]", line)
    buttons_matches = re.findall(r"\(([^)]*)\)", line)
    joltage_match = re.search(r"\{([^}]*)\}", line)

    lights_str = lights_match.group(1) if lights_match else ""
    width = len(lights_str)
    lights_bits = "".join("1" if ch == "#" else "0" for ch in lights_str)
    lights = int("".join(reversed(lights_bits)) or "0", 2)

    buttons: list[int] = []
    for bm in buttons_matches:
        bm = bm.strip()
        if bm:
            parts = [p.strip() for p in bm.split(",") if p.strip()]
            indices = [int(p) for p in parts]
            mask = ["0"] * width
            for idx in indices:
                if 0 <= idx < len(mask):
                    mask[idx] = "1"
            buttons.append(int("".join(reversed(mask)) or "0", 2))

    joltage_str = joltage_match.group(1) if joltage_match else ""
    joltage = [int(p.strip()) for p in joltage_str.split(",") if p.strip()]

    return Machine(lights=lights, buttons=buttons, joltage=joltage, width=width)


def combine(a: int, b: int) -> int:
    return a ^ b


def min_press_part1(machine: Machine) -> int:
    target = machine.lights
    buttons = machine.buttons
    if target in buttons:
        return 1

    visited: set[int] = set()
    q: deque[tuple[int, int]] = deque()

    for btn in buttons:
        if btn not in visited:
            visited.add(btn)
            q.append((btn, 1))

    while q:
        state, steps = q.popleft()
        for btn in buttons:
            nxt = combine(state, btn)
            if nxt == target:
                return steps + 1
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, steps + 1))

    return 0


score = 0
with open("input.txt") as f:
    for line in f:
        if line.strip():
            score += min_press_part1(parse_machine_line(line))

print(score)
