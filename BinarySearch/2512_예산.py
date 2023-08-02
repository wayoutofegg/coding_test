#1 스스로 정의한 변수명에 헷갈림
#2 Q1
#3 Q2

import sys
input = sys.stdin.readline

NumberOfRegions = int(input())
Budgets = list(map(int, input().split()))
TotalBudget = int(input())

Budgets = sorted(Budgets)
start = 0
end = Budgets[-1]
result = 0

while start <= end:
    DistributedBudget = 0
    mid = (start+end)//2
    for Budget in Budgets:
        if Budget >= mid: 
            DistributedBudget += mid
        else:
            DistributedBudget += Budget

    if DistributedBudget <= TotalBudget: #Q1 같을 때 따로 안 하고 왜 함께..?
        start = mid + 1
        # break -> while문 안에 종료조건 있잖아
    else: #DistributedBudget > TotalBudget:
        end = mid - 1

print(end) #Q2