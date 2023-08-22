'''Module Providing Function Printing Python version'''

from collections import deque
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, read().split())
field = []

for _ in range(N):
    field.append(list(map(int, list(read().rstrip()))))
    #how to develop: no list()
    #field.append(list(map(int, read().rstrip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#BFS
def BFS():
    queue = deque([])
    queue.append((0,0))
    while queue:
        now_x, now_y = queue.popleft()
        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_x + dy[i]
            if 0<=next_x<N and 0<=next_y<M and field[next_x][next_y]:
                field[next_x][next_y] = field[now_x][now_y] + 1
                queue.append((next_x, next_y))
    return field[-1][-1]
print(BFS())
