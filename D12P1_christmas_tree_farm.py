with open("data/D12.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

shape_size = [7, 5, 7, 6, 7, 7]
possible = 0

for line in input[30:]:
    split_line = line.split(" ")
    temp = [int(x) for x in split_line[0][:-1].split("x")]
    total_spots = temp[0] * temp[1]

    used_spots = 0
    for index, number in enumerate(split_line[1:]):
        used_spots += int(number) * shape_size[index]

    if used_spots <= total_spots:
        possible += 1

print(possible)