# ============================================
# final test
# graph, visited를 인수로 넣지 않을 거라면 global로 지정해줘야 함
# 매번 인수로 넣어주는 게 정석인 듯

import sys
sys.setrecursionlimit(10**6) 
#이거 때문에 Runtime Error
# 파이썬 기본 내장 Recursion Depth가 1000이라 발생하는 문제임!
input = sys.stdin.readline

def DFS(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False]*(N+1)
count = 0

for i in range(1, N+1):
    if not visited[i]:
        DFS(graph, i, visited)
        count += 1
print(count)









# ============================================
# 전형적인 그래프 탐색 문제
# 출처: https://dduniverse.tistory.com/entry/%EB%B0%B1%EC%A4%80-11724-%EC%97%B0%EA%B2%B0-%EC%9A%94%EC%86%8C%EC%9D%98-%EA%B0%9C%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python

# from collections import deque
# import sys
# input = sys.stdin.readline

# def DFS(graph, v, visited):
#     visited[v] = True
#     for i in graph[v]:
#         if visited[i] == False:
#             DFS(graph, i, visited)

# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]

# for _ in range(M):
#     v1, v2 = map(int, input().split())
#     graph[v1].append(v2)
#     graph[v2].append(v1)

# count = 0
# visited = [False]*(N+1)

# for i in range(1, N+1):
#     if not visited[i]:
#         DFS(graph, i, visited)
#         count += 1

# print(count)