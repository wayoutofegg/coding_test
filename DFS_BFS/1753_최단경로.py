# ===================================
# test2
import sys
import heapq
input = sys.stdin.readline #이거 추가

def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        now_weight, now = heapq.heappop(heap)
        if dp[now] < now_weight:
            continue
        for w, next in graph[now]:
            next_weight = w+now_weight
            if dp[next] > next_weight:
                dp[next] = next_weight
                heapq.heappush(heap, (next_weight, next))

V, E = map(int, input().split())
K = int(input())
INF = sys.maxsize
dp = [INF]*(V+1)
graph = [[] for _ in range(V+1)]
heap = []
for _ in range(E):
    a, b, weight = map(int, input().split())
    graph[a].append((weight, b)) #only once

Dijkstra(K)
for i in range(1, V+1):
    print('INF' if dp[i] == INF else dp[i])

# =====================================
# test 1
# import sys
# import heapq

# input = sys.stdin.readline
# INF = sys.maxsize
# V, E = map(int, input().split())
# K = int(input())
# dp = [INF]*(V+1)
# heap = []
# graph = [[] for _ in range(V+1)]

# for _ in range(E):
#     a, b, weight = map(int, input().split())
#     graph[a].append((weight, b))
#     # graph[b].append((weight, a)) 
#     # 이거 하나만 입력한다, why, Q

# def Dijkstra(start):
#     dp[start] = 0
#     heapq.heappush(heap, (0, start))
#     while heap:
#         now_weight, now = heapq.heappop(heap)
#         if dp[now] < now_weight:
#             continue
#         for w, next in graph[now]:
#             next_weight = w + now_weight
#             if next_weight < dp[next]:
#                 dp[next] = next_weight
#                 heapq.heappush(heap, (next_weight, next))


# Dijkstra(K)
# for i in range(1, V+1):
#     print('INF' if dp[i] == INF else dp[i])


# =======================================================
# 출처: https://sungmin-joo.tistory.com/33
# import sys
# import heapq

# input = sys.stdin.readline
# INF = sys.maxsize
# V, E = map(int, input().split())
# K = int(input())
# dp = [INF]*(V+1)
# heap = []
# graph = [[] for _ in range(V + 1)]

# def Dijkstra(start):
#     dp[start] = 0
#     heapq.heappush(heap,(0, start))
#     while heap:
#         wei, now = heapq.heappop(heap)
#         if dp[now] < wei:
#             continue

#         for w, next_node in graph[now]:
#             next_wei = w + wei
#             if next_wei < dp[next_node]:
#                 dp[next_node] = next_wei
#                 heapq.heappush(heap,(next_wei,next_node))

# for _ in range(E):
#     u, v, w = map(int, input().split())
#     graph[u].append((w, v))


# Dijkstra(K)
# for i in range(1,V+1):
#     print("INF" if dp[i] == INF else dp[i])


# ==================================================
# 아직 Dijkstra 알고리즘 익숙 X
# from collections import deque
# import sys
# input = sys.stdin.readline

# dp = [0]*()
# def Dijkstra(K, end): 

# N, Edges = map(int, input().split())
# K = int(input())
# graph = [[] for _ in range(N+1)]
    
# for _ in range(Edges):
#     a, b, weight = map(int, input().split())
#     graph[a].append((weight, b))
#     graph[b].append((weight, a))

# graph = sorted(graph) #최단경로

# for i in range(N):
#     if i == K:
#         print(0)
#     else:
#         temp = Dijkstra(K, i)
#         if temp:
#             print(temp)
#         else:
#             print('INF')


