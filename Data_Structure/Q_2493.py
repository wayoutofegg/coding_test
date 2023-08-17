'''File operating python version'''

# from collections import deque
import sys
read = sys.stdin.readline

N = int(read())
towers = [0] + list(map(int, read().split()))
answer = [0]*(N+1)
stack = [] #store index

for i in range(N, 0, -1):
    # 등호X = 본인 제외
    # tower에 닿으면 수신된다는 것으로 이해하면 됨
    stack.append(i)
    if stack and towers[i] > towers[stack[0]]:
        receiver_index = stack.pop()
        while stack:
            answer[stack.pop()] = receiver_index
        stack.append(i)

for i in range(1, N+1):
    print(answer[i], end = ' ')
