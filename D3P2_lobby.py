with open("data/D3.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

total_joltage = 0
for line in input:
    current_num = line[-12:]
    for num1 in line[:-12][::-1]:
        index = 0
        while index < len(current_num):
            if num1 >= current_num[index]:
                new_num = current_num[index]
                current_num = current_num[:index] + num1 + current_num[index + 1:]
                num1 = new_num
                index += 1
            else:
                break

    #print(current_num)
    total_joltage += int(current_num)

print(total_joltage)