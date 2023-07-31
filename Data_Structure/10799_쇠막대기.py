# 2023-07-31 Data Structure 19

# =============================================
# 2ND TRIAL: C+V
#0 아이디어: 레이저 나오는 순간, 현재 누적된 쇠막대기 모두 잘림
#출처: https://inuplace.tistory.com/844
# 문제를 이해하고 훨씬 짧은 코드를 작성하려면 어떻게 할지 고민하기

import sys
input = sys.stdin.readline

Parenthesis = list(input().rstrip())
Sticks = []
NumberOfPieces = 0

for i in range(len(Parenthesis)):
    # print(i, NumberOfPieces, Sticks)
    if Parenthesis[i] == '(':
        Sticks.append('(')
    else: #Parenthesis[i] == ')'
        if Parenthesis[i-1] == ')': #Stick 마지막
            Sticks.pop()
            NumberOfPieces += 1
        else: #Laser
            Sticks.pop()
            NumberOfPieces += len(Sticks)

# print('Answer: ', end='')
print(NumberOfPieces)


# ==============================================
# 1ST TRIAL: TIME OUT
#1 괄호 개수 엄청 많아서 시간초과 뜸... 이중 for문
# import sys
# input = sys.stdin.readline

# SticksAndLasers = list(input().rstrip())
# Sticks = []
# Lasers = []
# SticksIndex = []
# SticksCoupledIndex = []
# LasersIndex = []
# LasersCoupledIndex = []

# NowIndex = -1

# #Input Lasers and Sticks in Coupled Array
# for Parenthesis in SticksAndLasers:
#     NowIndex += 1
#     if Parenthesis == '(':
#         Sticks.append(Parenthesis)
#         SticksIndex.append(NowIndex)
#         Lasers.append(Parenthesis)
#         LasersIndex.append(NowIndex)
#     else: #Parenthesis == ')':
#         if Lasers: #IsLaserEnd
#             while Lasers:
#                 Lasers.pop()
#                 LasersIndex.pop()
#             LasersCoupledIndex.append([NowIndex-1, NowIndex])
#             Sticks.pop()
#             SticksIndex.pop()
#         else: #IsStickEnd
#             SticksCoupledIndex.append([SticksIndex[-1], NowIndex])
#             SticksIndex.pop()
#             Sticks.pop()

# # Find number of pieces
# TotalNumberOfPieces = 0
# for Stick in SticksCoupledIndex:
#     NumberOfPiecesOfStick = 1 #안 잘리면 한 조각
#     for Laser in LasersCoupledIndex:
#         start = 0
#         end = 1
#         if Stick[start]<Laser[start] and Laser[end]<Stick[end]:
#             NumberOfPiecesOfStick += 1
#     TotalNumberOfPieces += NumberOfPiecesOfStick
    
# print(TotalNumberOfPieces)
# # print(Lasers)
# # print(Sticks)
# # print('LaserCoupledIndex: ', LasersCoupledIndex)
# # print('SticksCoupledIndex: ', SticksCoupledIndex)