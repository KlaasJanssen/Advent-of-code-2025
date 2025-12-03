with open("data/D3.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

total_joltage = 0
for line in input:
    current_num = 0
    for index, num1 in enumerate(line[:-1]):
        if int(num1) * 10 < current_num - 10: continue
        for num2 in line[index + 1:]:
            if int(num1 + num2) > current_num:
                current_num = int(num1 + num2)

    total_joltage += current_num

print(total_joltage)