import sys
input = sys.stdin.readline

N = int(input())
hehave = list(map(int, input().split()))

M = int(input())
problem = list(map(int, input().split()))

hehave = sorted(hehave)

for i in range(M):
    #이진 탐색의 기본[!]
    found = 0
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right) // 2
        if problem[i] == hehave[mid]:
            found = 1
            break
        elif problem[i] > hehave[mid]:
            left = mid+1 #mid[X]
        else:
            right = mid-1 #mid[X]
    problem[i] = 1 if found else 0


print(' '.join(str(i) for i in problem)) #!

# ========================================
# import sys
# input = sys.stdin.readline

# NumberofCardsHeHave = int(input())
# CardsHeHave = list(map(int, input().split()))
# NumberofCardsToVerify = int(input())
# CardsToVerify = list(map(int, input().split()))

# CardsHeHave = sorted(CardsHeHave)
# IsInOrNot = []
# # Easier Version of 10816 as searching only
# # (no counting like 2)
# def IsCardsHeHave(i, CardsToVerify, start, end):
#     if start > end:
#         return 0
#     mid = (start+end)//2
#     if CardsToVerify[i] == CardsHeHave[mid]:
#         return 1
#     elif CardsToVerify[i] > CardsHeHave[mid]:
#         return IsCardsHeHave(i, CardsToVerify, mid+1, end)
#     else:
#         return IsCardsHeHave(i, CardsToVerify, start, mid-1)

    
# for i in range(len(CardsToVerify)):
#     start = 0
#     end = len(CardsHeHave) - 1
#     IsInOrNot.append(IsCardsHeHave(i, CardsToVerify, start, end))

# print(' '.join(str(IsInOrNot[i]) for i in range(len(IsInOrNot))))

