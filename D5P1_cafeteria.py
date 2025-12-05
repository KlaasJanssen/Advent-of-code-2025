with open("data/D5.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

ranges = []
range_input = True
fresh = 0

for line in input:
    if line == "":
        range_input = False
    elif range_input:
        ranges.append([int(x) for x in line.split("-")])
    else:
        for lower, upper in ranges:
            if int(line) >= lower and int(line) <= upper:
                fresh += 1
                break

print(fresh)