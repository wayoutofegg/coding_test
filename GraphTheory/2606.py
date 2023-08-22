import sys
read = sys.stdin.readline

num_computers = int(read())
num_connections = int(read())
graph = [[] for _ in range(num_computers+1)]
visited = [0 for _ in range(num_computers+1)]

for _ in range(num_connections):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

global COUNT
COUNT = 0

def DFS(now_vertex):
    global COUNT
    for next_vertex in graph[now_vertex]:
        if not visited[next_vertex]:
            COUNT += 1
            visited[next_vertex] = visited[now_vertex]

DFS(1)
print(COUNT)