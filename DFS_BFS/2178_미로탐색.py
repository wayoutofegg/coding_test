# ============================================
# 4th trial: Final test

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(map(int, input().rstrip())))

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(x, y):
    queue = deque([])
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y]+1

    return maze[-1][-1]


print(BFS(0,0))
    




# ============================================
# 3rd: mid-test
from collections import deque

N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(map(int, list(input()))))

# Up, Down, right left
dx = [-1,1,0,0]
dy = [0,0,-1,1] #+- 확실하게

#Using BFS
def BFS(x, y):
    queue = deque([])
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]    

            if 0<= nx <N and 0 <= ny <M and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y]+1
                queue.append((nx, ny))
    
    return maze[N-1][M-1]

print(BFS(0,0))

# ===========================================================
# 2nd trial: C+V, analysis
# 출처: 
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip()))) # readline의 경우 맨 뒤에 '\n'까지 입력받으므로 제거해줘야 함

# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i] #new x
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    
    return graph[n-1][m-1]

print(bfs(0,0))

# ===========================================================
# 1st trial: fail
# DFS, BFS 실전 적용 방법 익숙해지기
# N, M = map(int, input().split())
# maze = []
# for i in range(N):
#     maze.append(list(map(int, list(input()))))

# #DFS 탐색
# graph = [[] for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         if maze[i][j]:
#             graph[i]