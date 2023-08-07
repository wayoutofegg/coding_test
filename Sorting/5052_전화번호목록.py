#0 아이디어
# 하나가 다른 언어의 접두어라면 정렬했을 떄 두 수는 인접해있을 거다

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input()) #전화번호개수
    PhoneNumbers = [input().rstrip() for _ in range(n)]
    PhoneNumbers = sorted(PhoneNumbers)
    # 하나가 다른 언어의 접두어라면 정렬했을 떄 두 수는 인접해있을 거다

    Consistency = 1
    for i in range(n-1):
        if PhoneNumbers[i] == PhoneNumbers[i+1][:len(PhoneNumbers[i])]:
            #2차원 배열 가능하게 하려고 문자로 입력 받음
            Consistency = 0
            print('NO')
            break

    if Consistency:
        print('YES')


    