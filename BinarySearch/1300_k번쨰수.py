
# ============================
# [success] 3rd trial: final test
# why question 있음

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start = 1
end = k #why K not n*n?
result = 0

while start <= end: #같아져도 OK 
    # (등호 들어갈 수 있다면 들어가는 게 무조건 좋음, mid값 다양해짐)
    temp = 0
    mid = (start+end)//2
    for i in range(1, n+1):
        temp += min(mid//i, n)
    if temp <= k:
        result = mid
        end = mid - 1   #Q, 왜 end랑 start는 반드시 이 순서여야 하는가
    else:
        start = mid + 1
print(result)


# ============================
# [success] 2nd trial: C+V
# 출처: https://claude-u.tistory.com/449
# 0 아이디어: X보다 작은 숫자의 개수를 구하는 일반항 (temp가 핵심)
N, K = int(input()), int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2
    
    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N) #mid 이하의 i의 배수 or 최대 N
    
    if temp >= K: #이분탐색 실행
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)


# =================================================
# [fail] 1st trial: 
# 일일이 배열로 세우는 순간, 시간초과 발생하는 문제임 (X)
# i, j를 저렇게 움직일 수가 없네 -> 헛수고
# 0 1       2       3 4 5 6 7 '8'
# 0 2      '4'      6 8 10 12 
# 0 3       6       9 12
# 0 4       8       12 
# import sys
# input = sys.stdin.readline

# n = int(input())
# k = int(input())

# i, j = 1, 1

# while True:
#     if k >= 2*n-1: 
#         i += 1
#         j += 1
#         k -= 2*n-1
#     else:
#         for x in range(0, 2*n+1, 2): #1~2n-1번째로 작은 값
#             if k < x:
#                 print(i*(j+x//2))
#                 break
#         break