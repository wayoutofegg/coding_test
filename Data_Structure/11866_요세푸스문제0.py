# 2023-07-30 Data Structure 12
# 1st Trial:

import sys
input = sys.stdin.readline

PeopleinCircle, EliminatedUnit = map(int, input().split())
RemainedPeople = [i for i in range(1, PeopleinCircle+1)]
EliminatedPeople = []

PersonCount = 0
for _ in range(PeopleinCircle):
    PersonCount += EliminatedUnit - 1 
    if PersonCount >= len(RemainedPeople):
        PersonCount = PersonCount%len(RemainedPeople)
    EliminatedPeople.append(RemainedPeople[PersonCount])
    del RemainedPeople[PersonCount]

print('<',end='')
for EachPerson in range(len(EliminatedPeople)):
    if EachPerson == len(EliminatedPeople)-1:
        print(EliminatedPeople[EachPerson], end='')
    else:
        print(EliminatedPeople[EachPerson], end=', ')
print('>',end='')

# 이거 방법 Review: print('<',', '.join(map(str, EliminatedPeople[:])),'>',sep='')
