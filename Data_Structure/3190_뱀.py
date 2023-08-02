

# 시간초과 걱정 없이 구현해도 OK
# NOT FINISHED / 시간 초과 여부 체크해보기
# Snake, Apple deque로 구현하면 시간 줄일 수 있음(del -> popleft)

import sys
input = sys.stdin.readline

BoardSize = int(input())
NumberOfApples = int(input())
XYofApples = []
XYofSnake = [[1,1]]
for _ in range(NumberOfApples):
    XYofApples.append(list(map(int, input().rstrip().split())))

NumberOfRotations = int(input())
RotationsOfSnake = [] #L: <-, D: ->
for _ in range(NumberOfRotations):
    temp = input().split()
    RotationsOfSnake.append([int(temp[0]), temp[1]])

global Board
Board = [[1 for _ in range(BoardSize+2)] for _ in range(BoardSize+2)]
for i in range(BoardSize+2):
    for j in range(BoardSize+2):
        if i == 0 or i == BoardSize+1:
            Board[i][j] = 0
        if j == 0 or j == BoardSize+1:
            Board[i][j] = 0

# Check if inputs are valid 
# print(XYofApples)
# print(RotationsOfSnake)

def SnakeMove(time, XYofApples):
    #Snake Direction
    global SnakeDirection, SnakeRow, SnakeCol

    if RotationsOfSnake:
        if time-1 == RotationsOfSnake[0][0]:
            if RotationsOfSnake[0][1] == 'L':
                SnakeDirection += 90
            else: #RotationsOfSnake[0][1] == 'D'
                SnakeDirection += 270
            del RotationsOfSnake[0]

    #SnakeMove
    if SnakeDirection%360 == 0: #Right
        SnakeCol += 1
    if SnakeDirection%360 == 90: #Up
        SnakeRow -= 1
    if SnakeDirection%360 == 180: #Left
        SnakeCol -= 1
    if SnakeDirection%360 == 270: #Down
        SnakeRow += 1

    #Check Snake Overlap/Check It is wall
    if Board[SnakeRow][SnakeCol] == 'S' or\
        Board[SnakeRow][SnakeCol] == 0:
        return 1
    Board[SnakeRow][SnakeCol] = 'S'

    # print([SnakeRow, SnakeCol])
    # print(XYofApples)

    #Check Apple
    if [SnakeRow, SnakeCol] not in XYofApples:
        Board[XYofSnake[0][0]][XYofSnake[0][1]] = 1
        del XYofSnake[0]
    if [SnakeRow, SnakeCol] in XYofApples:
        XYofApples.remove([SnakeRow, SnakeCol])
    XYofSnake.append([SnakeRow, SnakeCol])
    return 0


time = 0
global SnakeRow, SnakeCol, SnakeDirection, ShouldStop
SnakeDirection = 0; ShouldStop = 0
SnakeRow = 1; SnakeCol = 1
Board[SnakeRow][SnakeCol] = 'S'

while True:
    time += 1
    if SnakeMove(time, XYofApples): #return 1 = shouldstop
        break
    # for i in range(BoardSize+2):
    #     for j in range(BoardSize+2):
    #         print(Board[i][j], end=' ')
    #     print()
    # print(SnakeDirection)
print(time)