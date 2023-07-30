import sys
input = sys.stdin.readline

NumberofCardsHeHave = int(input())
CardsHeHave = list(map(int, input().split()))
NumberofCardsToVerify = int(input())
CardsToVerify = list(map(int, input().split()))

CardsHeHave = sorted(CardsHeHave)
IsInOrNot = []
# Easier Version of 10816 as searching only
# (no counting like 2)
def IsCardsHeHave(i, CardsToVerify, start, end):
    if start > end:
        return 0
    mid = (start+end)//2
    if CardsToVerify[i] == CardsHeHave[mid]:
        return 1
    elif CardsToVerify[i] > CardsHeHave[mid]:
        return IsCardsHeHave(i, CardsToVerify, mid+1, end)
    else:
        return IsCardsHeHave(i, CardsToVerify, start, mid-1)

    
for i in range(len(CardsToVerify)):
    start = 0
    end = len(CardsHeHave) - 1
    IsInOrNot.append(IsCardsHeHave(i, CardsToVerify, start, end))

print(' '.join(str(IsInOrNot[i]) for i in range(len(IsInOrNot))))

