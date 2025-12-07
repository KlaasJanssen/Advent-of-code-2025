with open("data/D7.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

row = 0
cols = set()
cols.add(input[0].index("S"))
splits = 0

for row in range(1, len(input)):
    new_cols = set()
    for col in cols:
        if input[row][col] == "^":
            new_cols.add(col - 1)
            new_cols.add(col + 1)
            splits += 1
        else:
            new_cols.add(col)
    cols = new_cols
    
print(splits)
