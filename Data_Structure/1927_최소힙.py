# 2024-01-06 PASS
#     you need to be familiar with "heapq" library

import sys
import heapq
input = sys.stdin.readline

NumberOfCommands = int(input())
Array = []

for Command in range(NumberOfCommands):
    Command = int(input())
    if Command == 0:
        if Array: print(heapq.heappop(Array))
        else: print(0)
    else:
        heapq.heappush(Array, Command)
