#2023-07-30 Data Structure 04

import sys
input = sys.stdin.readline

n = int(input())
written = []

for i in range(n):
    number = int(input())
    if number == 0:
        written.pop()
    else:
        written.append(number)

print(sum(written))
