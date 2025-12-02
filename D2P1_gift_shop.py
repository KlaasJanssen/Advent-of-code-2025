with open("data/D2.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()][0]

invalid_ID = 0
for ID_range in input.split(","):
    lower, higher = ID_range.split("-")
    if len(lower) % 2 == 0 and len(higher) % 2 == 0:
        for pattern in range(int(lower[:len(lower)//2]), int(higher[:len(higher)//2]) + 1):
            if int(str(pattern) * 2) >= int(lower) and int(str(pattern) * 2) <= int(higher):
                invalid_ID += int(str(pattern) * 2)

    elif len(lower) % 2 == 0 and len(higher) % 2 == 1:
        for pattern in range(int(lower[:len(lower)//2]), int("1" + "0" * (len(lower)//2))):
            if int(str(pattern) * 2) >= int(lower) and int(str(pattern) * 2) <= int(higher):
                invalid_ID += int(str(pattern) * 2)

    elif len(lower) % 2 == 1 and len(higher) % 2 == 0:
        for pattern in range(int("1" + "0" * (len(higher)//2 - 1)), int(higher[:len(higher)//2]) + 1):
            if int(str(pattern) * 2) >= int(lower) and int(str(pattern) * 2) <= int(higher):
                invalid_ID += int(str(pattern) * 2)

print(invalid_ID)


