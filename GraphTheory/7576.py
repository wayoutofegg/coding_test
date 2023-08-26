from collections import deque
import sys
read = sys.stdin.readline

W, H = map(int, (input().split()))
field = []
queue = deque([])
for i in range(H):
    temp = list(map(int, input().split()))
    for j in range(W):
        if temp[j] == 1:
            queue.append((i, j))
    field.append(temp)

#BFS
while queue:
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    y, x = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<W and 0<=ny<H and field[ny][nx]==0:
            field[ny][nx] = field[y][x] + 1
            queue.append((ny, nx))

DaySpent = 0
ALLRIPED = True
for i in range(H):
    for j in range(W):
        if field[i][j] == 0:
            ALLRIPED = False
            break
        else:
            DaySpent = max(DaySpent, field[i][j])

if not ALLRIPED:
    print(-1)
else:
    print(DaySpent-1)