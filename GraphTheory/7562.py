'''This file functioning only on python'''

from collections import deque
import sys
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    N = int(read())
    startKnight = list(map(int, read().split()))
    goalKnight = list(map(int, read().split()))
    visited = [[0 for _ in range(N)] for _ in range(N)]

    #BFS:
    queue = deque([])
    queue.append((startKnight[0], startKnight[1]))
    visited[startKnight[0]][startKnight[1]] = 1

    while queue:
        nowX, nowY = queue.popleft()
        if nowX == goalKnight[0] and nowY == goalKnight[1]:
            print(visited[nowX][nowY]-1)
            break
        dx = [-2, -1, 1, 2, 2, 1, -1, -2]
        dy = [-1, -2, -2, -1, 1, 2, 2, 1]
        for i in range(8):
            nextX = nowX+dx[i]
            nextY = nowY+dy[i]
            if 0<=nextX<N and 0<=nextY<N and visited[nextX][nextY] == 0:
                #최소 횟수 출력하기 위한 if문 필요 없음
                visited[nextX][nextY] = visited[nowX][nowY]+1
                queue.append((nextX, nextY))
