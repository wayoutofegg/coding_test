'''Module Providing Function Printing Python version'''
#! modified mistakes

from collections import deque
import sys
read = sys.stdin.readline

N, M, V = map(int, read().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

for points in graph: #!
    points.sort()

def DFS(vertex):
    '''Function printing python version'''
    visited[vertex] = True
    print(vertex, end=' ')
    for next_vertex in graph[vertex]: #!
        if not visited[next_vertex]: #!
            DFS(next_vertex)

def BFS(vertex):
    '''Function printing python version'''
    visited[vertex] = True
    queue = deque([])
    queue.append(vertex)
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for next_vertex in graph[now]:
            if visited[next_vertex] is False:
                visited[next_vertex] = True
                queue.append(next_vertex)

visited = [False]*(N+1)
DFS(V)
print()

visited = [False]*(N+1)
BFS(V)
