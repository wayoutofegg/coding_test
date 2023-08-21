'''Module Providing Function Printing Python version '''

#출처: https://whitehairhan.tistory.com/333
# DFS
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]

def dfs(x):
    for i in range(n):
        if graph[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

visited = [0 for _ in range(n)]
for i in range(n):
    dfs(i)
    for j in range(n):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visited = [0 for _ in range(n)]

# =====================================================
# import sys
# read = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# N = int(read())
# graph = [[] for _ in range(N+1)]
# result = [[0 for _ in range(N+1)] for _ in range(N+1)] #visited

# for i in range(1,N+1):
#     tmp = [0] + list(map(int, input().split()))
#     for j in range(1,N+1):
#         if tmp[j]:
#             graph[i].append(j)
#             graph[j].append(i)

# def DFS(nowV, goal): 
#     #1. 코드 동작 비효율적
#     #2. 최종적으로 0/1이 return되는 구조가 아님(재귀함수라서)
#     visited[nowV] = 1
#     if nowV == goal:
#         return 1
#     for nextV in graph[nowV]:
#         if not visited[nextV]:
#             DFS(nextV, goal)

# for i in range(1,N+1):
#     for j in range(i, N+1):
#         if i == j:
#             result[i][j] = 1
#             continue
#         if result[i][j] == 0:
#             visited = [0 for _ in range(N+1)]
#             if DFS(i,j):
#                 result[i][j] = 1
#                 result[j][i] = 1
#         else: #result[i][j] == 1:
#             result[j][i] = 1

# for i in range(1,N+1):
#     for j in range(1, N+1):
#         print(result[i][j], end = ' ')
#     print()