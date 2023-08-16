# ====================================================
# 분명 풀었던 문제 유형인데... 아직 멀었다
"""Module providingFunction printing python version."""

from collections import deque
import copy
import sys
read = sys.stdin.readline

M, N, H = map(int, read().split())
NumberOf0 = 0
BOX = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        arr = list(map(int, read().split()))
        for k in range(M):
            BOX[i][j][k] = arr[k]
            if arr[k] == 0:
                NumberOf0 += 1

# print(box)

box = copy.deepcopy(BOX)
answer = -1
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
# 모든 노드 방문하면 -> 최대 거리 출력
# 모든 노드 못하면   ->  -1 출력
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def Ripe(iGet, jGet, kGet):
    MaxDay = 0
    queue = deque([])
    queue.append((0, iGet, jGet, kGet))

    while queue:
        ColorChanged = 0
        day, x, y, z = queue.popleft()
        for way in range(6):
            nx = x + dx[way]
            ny = y + dy[way]
            nz = z + dz[way]
            if 0<=nx<H and 0<=ny<N and 0<=nz<M and box[nx][ny][nz] == 0:
                box[nx][ny][nz] = 1
                queue.append((day+1, nx,ny,nz))
                MaxDay = max(day+1, MaxDay)
                ColorChanged += 1
    if ColorChanged == NumberOf0:
        return MaxDay
    else:
        return -1

for i in range(H):
    for j in range(N):
        for k in range(M):
            # 1: 익은 토마토; 0: 익지 않은 토마토; -1: 벽;
            if box[i][j][k] == 1:
                answer = max(answer, Ripe(i, j, k))
                break

print(answer)
print(box)
print(BOX)
