#global 없이 구현할 수 있는 방법은?

N = int(input())
M = int(input())
connections = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    connections[a].append(b)
    connections[b].append(a)
# print(connections)

def DFS(v):
    global count
    count += 1
    visited[v] = True

    for next in connections[v]:
        if not visited[next]:
            DFS(next)
            
global count
count = 0
visited = [False]*(N+1)
DFS(1)
print(count-1) #except for Computer1