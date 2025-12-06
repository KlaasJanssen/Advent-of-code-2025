with open("data/D6.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") + " " for x in f.readlines()]

index = 0
sign_index = 0
sign = input[-1][0]
total_answer = 0
while index < len(input[0]):
    index += 1
    if index == len(input[0]) or input[-1][index] in ["+", "*"]:
        numbers = []
        for col in range(sign_index, index-1):
            number = ""
            for row in range(len(input) - 1):
                number += "" if input[row][col] == " " else input[row][col]
            numbers.append(int(number))

        if sign == "+":
            answer = sum(numbers)
        else:
            answer = 1
            for number in numbers:
                answer *= number

        total_answer += answer
        sign_index = index
        sign = input[-1][index] if index < len(input[0]) else None

print(total_answer)
