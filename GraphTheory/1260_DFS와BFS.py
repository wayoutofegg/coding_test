# 3) final test
from collections import deque
# In Graph Theory, point -> vertex or node / line -> edge
# 다음부터는 point가 아닌 v, e로 나타낼 것!

def DFS(point):
    visited[point] = True
    print(point, end=' ')
    for next in graph[point]:
        if not visited[next]:
            DFS(next)

def BFS(point):
    queue = deque([point])
    visited[point] = True #V 추가
    while queue:
        v = queue.popleft()
        print(v, end=' ') #V print 위치
        for next in graph[v]:
            if not visited[next]:
                visited[next] = True
                queue.append(next) #V visit하고 append

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for points in graph:
    points.sort()

visited = [False]*(N+1)
DFS(V)
print()

visited = [False]*(N+1)
BFS(V)
# =====================
# 2) 작성해보며 이해하기
# from collections import deque
# import sys
# input = sys.stdin.readline

# def dfs(start):
#     visited[start] = True
#     print(start, end=' ')
#     for i in graph[start]:
#         if not visited[i]:
#             dfs(i)

# def bfs(start):
#     queue = deque([start])
#     visited[start] = True
#     while queue: #이거 끝나면 BFS 함수 끝남
#         v = queue.popleft()
#         print(v, end=' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 visited[i] = True 
#                 queue.append(i)

# N, M, V = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# visited = [False]*(N+1)

# for i in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b) #append로 입력, 배열 값 바꾸는 거 X
#     graph[b].append(a) #두 관계 모두 연결

# # print(graph)
# # for points in graph:
# #     points = sorted(points) #왜 이 방식으로 하면 정렬이 안 될까...

# print(graph)
# for points in graph:
#     points.sort() 
#     # points = sorted(points) X

# print(graph)

# #DFS
# visited = [False]*(N+1)
# dfs(V)
# print()

# #BFS
# visited = [False]*(N+1) 
# bfs(V)

# # 1) C+V
# # 일단 다른 사람 코드 보고 이해하기
# # 처음 푸는 DFS, BFS
# # 출처: https://ji-gwang.tistory.com/291

# from collections import deque

# def dfs(start): 
#     # 재귀
#     #Depth Frist Search: 연결해서 끝까지 방문
#     visited[start] = True
#     print(start, end=" ")

#     for i in graph[start]:
#         if not visited[i]:
#             dfs(i)


# def bfs(start): 
#     # 큐
#     #Breadth Frist Search: 하나랑 연결된 거 다 방문
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end=" ")
#         for i in graph[v]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)


# N, M, V = map(int, input().split())
# graph = [[] for _ in range(N + 1)]

# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# # 정렬
# for i in graph:
#     i.sort()

# # dfs
# visited = [False] * (N + 1)
# dfs(V)
# print()

# # bfs
# visited = [False] * (N + 1)
# bfs(V)

# # print(graph)