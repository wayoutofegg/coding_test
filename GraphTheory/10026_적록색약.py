import copy
from collections import deque
import sys
input = sys.stdin.readline

FieldInput = []
RG, RGB = 0, 0 #색약, 정상

N = int(input())
for _ in range(N):
    FieldInput.append(list(input().rstrip()))

def FindArea(i, j, color, field):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([])
    queue.append((i,j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and field[nx][ny] == color:
                queue.append((nx,ny))
                field[nx][ny] = 0

#정상인
# RGBfield = FieldInput # 하나의 데이터를 2개의 이름으로 가리키는 것뿐
# RGBfield = FieldInput.copy() #얕은 복사 -> 원본 데이터 변하면 변함(append 제외) 
RGBfield = copy.deepcopy(FieldInput)
for i in range(N):
    for j in range(N):
        if RGBfield[i][j] == 0:
            continue
        elif RGBfield[i][j] == 'R':
            FindArea(i,j,'R', RGBfield)
        elif RGBfield[i][j] == 'G':
            FindArea(i,j,'G', RGBfield)
        else: 
            FindArea(i,j,'B', RGBfield)
        RGB += 1

#색약인
RGfield = copy.deepcopy(FieldInput)
for i in range(N): # Red -> Green
    for j in range(N):
        if RGfield[i][j] == 'G':
            RGfield[i][j] = 'R'

for i in range(N): # field with only R & B
    for j in range(N):
        if RGfield[i][j] == 0:
            continue
        elif RGfield[i][j] == 'R':
            FindArea(i,j,'R', RGfield)
        else: 
            FindArea(i,j,'B', RGfield)
        RG += 1

print(RGB, RG)