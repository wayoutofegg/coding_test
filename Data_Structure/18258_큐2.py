import sys
from collections import deque
sys = sys.stdin.readline #2nd? -> 시간초과

NumberOfCommands = int(input())
queue = deque([]) #1st? deque() -> 시간초과

for _ in range(NumberOfCommands): #_ 대신 Command 들어감..
    Command = list(input().split())
    if Command[0] == 'push':
        queue.append(Command[1])

    elif Command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif Command[0] == 'size':
        print(len(queue))

    elif Command[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    elif Command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    else: #Command[0] == 'back'
        if queue:
            print(queue[-1])
        else:
            print(-1)