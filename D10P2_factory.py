from collections import defaultdict
from functools import cache

@cache
def try_combinations(joltage):
    if all([x == 0 for x in joltage]):
        return [0]
    
    state = "".join(["." if x % 2 == 0 else "#" for x in joltage])
    options = state_dict[state]
    
    if not options:
        return []
    
    results = []
    for option in options:
        new_joltage = list(joltage)
        for button, used in zip(buttons, option):
            if used == 1:
                for switch in button:
                    new_joltage[switch] -= 1
        if any([x < 0 for x in new_joltage]):
            continue

        new_joltage = [x // 2 for x in new_joltage]
        for sub_res in try_combinations(tuple(new_joltage)):
            results.append(sub_res * 2 + sum(option))
    
    return results

def create_state_dict(buttons, state, pressed):
    if len(buttons) == 0:
        state_dict[state].append(pressed)
        return

    create_state_dict(buttons[1:], state, pressed + [0])

    for switch in buttons[0]:
        state = state[:switch] + ("#" if state[switch] == "." else ".") + state[switch + 1:]
    create_state_dict(buttons[1:], state, pressed + [1])

with open("data/D10.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

total_presses = 0
for line in input:
    split_line = line.split(" ")
    buttons = [[int(y) for y in x[1:-1].split(",")] for x in split_line[1:-1]]
    joltage = [int(x) for x in split_line[-1][1:-1].split(",")]

    state_dict = defaultdict(list)
    create_state_dict(buttons, "." * len(joltage), [])
    total_presses += min(try_combinations(tuple(joltage)))
    try_combinations.cache_clear()
print(total_presses)



