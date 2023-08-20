# =================================
# 2206번 벽 부수고 이동하기, 아이디어 3차원 배열
# ref: https://baekh-93.tistory.com/27

'''Module ProvidingFunction Printing Python version'''

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
# 3차원 리스트(행, 열, 벽을 깬 여부) 생성
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# 상하좌우 이동 표시
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 큐가 빌 때까지 반복
def solve(x, y, wall_break_left, visited, graph):
    q = deque()
    # 큐에 시작 위치 삽입
    q.append((x, y, wall_break_left))
    # 방문 표시
    visited[x][y][wall_break_left] = 1
    # 큐가 빌 때까지 반복
    while q:
        x, y, wall_break_left = q.popleft()
        # 도착할 위치에 도착하였다면
        if x == n -1 and y == m -1:
            # 최단거리 횟수 리턴
            return visited[x][y][wall_break_left]
        # 이동할 수 있는 4가지 방향에 대하여
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵을 벗어나면 건너뛰기
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽을 부수지 않고 이동
            if graph[nx][ny] == 0 and visited[nx][ny][wall_break_left] == 0:
                q.append((nx, ny, wall_break_left))
                visited[nx][ny][wall_break_left] = visited[x][y][wall_break_left] + 1
            # 벽을 부수고 이동
            if graph[nx][ny] == 1 and wall_break_left == 1:
                q.append((nx, ny, wall_break_left - 1))
                visited[nx][ny][wall_break_left - 1] = visited[x][y][wall_break_left] + 1
    # 불가능할 경우 -1 리턴
    return -1

# 결과 출력
print(solve(0, 0, 1, visited, graph))
# ========================================================
# 감 자체를 못 잡음. 2차원 배열로 꾸준히 시도
# import sys
# from collections import deque
# read = sys.stdin.readline

# N, M = map(int, read().split())
# graph = [[0 for _ in range(M+1)] for _ in range(N+1)]

# for i in range(1, N+1):
#     tmp = [0]+list(map(int, list(read().rstrip())))
#     for j in range(1, M+1):
#         graph[i][j] = tmp[j]

# breakCount = 0

# #BFS
# queue = deque([])
# queue.append((1,1))
# graph[1][1] = 1
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# while queue:
#     x, y = queue.popleft()
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 1<=nx<=N and 1<=ny<=M and graph[nx][ny] == 0:
#             graph[nx][ny] = graph[x][y] + 1
#             queue.append((nx,ny))
#     if breakCount == 0:
#         for i in range(4):
#             if breakCount 


# if graph[N][M] == 0: print(-1)
# else: print(graph[N][M])
