'''File functioning on python only'''

import sys
read = sys.stdin.readline

arr = []
N = int(read())
for _ in range(N):
    arr.append(int(read()))

arr = sorted(arr, reverse=True)
for i in range(N):
    print(arr[i])