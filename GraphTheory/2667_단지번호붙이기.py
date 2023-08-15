from collections import deque
N = int(input())
apts = []
for i in range(N):
    apts.append(list(map(int, input().rstrip())))
# print(apts)

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
houses = []

def BFS(v):
    count = 0
    queue = deque([])
    queue.append(v)
    while queue:
        x, y  = queue.popleft()
        count += 1
        apts[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and apts[nx][ny] == 1:
                if (nx,ny) not in queue:
                    queue.append((nx,ny))
    return count

groups = 0
for i in range(N):
    for j in range(N):
        if apts[i][j]:
            houses.append(BFS((i,j)))
            groups += 1

print(groups)
houses = sorted(houses)
print('\n'.join(map(str, houses)))