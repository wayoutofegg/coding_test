# SUCCESS FINAL TEST
import sys
input = sys.stdin.readline

n = int(input())
positive = []
negative = []
total = 0

for i in range(n):
    number = int(input())
    if number > 1:
        positive.append(number)
    elif number == 1:
        total += 1
    else:
        negative.append(number)

positive = sorted(positive, reverse=True)
negative = sorted(negative)

if len(positive)%2==0:
    for i in range(0, len(positive)-1, 2):
        total += positive[i] * positive[i+1]
else:
    for i in range(0, len(positive)-1, 2):
        total += positive[i] * positive[i+1]
    total += positive[-1]


if len(negative)%2==0:
    for i in range(0, len(negative)-1, 2):
        total += negative[i] * negative[i+1]
else:
    for i in range(0, len(negative)-1, 2):
        total += negative[i] * negative[i+1]
    total += negative[-1]

print(total)

#0 SUCCESS 2nd Trial: reference C+V 
# 아이디어: 양/영/음 따로 계산
#1 출처: https://jokerldg.github.io/algorithm/2021/03/15/number-tie.html
# import sys
# input = sys.stdin.readline

# N = int(input())
# positive  = [] # 양수를 저장할 리스트
# negative = [] # 음수를 저장할 리스트
# max_sum = 0

# for _ in range(N):
#   n = int(input())
  
#   if n > 1:
#     positive.append(n)
#   elif n == 1:
#     max_sum += 1 # 1, 양수의 규칙에 의해 1을 더한다.
#   else:
#     negative.append(n)

# positive.sort(reverse=True) # 양수의 큰 수부터 정렬한다.
# negative.sort() # 음수의 작은 수부터 정렬한다.

# # 양수 리스트 더해주기
# if len(positive) % 2 == 0: # 양수가 짝수개 일경우 두개씩 곱해준다.
#   for i in range(0, len(positive), 2):
#     max_sum += positive[i] * positive[i+1]
# else:
#   for i in range(0, len(positive)-1, 2): 
#     max_sum += positive[i] * positive[i+1]
#   max_sum += positive[len(positive)-1] # 마지막 수는 더해준다.

# # 음수 더해주기
# if len(negative) % 2 == 0: # 음수가 짝수개 일경우 두개씩 곱해준다.
#   for i in range(0, len(negative), 2):
#     max_sum += negative[i] * negative[i+1]
# else:
#   for i in range(0, len(negative)-1, 2):
#     max_sum += negative[i] * negative[i+1]
#   max_sum += negative[len(negative)-1] # 마지막 수는 더해준다.

# print(max_sum)

# FAIL 1st Trial
# 이렇게 충분히 구할 수 있을 거 같은데... 왜 그럴까
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))

# arr = sorted(arr, reverse=True)
# total = 0
# i = 0

# while i < n-1:
#     #양수
#     if arr[i] == 1:
#         total += arr[i]
#         i+=1
#     elif arr[i] > 0 and arr[i+1] > 0:
#         total += arr[i]*arr[i+1]
#         i+=2
#     elif arr[i] > 0 and arr[i+1] == 0:
#         total += arr[i]
#         i+=1
#     elif arr[i] > 0 and arr[i] <0:
#         total += arr[i] + arr[i+1]
#         i+=2
#     #0
#     elif arr[i] == 0 and arr[i+1] == 0:
#         i+=1
#     elif arr[i] == 0 and arr[i+1] < 0:
#         if len(arr[i+1:])%2==0:
#             i+=1
#         else:
#             i+=2

#     #음수
#     else:
#     # elif arr[i] < 0 and arr[i+1] < 0: 
#         total += arr[i]*arr[i+1]
#         i+=2

# print(total+sum(arr[i:]))