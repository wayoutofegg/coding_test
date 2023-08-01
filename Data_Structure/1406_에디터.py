# 2023-08-02 Data Structure 24

# ========================================
# SUCCESS 3RD TRIAL: FINAL TEST

import sys
input = sys.stdin.readline

stack1 = list(input().rstrip())
stack2 = []
NumberOfCommands = int(input())


for _ in range(NumberOfCommands):
    Command = list(input().split())
    if Command[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif Command[0] == 'D': #L과 반대 동작
        if stack2:
            stack1.append(stack2.pop())
    elif Command[0] == 'B':
        if stack1:
            stack1.pop()
    else: #if Command[0] == 'P'
        stack1.append(Command[1])

stack1.extend(reversed(stack2))
print(''.join(stack1))



# ========================================
# SUCCESS 2ND TRIAL: C+V
#0 아이디어: Cursor 없이 stack 2개로 구현
#1 복붙 에러 해결: tab 모두 제거하고 스페이스바 띄어쓰기로 통일
#출처: 
import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []
# Cursor variable X

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())

    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())
            
    elif command[0] == 'B':
        if st1:
            st1.pop()
            
    else: # P
    	st1.append(command[1])
        
st1.extend(reversed(st2))
print(''.join(st1))


# =======================================
# FAIL 1ST TRIAL: TIME OUT
#1 시간 초과; INSERT, DEL 문법 자체를 교체 >> 
# import sys
# from collections import deque
# input = sys.stdin.readline

# GivenString = list(input().rstrip())
# NumberOfCommands = int(input())
# Cursor = len(GivenString)

# for _ in range(NumberOfCommands):
#     Command = list(input().split())
#     if Command[0] == 'L':
#         if Cursor:
#             Cursor -= 1
#     elif Command[0] == 'D':
#         if Cursor != len(GivenString):
#             Cursor += 1
#     elif Command[0] == 'B':
#         if Cursor:
#             Cursor -= 1
#             #2 GivenString[:Cursor].extend(GivenString[Cursor+1:]), 리스트 원소 하나씩 추가
#             #1 del GivenString[Cursor], 한칸씩 다 옮겨짐
#     else: #if Command[0] == 'P':
#         Cursor += 1

#         #1 GivenString.insert(Cursor-1, Command[1]) 한칸씩 다 옮겨짐
#         #2 Temp = GivenString[Cursor:] >> extend 하나씩 추가
#         # GivenString = GivenString[:Cursor]
#         # GivenString.append(Command[1])
#         # GivenString.extend(Temp)
#     # print(GivenString, Command)

# print(''.join(GivenString))