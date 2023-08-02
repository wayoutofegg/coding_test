import sys
input = sys.stdin.readline

NumberOfLansHeHave, NumberOfLansHeNeed = map(int, input().split())
Lans = []
for _ in range(NumberOfLansHeHave):
    Lans.append(int(input()))

start = 1 #0으로 자를 수는 없음
end = max(Lans)
while start <= end:
    NumberOfLans = 0
    mid = (start+end)//2
    # print('before change: ', start, mid, end)
    for Lan in Lans:
        NumberOfLans += Lan//mid
    if NumberOfLans >= NumberOfLansHeNeed:
        start = mid + 1
    else: # NumberOfLans < NumberOfLansHeNeed: #가능한 것중에 제일 큰 거  
        end = mid-1
    # print('after change: ', start, mid, end)

print(end) #왜 mid가 아니라 end?
# 일단 이 기법 암기하자. 왜인지는 하다 보면 알게 될 거다