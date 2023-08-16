'''This Code Only runs on python'''

import sys
read = sys.stdin.readline

N, M = map(int, input().split())
arr = []
# arr_check = []
count = 0

for _ in range(N):
    arr.append(read().rstrip())

for _ in range(M):
    check = read().rstrip()
    if check in arr: #10,000개 data - O(N**2) OK
        count += 1

print(count)
