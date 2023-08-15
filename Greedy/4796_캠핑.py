import sys
input = sys.stdin.readline

case = 1
while True:
    available, camping, vacation = map(int, input().split())
    result = 0
    if available and camping and vacation:
        times = vacation//camping
        remain = min(available, vacation%camping) #avail보다 많이 남으면 avail만큼 써야 함
        result += available*times + remain
        print('Case {}: {}'.format(case, result))
        case += 1
        continue
    else:
        break