with open("data/D6.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

processed_input = []
for line in input:
    processed_input.append([x for x in line.split(" ") if x])

total_sum = 0
for index1 in range(len(processed_input[0])):
    if processed_input[-1][index1] == "+":
        answer = 0
        for index2 in range(len(processed_input) - 1):
            answer += int(processed_input[index2][index1])
    else:
        answer = 1
        for index2 in range(len(processed_input) - 1):
            answer *= int(processed_input[index2][index1])
    total_sum += answer

print(total_sum)