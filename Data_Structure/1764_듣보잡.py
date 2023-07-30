import sys
input = sys.stdin.readline

NoOneHear = []
NoOneSee = []
NumberOfNoOneHear, NumberOfNoOneSee = map(int, input().split())
for _ in range(NumberOfNoOneHear):
    NoOneHear.append(input().rstrip())
for _ in range(NumberOfNoOneSee):
    NoOneSee.append(input().rstrip())

# NoOneHear = sorted(NoOneHear)
NoOneSee = sorted(NoOneSee)
NoOneHearAndSee = []

def DoesNoOneSeeHave(i, NoOneHear, start, end):
    if start > end:
        return 0
    mid = (start+end)//2
    if NoOneHear[i] == NoOneSee[mid]:
        return 1
    elif NoOneHear[i] < NoOneSee[mid]:
        return DoesNoOneSeeHave(i, NoOneHear, start, mid-1)
    else:
        return DoesNoOneSeeHave(i, NoOneHear, mid+1, end)
    
for i in range(len(NoOneHear)):
    start = 0
    end = len(NoOneSee) - 1
    if DoesNoOneSeeHave(i, NoOneHear, start, end):
        NoOneHearAndSee.append(NoOneHear[i])

NoOneHearAndSee = sorted(NoOneHearAndSee) #사전순 출력       
print(len(NoOneHearAndSee))
print('\n'.join(NoOneHearAndSee[:])) #\n이 불안함 -> .rstrip()으로 해결
# for i in range(len(NoOneHearAndSee)):
#     print(NoOneHearAndSee[i])
