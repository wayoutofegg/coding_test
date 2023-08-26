import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, read().split())
graph = [[] for _ in  range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

def Find(vertex):
    visited[vertex] = 1
    for next_vertex in graph[vertex]:
        if not visited[next_vertex]:
            Find(next_vertex)

COUNT = 0
for i in range(1, N+1):
    if not visited[i]:
        Find(i)
        COUNT += 1

print(COUNT)
