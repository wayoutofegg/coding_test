# 2024-01-10 FAIL
# 1. 전선 가격은 브랜드별로 다를 뿐
# 2. 최소값 후보 다 골라서 한 번에 최소값 출력하면 될 뿐
# 3. 6개짜리가 엄청 싸서, 이것만 사는 게 이득인 경우도 가능하다!

import sys
input = sys.stdin.readline
N, brands = map(int, input().split())
min_package = 10**3
min_each = 10**3
answer = 0

for _ in range(brands):
    package, each = map(int, input().split())
    min_package = min(min_package, package)
    min_each = min(min_each, each)
    
answer += min(min_package*(N//6), min_each*(N-N%6))
answer += min(min_package, min_each*(N%6))
print(answer)

# -===================================================
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

