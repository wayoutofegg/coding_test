# 19th commit
# 예외 고려하는 게 핵심... 너무 많이 틀렸다! 정답률 25%
# n 끊어진 줄 개수
# m 브랜드 종류
# string

import sys
input = sys.stdin.readline

payment = 0
min_every = 10**5
min_each = 10**5
brands = []

n, m = map(int, input().split())
for i in range(m):
    every, each = map(int, input().split())
    brands.append([every, each])
    min_every = min(min_every, every)
    min_each = min(min_each, each)
    
payment = min(min_each*(n-n%6), min_every*(n//6)) + min(min_each*(n%6), min_every)

print(payment)
# print(min_every, min_each)

