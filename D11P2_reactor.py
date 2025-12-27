from collections import defaultdict

with open("data/D11.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

connections = defaultdict(list)

for line in input:
    split_line = line.split(" ")
    connections[split_line[0][:-1]] = split_line[1:]

current_paths = defaultdict(int)
current_paths["svr_F_F"] = 1
total_paths = 0

paths_going = True
while paths_going:
    paths_going = False
    new_paths = defaultdict(int)
    for start, times in current_paths.items():
        start_split = start.split("_")
        for connection in connections[start_split[0]]:
            if connection == "out":
                if start_split[1] == "T" and start_split[2] == "T":
                    total_paths += times
            else:
                if connection == "dac":
                    new_connection = f"{connection}_T_{start_split[2]}" 
                elif connection == "fft":
                    new_connection = f"{connection}_{start_split[1]}_T" 
                else:
                    new_connection = f"{connection}_{start_split[1]}_{start_split[2]}" 
                new_paths[new_connection] += times
                paths_going = True
    
    current_paths = new_paths

print(total_paths)

# 835553846187340 too high