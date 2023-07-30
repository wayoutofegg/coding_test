# 20230730 Data Structure 01
#1 stack 사용법 익숙해지기

import sys
input = sys.stdin.readline

n = int(input())
ps = []

for i in range(n):
    ps.append(list(input().rstrip()))
    check = []
    for j in range(len(ps[i])):
        if ps[i][j] == '(':
            check.append(ps[i][j])
        else: #if ps[i][j] == ')':
            if '(' in check:
                check.pop()
            else:
                check.append(ps[i][j]) #if에서 출력되지 않도록!
                print('NO')
                break
                # exit() #프로그램 종료라 다음 input을 못 받음
    if len(check) == 0: print('YES')
    elif len(check) > 0 and '(' in check: print('NO')
    else: continue #len(check)>0 and ')' in check, printed NO already