import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    print(sorted(list(map(int, input().split())))[-3])