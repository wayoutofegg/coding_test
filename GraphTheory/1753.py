import sys
import heapq
read = sys.stdin.readline

def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        now_weight, now = heapq.heappop(heap)
        if now_weight > dp[now]:
            continue
        for w, next_vertex in graph[now]:
            next_weight = w + now_weight
            if next_weight < dp[next_vertex]:
                dp[next_vertex] = next_weight
                heapq.heappush(heap, (next_weight, next_vertex))

V, E = map(int, read().split())
K = int(read())
graph = [[] for _ in range(V+1)]
dp = [sys.maxsize]*(V+1)
heap = []
for _ in range(E):
    u, v, weight = map(int, read().split())
    graph[u].append((weight, v))
    
Dijkstra(K)
for i in range(1, V+1):
    if dp[i] == sys.maxsize:
        print('INF')
    else:
        print(dp[i])