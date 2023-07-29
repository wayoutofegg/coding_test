
# dictionary 사용 익숙해지기
# 경우에 따라 어떤 자료형을 사용해야 하는지 알아야 함
#0 출처: https://hongcoding.tistory.com/76
#1 rstrip: 개행 문자 없이 입력
#2 

import sys
input = sys.stdin.readline
letters = []
alphabets = {}
NumList = []

n = int(input())
for i in range(n):
    letters.append(list(input().rstrip())) #rstrip : 개행 문자 없이 입력

for i in range(n):
    for j in range(len(letters[i])):
        if letters[i][j] in alphabets:
            alphabets[letters[i][j]] += 10**(len(letters[i])-j-1)
        else:
            alphabets[letters[i][j]] = 10**(len(letters[i])-j-1)

for val in alphabets.values():
    NumList.append(val)

NumList = sorted(NumList, reverse=True)

result = 0
allocating = 9
for num in NumList:
    result += num*allocating
    allocating -= 1

print(result)
# print(letters)
# print(alphabets)
# print(NumList)


# #FAIL MY CODE
# import sys
# input = sys.stdin.readline

# n = int(input())
# words = []
# used_alphabets = []
# used_alphabets_pos = []
# used_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in range(n):
#     words.append(list(input()))
    
# for i in range(n):
#     for j in range(len(words[i])):
#         if words[i][j] == '\n':
#             continue
#         elif words[i][j] not in used_alphabets:
#             used_alphabets.append(words[i][j])
#             used_alphabets_pos.append(len(words)-1-j)
#         # elif (words[i][j] in used_alphabets) and ():

# used_alphabets_pos = sorted(used_alphabets, reverse=True)

# num = 9
# for pos in used_alphabets_pos:
#     used_alphabets[pos] = used_numbers[num]
#     num -= 1