with open("data/D9.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [[int(y) for y in x.strip("\n").split(",")] for x in f.readlines()]

max_area = 0
for index, corner1 in enumerate(input[:-1]):
    for corner2 in input[index + 1:]:
        area = abs(corner1[0] - corner2[0] + 1) * abs(corner1[1] - corner2[1] + 1)
        #print(corner1, corner2, area)
        max_area = max(max_area, area)

print(max_area)