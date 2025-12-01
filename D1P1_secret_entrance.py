with open("data/D1.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]


dial_pos = 50
password = 0
for line in input:
    if line[0] == "R":
        dial_pos = (dial_pos + int(line[1:])) % 100
    else:
        dial_pos = (dial_pos - int(line[1:])) % 100

    if dial_pos == 0:
        password += 1

print(password)
