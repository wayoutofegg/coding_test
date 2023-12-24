# 2023-12-25 Correct
# 1. Deck으로 구현하면 훨씬 쉬움
import sys
from collections import deque
input = sys.stdin.readline

answer = []
N, K = map(int, input().split())
people = deque([i for i in range(1, N+1)])

for i in range(N):
    for j in range(K-1):
        people.append(people.popleft())
    answer.append(people.popleft())

print("<" + ', '.join([str(i) for i in answer]) + '>')

# 2023-07-30 Data Structure 12
# 1st Trial:
# import sys
# input = sys.stdin.readline

# PeopleinCircle, EliminatedUnit = map(int, input().split())
# RemainedPeople = [i for i in range(1, PeopleinCircle+1)]
# EliminatedPeople = []

# PersonCount = 0
# for _ in range(PeopleinCircle):
#     PersonCount += EliminatedUnit - 1 
#     if PersonCount >= len(RemainedPeople):
#         PersonCount = PersonCount%len(RemainedPeople)
#     EliminatedPeople.append(RemainedPeople[PersonCount])
#     del RemainedPeople[PersonCount]

# print('<',end='')
# for EachPerson in range(len(EliminatedPeople)):
#     if EachPerson == len(EliminatedPeople)-1:
#         print(EliminatedPeople[EachPerson], end='')
#     else:
#         print(EliminatedPeople[EachPerson], end=', ')
# print('>',end='')

# 이거 방법 Review: print('<',', '.join(map(str, EliminatedPeople[:])),'>',sep='')
