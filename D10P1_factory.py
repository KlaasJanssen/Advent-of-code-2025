with open("data/D10.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

total_presses = 0
for line in input:
    split_line = line.split(" ")
    state = split_line[0][1:-1]
    buttons = [[int(y) for y in x[1:-1].split(",")] for x in split_line[1:-1]]
    
    possible_states = [state]
    presses = 0
    found = False
    while not found:
        presses += 1
        new_possible_states = []
        for state in possible_states:
            for button in buttons:
                new_state = list(state)
                for light in button:
                    new_state[light] = "#" if new_state[light] == "." else "."
                if not "#" in new_state:
                    found = True
                    break
                new_possible_states.append("".join(new_state))
            if found:
                break
        possible_states = new_possible_states
        # if presses > 3:
        #     break
    total_presses += presses
    # break

print(total_presses)