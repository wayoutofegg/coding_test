# 2023-07-30 Data Structure 08

import sys
input = sys.stdin.readline

n = int(input())
deck = []

for i in range(n):
    command = list(input().split())
    if command[0] == 'push_front':
        deck.insert(0, int(command[1]))

    elif command[0] == 'push_back': #insert(-1, command[0])은 FAIL
        deck.append(int(command[1]))
        
    elif command[0] == 'pop_front':
        if deck:
            print(deck[0])
            del deck[0]
        else:
            print(-1)

    elif command[0] == 'pop_back':
        if deck:
            print(deck[-1])
            # del deck[-1]
            deck.pop()
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(deck))

    elif command[0] == 'empty':
        if deck:
            print(0)
        else:
            print(1)

    elif command[0] == 'front':
        if deck:
            print(deck[0])
        else:
            print(-1)

    elif command[0] == 'back':
        if deck:
            print(deck[-1])
        else:
            print(-1)

    else: continue