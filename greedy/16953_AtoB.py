a, b = map(int, input().split())
count = 0

#0 쉬운데, 실수로 너무 많이 틀림..
#1 elif or continue
#2 if를 썼다면 else 조건 필요한지 확인할 것(test case 제시 X 예외 확인)

while True: #3 4 42처럼 지나치는 경우도 있음. 이러면 -1 출력해야 함
    count+=1
    if b < a:
        count = -1
        break

    if b == a:
        break

    if b%10 == 1:
        b = b//10
        continue #한 루프에서 연산이 한 번만 진행되어야 함 (elif도 OK)

    if b%2==0:
        b = b//2
        continue

    else:
        count = -1 # 53같은 예외 경우의 수 고려해야 함! / else 조건 필요성 여부 확인하기
        break     # 아이디어 출처: https://ralp0217.tistory.com/entry/%EB%B0%B1%EC%A4%80Python16953%EB%B2%88-A-BGreedy

print(count)