# 2024-01-06 FAIL
#     lack of fundamental idea
#     i, j, stack, answer -> if it doesn't work then just print "NO"

# 3RD TRIAL: APPLICATION / 이제는 수정할 수 있어야 해 -> 별거 아니었네
import sys
input = sys.stdin.readline

import time
start = time.time()
#시간초과 확인, max = 100,000

n = int(input())
# n = 8 

given = []
for i in range(n):
    given.append(int(input()))
# given = [4, 3, 6, 8, 7, 5, 2, 1]
i = 0
j = 1
stack = [1]
result = ['+']

while i<=n-1: #이 조건문 수정이 핵심 
    if given[i] > j:
        j+=1
        stack.append(j)
        result.append('+')
    elif given[i] == stack[-1]:
        stack.pop()
        result.append('-')
        i += 1
    else: #elif given[i] < j:
        result = ['NO']
        break

for symbol in result:
    print(symbol)

# print(time.time()-start)





#SUCCESS 2ND TRIAL: 사소한 실수 수정
#REFERENCE: https://hongcoding.tistory.com/39
# n = int(input())
# stack = []
# answer = []
# flag = 0
# cur = 1
# for i in range(n):
#     num = int(input())
#     while cur <= num:       # 입력한 수를 만날 때 까지 오름차순으로 push
#         stack.append(cur)
#         answer.append("+")
#         cur += 1
#     # 입력한 수를 만나면 while문 탈출. 즉 cur = num일 때 까지 while문을 돌아 스택을 쌓는다.

#     if stack[-1] == num:    # stack의 TOP이 입력한 숫자와 같다면
#         stack.pop()         # 스택의 TOP을 꺼내 수열을 만들어 준다.
#         answer.append("-")
#     else:                   # stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
#         print("NO")         # 왜냐하면 12345 처럼 오름차순으로 스택이 입력되는데
#         flag = 1            # TOP이 num보다 크면 num은 TOP보다 더 아래에 쌓여있기 때문이다.
#         break               

# if flag == 0:
#     for i in answer:
#         print(i)


#FAIL 1ST TRIAL: 예제는 정답, TEST CASE 실패 
# import sys
# input = sys.stdin.readline

# import time
# start = time.time()
# #시간초과 확인, max = 100,000

# n = int(input())
# # n = 8 

# given = []
# for i in range(n):
#     given.append(int(input()))
# # given = [4, 3, 6, 8, 7, 5, 2, 1]
# i = 0
# j = 1
# stack = [1]
# result = ['+']

# while stack and i<=n-1:
#     if given[i] > j:
#         j+=1
#         stack.append(j)
#         result.append('+')
#     elif given[i] == stack[-1]:
#         stack.pop()
#         result.append('-')
#         i += 1
#     else: #elif given[i] < j:
#         result = ['NO']
#         break

# for symbol in result:
#     print(symbol)

# # print(time.time()-start)
