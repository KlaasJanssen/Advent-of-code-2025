from collections import defaultdict

with open("data/D7.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

row = 0
cols = defaultdict(int)
cols[input[0].index("S")] = 1

for row in range(1, len(input)):
    new_cols = defaultdict(int)
    for col, times in cols.items():
        if input[row][col] == "^":
            new_cols[col - 1] += times
            new_cols[col + 1] += times
        else:
            new_cols[col] += times
    cols = new_cols
    
print(sum(cols.values()))
