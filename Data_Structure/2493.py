# 2024-01-09 FAIL
# 1. 그냥 3번 써보면서 외운 듯 (실전성 부족)
# 2. 정보 여러 개 저장하고 싶을 떄는 2차원 배열 떠올릴 것

import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > towers[i]:
            answer.append(stack[-1][0] + 1)
            break
        else: stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i, towers[i]])
    
print(' '.join(str(i) for i in answer))
