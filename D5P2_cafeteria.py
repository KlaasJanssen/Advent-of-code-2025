with open("data/D5.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

ranges = []

for line in input:
    if line == "":
        break
    else:
        overlap = False
        overlap_index = None
        new_range = [int(x) for x in line.split("-")]
        for fresh_range in ranges[::-1]:
            # if (new_range[0] >= fresh_range[0] and new_range[0] <= fresh_range[1]) or \
            #     (new_range[1] >= fresh_range[0] and new_range[1] <= fresh_range[1]): # Wrong function for overlap, there goes 30 minutes...
            if new_range[0] <= fresh_range[1] and new_range[1] >= fresh_range[0]:
                if not overlap:
                    fresh_range[0] = min(new_range[0], fresh_range[0])
                    fresh_range[1] = max(new_range[1], fresh_range[1])
                    overlap = True
                    overlap_range = fresh_range
                else:
                    overlap_range[0] = min(overlap_range[0], fresh_range[0])
                    overlap_range[1] = max(overlap_range[1], fresh_range[1])
                    ranges.remove(fresh_range)
                
        if not overlap:
            ranges.append(new_range)

fresh_IDs = 0
for fresh_range in ranges:
    fresh_IDs += fresh_range[1] - fresh_range[0] + 1
print(fresh_IDs)