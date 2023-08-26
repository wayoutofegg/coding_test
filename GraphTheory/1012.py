from collections import deque
import sys
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    M, N, K = map(int, read().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        a, b = map(int, read().split()) #가로, 세로
        field[b][a] = 1 #세로, 가로

    def CountWorms(i, j):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        field[i][j] = 0
        queue = deque([])
        queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<N and 0<=ny<M and field[nx][ny]:
                    field[nx][ny] = 0
                    queue.append((nx,ny))
    count = 0
    for i in range(N):
        for j in range(M):
            if field[i][j]:
                CountWorms(i, j)
                count += 1
    print(count)
