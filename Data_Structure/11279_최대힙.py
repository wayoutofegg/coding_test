# 2023-12-25 Wrong
# 1. heapq algorithm 사용법 익히기
# 2. else: print(0) 적용

# 2023-07-31 Data Structure 17

import sys
import heapq
input = sys.stdin.readline

NumberOfCommands = int(input())
Array = []

for Command in range(NumberOfCommands):
    Command = -int(input())
    if Command == 0:
        if Array:
            print(-heapq.heappop(Array))
        else:
            print(0)
    else:
        heapq.heappush(Array, Command)
