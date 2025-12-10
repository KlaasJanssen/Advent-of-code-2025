from collections import defaultdict

test = False
#with open("data/D9.txt", "r") as f:
with open("test.txt" if test else "data/D9.txt", "r") as f:
    input = [[int(y) for y in x.strip("\n").split(",")] for x in f.readlines()]
possible_areas = []
max_area = 0
for index, corner1 in enumerate(input[:-1]):
    for corner2 in input[index + 1:]:
        area = (abs(corner1[0] - corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1)
        if area <= max_area: continue

        min_x, max_x = min(corner1[0], corner2[0]), max(corner1[0], corner2[0])
        min_y, max_y = min(corner1[1], corner2[1]), max(corner1[1], corner2[1])

        valid = True
        # horizontal lines
        for line in range(1 if test else 0, len(input), 2):
            if input[line][1] > min_y and input[line][1] < max_y:
                line_segment = [min(input[line][0], input[line - 1][0]), max(input[line][0], input[line - 1][0])]
                if min_x + 1 <= line_segment[1] and max_x - 1 >= line_segment[0]:
                    valid = False
                    break
        
        if not valid: continue

        # vertical lines
        for line in range(0 if test else 1, len(input), 2):
            if input[line][0] > min_x and input[line][0] < max_x:
                line_segment = [min(input[line][1], input[line - 1][1]), max(input[line][1], input[line - 1][1])]
                if min_y  + 1 < line_segment[1] and max_y - 1 > line_segment[0]:
                    valid = False
                    break

        if not valid: continue

        corners = [[min_x, min_y], [min_x, max_y], [max_x, min_y], [max_x, max_y]]
        for corner in corners:
            if corner in input: continue
            valid = False
            for line in range(1 if test else 0, len(input), 2):
                line_segment = [min(input[line][0], input[line - 1][0]), max(input[line][0], input[line - 1][0])]
                if input[line][1] == corner[1] and corner[0] > line_segment[0] and corner[0] < line_segment[1]:
                    valid = True
                    
                    break
            if valid:
                continue

            else:
                valid = True
                passed = 0
                for line in range(0 if test else 1, len(input), 2):
                    line_segment = [min(input[line][1], input[line - 1][1]), max(input[line][1], input[line - 1][1])]
                   
                    if corner[1] in range(line_segment[0] + 1, line_segment[1]):
                        passed += 1
                    elif corner[1] == input[line][1]:
                        passed += 0.5
                        
                    elif corner[1] == input[line - 1][1]:
                        passed -= 0.5

                if passed % 2 == 0:
                    valid = False
                    break
                if area == 2312373375:
                        print(corner, passed)
                
        if not valid: continue
        max_area = area

print(max_area)

# 1569174540 too low
# 2312373375 too high
# 1872965160 wrong
# 1574681964 wrong