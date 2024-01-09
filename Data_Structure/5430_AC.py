# 2024-01-09 FAIL
# 1. [1,2,3,4]를 파이썬 배열로 입력받는 방법 익숙해지기
  # 내가 시도한 입력 방법|Wrong; ChatGPT
  # arr_prev = input().rstrip().strip('[]').split(',')
  # arr = deque(list(map(int, arr_prev)))
# 2. len_arr과 len(arr)을 모두 활용하기

import sys
from collections import deque
input = sys.stdin.readline

testcases = int(input())

def MakeArr():
    arr_reversed = False
    commands = list(input().rstrip())
    len_arr = int(input())

    arr = input().rstrip()[1:-1].split(',')
    arr = deque(arr)
    
    for command in commands:
        if command == 'R': 
            if arr_reversed: arr_reversed = False
            else: arr_reversed = True
        else: #'D'
            if len_arr == 0: return "error"
            elif len(arr) == 0: return "error"
            else:
                if arr_reversed: arr.pop()
                else: arr.popleft()
    
    if arr_reversed: arr = reversed(arr)
    return '[' + ','.join(str(i) for i in arr) + ']'
    
for _ in range(testcases):
    print(MakeArr())


# 2023-07-31 Data Structure 20

# SUCCESS 2ND TRIAL: C+V
#0 아이디어: 자료구조 deque로 시간 절약
# from collections import deque
 
# t = int(input())
 
# for i in range(t):
#     p = input()
#     n = int(input())
#     arr = input()[1:-1].split(',')
 
#     queue = deque(arr)
 
#     flag = 0
 
#     if n == 3:
#         queue = []
 
#     for j in p:
#         if j == 'R':
#             flag += 1
#         elif j == 'D':
#             if len(queue) == 0:
#                 print("error")
#                 break
#             else:
#                 if flag % 2 == 0:
#                     queue.popleft()
#                 else:
#                     queue.pop()
 
#     else:
#         if flag % 2 == 0:
#             print("[" + ",".join(queue) + "]")
#         else:
#             queue.reverse()
#             print("[" + ",".join(queue) + "]")

# FAIL 1st TRIAL: I DON'T KNOW
# import sys
# input = sys.stdin.readline

# NumberOfTestCases = int(input())
# for TestCase in range(NumberOfTestCases):
#     #input
#     Commands = list(input().rstrip())
#     SizeOfArray = int(input())
    
#     if SizeOfArray == 0:
#         Temp = input()
#         print('error')
#         continue
#     else:
#         Array = list(map(int, input().rstrip()[1:-1].split(',')))
#     # print(Array)
    
#     # FAIL 1 INPUT ARRAY 
#     # Array = [int(i) for i in list(input().split(',')) if i.isdigit()]
    
#     # FAIL 2 INPUT ARRAY
#     # Temp = list(input().split(','))
#     # for i in range(len(Temp)):
#     #     if '[' in Temp[i]:
#     #         Array.append(int(Temp[i][1]))
#     #     if ']' in Temp[i]:
#     #         Array.append(int(Temp[i][0]))
#     #     elif Temp[i].isdigit(): 
#     #         Array.append(int(Temp[i]))

#     #initialization
#     NumberOfRCommands = 0
#     AllCommmandCompleted = 1

#     #Commands
#     for Command in Commands:
#         if Command == 'R':
#             NumberOfRCommands += 1
#         else: #Command == 'D'
#             if Array:
#                 if NumberOfRCommands%2==1:
#                     del Array[-1]
#                 else:
#                     del Array[0]
#             else:
#                 AllCommmandCompleted = 0
#                 # print('Anser: ',end='')
#                 print('error')
#                 break
    
#     #Print
#     if AllCommmandCompleted:
#         if NumberOfRCommands%2==1:
#             # print('Anser: ',end='')
#             Array.reverse()
#             print('[', ' '.join(map(str, Array[:])), ']', sep='')
#         else:
#             # print('Anser:, ',end='')
#             print('[', ','.join(map(str, Array[:])), ']', sep='')
