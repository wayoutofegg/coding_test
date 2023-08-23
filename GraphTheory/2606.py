'''Module Providing Function Printing Python version'''
import sys
from collections import deque
read = sys.stdin.readline

N = int(input())
M = int(input())
computers = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

print(computers)

#DFS
def SearchVirus(vertex, count):
    visited[vertex] = 1
    for next_vertex in computers[vertex]:
        if not visited[next_vertex]:
            count += 1
            SearchVirus(next_vertex, count)
    return count

print(SearchVirus(1,0))
