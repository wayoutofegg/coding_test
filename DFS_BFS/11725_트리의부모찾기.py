import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) #재귀함수 쓴다면 꼭 넣어주기

N = int(input())
graph = [[0] for _ in range(N+1)]

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0]*(N+1)
parents = [0]*(N+1)

def DFS(v, visited, parents):
    visited[v] = 1
    for next_v in graph[v]:
        if not visited[next_v]:
            parents[next_v] = v
            DFS(next_v, visited, parents)

for i in range(N+1):
    if not visited[i]:
        DFS(i, visited, parents)

for i in range(2,N+1):
    print(parents[i])