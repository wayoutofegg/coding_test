# ================================================
# Final test
#Solution 2: Using Bisect
import bisect

T = int(input())
N = int(input())
ArrA = list(map(int, input().split()))
M = int(input())
ArrB = list(map(int, input().split()))

answer = 0
Asum = ArrA
Bsum = ArrB

for a in range(N):
    for e in range(a+1, N): #하나로 구성되는 것도 OK
        Asum.append(sum(ArrA[a:e+1]))

for b in range(M):
    for e in range(b+1, M): #하나로 구성되는 것도 OK
        Bsum.append(sum(ArrB[b:e+1]))

Asum = sorted(Asum)
Bsum = sorted(Bsum)
result = 0

for i in range(len(Asum)): #Asum, Bsum 중에 긴 거 해야하지 않나
    l = bisect.bisect_left(Bsum, T-Asum[i])
    r = bisect.bisect_right(Bsum, T-Asum[i])
    result += r-l

print(result)    


# Solution 1: Using Counter
# from collections import Counter

# T = int(input())
# N = int(input())
# ArrA = list(map(int, input().split()))
# M = int(input())
# ArrB = list(map(int, input().split()))

# answer = 0
# SubArrA = Counter()

# for a in range(N):
#     for e in range(a, N):
#         SubArrA[sum(ArrA[a:e+1])] += 1

# for b in range(M):
#     for e in range(b, M):
#         temp = T - sum(ArrB[b:e+1])
#         answer += SubArrA[temp]

# print(answer)

# ==========================================
#  Solution 2: Using Bisect
# import bisect 

# T = int(input())
# N = int(input())
# arrA = list(map(int, input().split()))
# M = int(input())
# arrB = list(map(int, input().split()))

# #SubArr
# # 이분탐색이라면 left, right 강박을 버릴 것, 결과적으로 logN이면 이분 탐색인 거다
# # 출처: https://bio-info.tistory.com/206#1)_Counter_%EC%9D%B4%EC%9A%A9

# result = 0
# Asum, Bsum = arrA, arrB

# for a in range(N):
#     for e in range(a+1, N):
#         Asum.append(sum(arrA[a:e+1]))
        
# for b in range(M):
#     for e in range(b+1, M):
#         Bsum.append(sum(arrB[b:e+1]))

# Asum = sorted(Asum)
# Bsum = sorted(Bsum)

# for i in range(len(Asum)):
#     l = bisect.bisect_left(Bsum, T-Asum[i])
#     r = bisect.bisect_right(Bsum, T-Asum[i])
#     result += r-l

# print(result)

# ==========================================
#  Solution 1 : Using Counter
# from collections import Counter
# T = int(input())

# N = int(input())
# arrA = list(map(int, input().split()))
# M = int(input())
# arrB = list(map(int, input().split()))

# #SubArr
# # 이분탐색이라면 left, right 강박을 버릴 것, 결과적으로 logN이면 이분 탐색인 거다
# # 출처: https://bio-info.tistory.com/206#1)_Counter_%EC%9D%B4%EC%9A%A9

# result = 0
# SubArrA = Counter()

# for a in range(N):
#     for e in range(a, N):
#         SubArrA[sum(arrA[a:e+1])] += 1 #(Total, HowManyNumbers)

# for b in range(M):
#     for e in range(b,M):
#         temp = T - sum(arrB[b:e+1])
#         result += SubArrA[temp] #없다면 0

# print(result)