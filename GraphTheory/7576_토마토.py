from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
tomato = []
RipeTomato = deque([])

for i in range(N):
    tomato.append(list(map(int, input().split())))
    for j in range(M):
        if tomato[i][j] == 1:
            RipeTomato.append((i,j))

# print(tomato)
# print(RipeTomato)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
day = 0

def BFS():
    while RipeTomato:
        # day += 1
        x, y = RipeTomato.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and tomato[nx][ny] == 0: 
                #-1은 건들지도 않음
                tomato[nx][ny] = tomato[x][y]+1
                RipeTomato.append((nx,ny))

# 출처: https://jae04099.tistory.com/entry/%EB%B0%B1%EC%A4%80-7576-%ED%86%A0%EB%A7%88%ED%86%A0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EC%84%A4%ED%8F%AC%ED%95%A8
BFS()
res = 0
for i in tomato:
    for j in i:
        if j==0: #익지 않은 토마토가 있다면
            print(-1)
            exit(0) #성공적으로 프로그램 종료
    res = max(res, max(i)) #토마토 숫자 중에 가장 큰 거 채택
print(res-1)