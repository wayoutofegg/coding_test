from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cases = int(input())
for _ in range(cases):
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        field[b][a] = 1
    # print(field)
    
    def BFS(v):
        queue = deque([])
        queue.append(v)
        field[v[0]][v[1]] = 0
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<N and 0<=ny<M and field[nx][ny] == 1:
                    queue.append((nx,ny))
                    field[nx][ny] = 0 #nx, ny 조심
                    #초기화 2 : 여기서 초기화 안 하면 여러 좌표가 추가됨

    count = 0
    for i in range(N):
        for j in range(M):
            if field[i][j]:
                BFS((i,j))
                count += 1
    
    print(count)