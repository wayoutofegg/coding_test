'''Module ProvidingFunction Printing Python version'''

from collections import deque
import sys
read = sys.stdin.readline
queue = deque([])
graph = []

M, N, H = map(int, input().split())
for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, input().split())))
        for k in range(M):
            if tmp[j][k] == 1:
                queue.append((i,j,k))
    graph.append(tmp)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while queue:
    x, y, z = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0<=nx<H and 0<=ny<N and 0<=nz<M and graph[nx][ny][nz] == 0:
            graph[nx][ny][nz] = graph[x][y][z] + 1
            queue.append((nx,ny,nz))

day = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))

print(day-1)
# reference: https://jiwon-coding.tistory.com/98
# import sys
# from collections import deque
# m,n,h = map(int,input().split()) # mn크기, h상자수
# graph = []
# queue = deque([])
# for i in range(h):
#     tmp = []
#     for j in range(n):
#         tmp.append(list(map(int,sys.stdin.readline().split())))
#         for k in range(m):
#             if tmp[j][k]==1:
#                 queue.append([i,j,k])
#     graph.append(tmp) 
# dx = [-1,1,0,0,0,0]
# dy = [0,0,1,-1,0,0]
# dz = [0,0,0,0,1,-1]
# while(queue):
#     x,y,z = queue.popleft()  
#     for i in range(6):
#         a = x+dx[i]
#         b = y+dy[i]
#         c = z+dz[i]
#         if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
#             queue.append([a,b,c])
#             graph[a][b][c] = graph[x][y][z]+1      
# day = 0
# for i in graph:
#     for j in i:
#         for k in j:
#             if k==0: #한번이라도 0이면 모두 익을 수 없는 구조임
#                 print(-1)
#                 exit(0)
#         day = max(day,max(j))
# print(day-1)
# # ====================================================
# # 분명 풀었던 문제 유형인데... 아직 멀었다
# """Module providingFunction printing python version."""

# from collections import deque
# import copy
# import sys
# read = sys.stdin.readline

# M, N, H = map(int, read().split())
# NumberOf0 = 0
# BOX = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
# for i in range(H):
#     for j in range(N):
#         arr = list(map(int, read().split()))
#         for k in range(M):
#             BOX[i][j][k] = arr[k]
#             if arr[k] == 0:
#                 NumberOf0 += 1

# # print(box)

# box = copy.deepcopy(BOX)
# answer = -1
# visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
# # 모든 노드 방문하면 -> 최대 거리 출력
# # 모든 노드 못하면   ->  -1 출력
# dx = [-1, 1, 0, 0, 0, 0]
# dy = [0, 0, -1, 1, 0, 0]
# dz = [0, 0, 0, 0, -1, 1]

# def Ripe(iGet, jGet, kGet):
#     MaxDay = 0
#     queue = deque([])
#     queue.append((0, iGet, jGet, kGet))

#     while queue:
#         ColorChanged = 0
#         day, x, y, z = queue.popleft()
#         for way in range(6):
#             nx = x + dx[way]
#             ny = y + dy[way]
#             nz = z + dz[way]
#             if 0<=nx<H and 0<=ny<N and 0<=nz<M and box[nx][ny][nz] == 0:
#                 box[nx][ny][nz] = 1
#                 queue.append((day+1, nx,ny,nz))
#                 MaxDay = max(day+1, MaxDay)
#                 ColorChanged += 1
#     if ColorChanged == NumberOf0:
#         return MaxDay
#     else:
#         return -1

# for i in range(H):
#     for j in range(N):
#         for k in range(M):
#             # 1: 익은 토마토; 0: 익지 않은 토마토; -1: 벽;
#             if box[i][j][k] == 1:
#                 answer = max(answer, Ripe(i, j, k))
#                 break

# print(answer)
# print(box)
# print(BOX)
