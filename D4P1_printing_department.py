with open("data/D4.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

accessible = 0
for row_index, row in enumerate(input):
    for col_index, char in enumerate(row):
        if char == "@":
            neighbors = 0
            for offset_row in [-1, 0, 1]:
                for offset_col in [-1, 0, 1]:
                    if offset_row == 0 and offset_col == 0: continue
                    if row_index + offset_row < 0 or row_index + offset_row >= len(input): continue
                    if col_index + offset_col < 0 or col_index + offset_col >= len(input[0]): continue

                    if input[row_index + offset_row][col_index + offset_col] == "@":
                        neighbors += 1
            if neighbors < 4:
                accessible += 1

print(accessible)
