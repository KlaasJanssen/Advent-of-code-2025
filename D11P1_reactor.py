from collections import defaultdict

with open("data/D11.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

connections = defaultdict(list)

for line in input:
    split_line = line.split(" ")
    connections[split_line[0][:-1]] = split_line[1:]

current_paths = defaultdict(int)
current_paths["you"] = 1
total_paths = 0

paths_going = True
while paths_going:
    paths_going = False
    new_paths = defaultdict(int)
    for start, times in current_paths.items():
        for connection in connections[start]:
            if connection == "out":
                total_paths += times
            else:
                new_paths[connection] += times
                paths_going = True
    
    current_paths = new_paths

print(total_paths)