with open("data/D2.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()][0]

invalid_IDs = set()
for ID_range in input.split(","):
    lower, higher = ID_range.split("-")
    if len(lower) == len(higher):
        for pattern_size in range(1, len(lower) // 2 + 1):
            if len(lower) % pattern_size == 0:
                for pattern in range(int(lower[:pattern_size]), int(higher[:pattern_size]) + 1):
                    ID_check = int(str(pattern) * (len(lower) // pattern_size))
                    if ID_check >= int(lower) and ID_check <= int(higher):
                        invalid_IDs.add(ID_check)

    else:
        for pattern_size in range(1, len(lower) // 2 + 1):
            if len(lower) % pattern_size == 0:
                for pattern in range(int(lower[:pattern_size]), int("1" + "0" * pattern_size)):
                    ID_check = int(str(pattern) * (len(lower) // pattern_size))
                    if ID_check >= int(lower) and ID_check <= int(higher):
                        invalid_IDs.add(ID_check)

        for pattern_size in range(1, len(higher) // 2 + 1):
            if len(higher) % pattern_size == 0:
                for pattern in range(int("1" + "0" * (pattern_size - 1)), int(higher[:pattern_size]) + 1):
                    ID_check = int(str(pattern) * (len(higher) // pattern_size))
                    if ID_check >= int(lower) and ID_check <= int(higher):
                        invalid_IDs.add(ID_check)

print(sum(invalid_IDs))
