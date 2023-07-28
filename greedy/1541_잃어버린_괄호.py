# 괄호는 여러 개가 될 수 있다!! -> - 뒤에 나오면 그냥 다 빼주면 돼
cut = 0
temp = 0
sentence = input()
numbers = []
symbols = []

for i in range(len(sentence)):
    if sentence[i] in '+-':
        numbers.append(int(sentence[cut:i]))
        symbols.append(sentence[i])
        cut = i+1
    if i == len(sentence)-1:
        numbers.append(int(sentence[cut:]))

answer = numbers[0]

for i in range(len(symbols)):
    if symbols[i] == '-':
        for j in range(i+1, len(symbols)+1):
            answer -= numbers[j]
        break
    else:
        answer += numbers[i+1]

print(answer)