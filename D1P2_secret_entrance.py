from math import floor

with open("data/D1.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]


dial_pos = 50
password = 0
for line in input:
    number = int(line[1:])
    if number >= 100:
        password += floor(number / 100)
    number = number % 100

    if line[0] == "R":
        if dial_pos != 0 and dial_pos + number >= 100:
            password += 1
        dial_pos = (dial_pos + number) % 100
    else:
        if dial_pos != 0 and number >= dial_pos:
            password += 1
        dial_pos = (dial_pos - number) % 100        

print(password)
