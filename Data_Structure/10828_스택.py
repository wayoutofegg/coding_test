#2023.12.24. Correct
#2023-07-30 Data Structure 02
#1 stack 선언할 때 s = stack()으로 할 필요 없음. list로도 충분히 가능

import sys
input = sys.stdin.readline

n = int(input())
command = []
stack = []

for i in range(n):
    command = list(input().split())
    if command[0] == 'push':
        stack.append(int(command[1]))

    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        print(0 if stack else 1)

    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

    else: continue #only 5 types command
    
