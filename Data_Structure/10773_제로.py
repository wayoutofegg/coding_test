# 2023.12.24. Correct
import sys
input = sys.stdin.readline

K = int(input())
correct_num = []

for i in range(K):
    temp = int(input())
    if temp != 0:
        correct_num.append(temp)
    else:
        correct_num.pop()
        
print(sum(correct_num))

#2023-07-30 Data Structure 04
# import sys
# input = sys.stdin.readline

# n = int(input())
# written = []

# for i in range(n):
#     number = int(input())
#     if number == 0:
#         written.pop()
#     else:
#         written.append(number)

# print(sum(written))
