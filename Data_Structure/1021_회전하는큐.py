#2023-12-24 Wrong
import sys
from collections import deque
input = sys.stdin.readline

N, commands = map(int, input().split())
indices = list(map(int, input().split()))

Queue = deque([i for i in range(1, N+1)])
NumMoveLeft = 0
NumMoveRight = 0

for i in range(commands):
    if Queue[0] == indices[i]:
        Queue.popleft() #.pop() [X] - 뺄 원소가 0번째니까
    elif Queue.index(indices[i]) > len(Queue)//2: #.index(Queue[0]) [X]
        while Queue[0] != indices[i]:
            NumMoveRight += 1
            Queue.appendleft(Queue.pop())
        Queue.popleft() #.pop() [X] 
    else:
        while Queue[0] != indices[i]:
            NumMoveLeft += 1
            Queue.append(Queue.popleft())
        Queue.popleft()
        
print(NumMoveLeft + NumMoveRight)

# ================================
# import sys
# from collections import deque
# input = sys.stdin.readline

# SizeOfQueue, NumberOfIndexesToPrint = map(int, input().split())
# #input개수 50개 이하니까 탐색 효율 걱정 X
# IndexesToPrint = list(map(int, input().split()))

# Queue = deque([i for i in range(1, SizeOfQueue+1)])
# NumberOfCommand2 = 0
# NumberOfCommand3 = 0

# for i in range(NumberOfIndexesToPrint): #0~n-1
#     if IndexesToPrint[i] == Queue[0]:
#         Queue.popleft()
#     elif Queue.index(IndexesToPrint[i]) > len(Queue)//2: #오른쪽으로 회전
#         while IndexesToPrint[i] != Queue[0]:
#             NumberOfCommand2 += 1
#             Queue.appendleft(Queue.pop())
#         Queue.popleft()
#     else: #왼쪽으로 회전
#         while IndexesToPrint[i] != Queue[0]:
#             NumberOfCommand3 += 1
#             Queue.append(Queue.popleft())
#         Queue.popleft()
#     # print(Queue)

# print(NumberOfCommand2 + NumberOfCommand3)
