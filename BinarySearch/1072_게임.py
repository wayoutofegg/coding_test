tot, win = map(int, input().split())
Z = win*100 // tot     #int((win/tot*100)%100) -> 실패 
# 몫만 취하고 나머지는 버리니까 이런 식으로도 구현 가능!

# 실패한 원인: 부동소수점 반올림 오차
# 해결 1: 오차가 sys.float_info.epsilon보다 작거나 같은지 판단
# 해결 2: math.isclose 사용  (단, Python 3.5이상)
# 해결 3: Decimal 사용
# (해결 4: Fraction 사용, 이 문제에서는 적용 불가)

start = 1
end = 1000000000 #넣을 수 있는 최댓값
global moregame
moregame = 0

while start <= end:
    mid = (start+end)//2
    new_win = win + mid
    new_tot = tot + mid
    if new_win*100 // new_tot != Z:
        end = mid - 1
        moregame = mid
    else:
        start = mid + 1

if Z >= 99: #직관
    print(-1)
else:
    print(moregame)