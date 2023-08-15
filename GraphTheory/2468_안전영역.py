# ==========================================================
# final test
from collections import deque

def BFS(v, visited, rain): #rain 변수 필요
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append(v)
    visited[v[0]][v[1]] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]\
                and fields[nx][ny]>rain:
                queue.append((nx, ny))
                visited[nx][ny] = 1

N = int(input())

fields = []
MaxRain = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    fields.append(temp)
    MaxRain = max(max(temp), MaxRain)

answer = 0

for rain in range(MaxRain):
    visited = [[0]*N for _ in range(N)] #매 반복문마다 초기화 필요
    count = 0
    for i in range(N):
        for j in range(N):
            if fields[i][j] > rain and not visited[i][j]:
                BFS((i, j), visited, rain)
                count += 1
    answer = max(answer, count)

print(answer)

# ===============================================================
# https://lakelouise.tistory.com/78
#1 3중 for문인데도 100 이하라 시간초과가 안 걸리나봄

# from collections import deque
 
# n = int(input())
# graph = []
# maxNum = 0
 
# for i in range(n):
#     graph.append(list(map(int, input().split())))
#     for j in range(n):
#         if graph[i][j] > maxNum:
#             maxNum = graph[i][j] 

# dx = [0 ,0, 1, -1]
# dy = [1, -1, 0 ,0]

# def bfs(a, b, value, visited):
#     q = deque()
#     q.append((a, b))
#     visited[a][b] = 1
 
#     while q:
#         x, y = q.popleft()
 
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if graph[nx][ny] > value and visited[nx][ny] == 0:
#                     visited[nx][ny] = 1
#                     q.append((nx, ny))
 
# result = 0
# for i in range(maxNum): #올 수 있는 비의 양
#     visited = [[0] * n for _ in range(n)]
#     cnt = 0
#     for j in range(n):
#         for k in range(n):
#             if graph[j][k] > i and visited[j][k] == 0: 
#                 bfs(j, k, i, visited)
#                 cnt += 1
#     if result < cnt:
#         result = cnt
 
# print(result)

# ====================================================
#FAIL: 3중 for문
# import sys
# input = sys.stdin.readline

# from collections import deque

# N = int(input())

# def BFS(v, RainFields):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     RainFields[v[0]][v[1]] = 0

#     queue = deque([])
#     queue.append(v)
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<N and 0<=ny<N and RainFields[nx][ny]:
#                 queue.append((nx,ny))
#                 RainFields[nx][ny] = 0
    
# fields = []; MaxHeight=0; MinHeight=0
# for i in range(N):
#     row = list(map(int, input().split()))
#     fields.append(row)
#     MaxHeight = max(max(row), MaxHeight)
#     MinHeight = min(min(row), MinHeight)

# SafetyAreas = 0

# for rain in range(MinHeight, MaxHeight+1):
#     count = 0
#     RainFields = fields
#     for i in range(N):
#         for j in range(N):
#             RainFields[i][j] = max(0, RainFields[i][j]-rain)
            
#     for i in range(N):
#         for j in range(N):
#             if RainFields[i][j]:
#                 BFS((i,j), RainFields)
#                 count += 1
    
#     SafetyAreas = max(SafetyAreas, count)

# print(SafetyAreas)