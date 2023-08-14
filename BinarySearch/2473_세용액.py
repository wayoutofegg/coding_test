# 하나는 고정(N)하고, 다른 2개가 움직임(NlogN)

# if문 위치 바꿈 -> 이거 하나 때문에 시간 절약 효과!! 
# minTake = sys.maxsize로 선언

import sys
input = sys.stdin.readline

N = int(input())
Solutions = list(map(int, input().split()))
Solutions = sorted(Solutions)

answer = []
minTake = sys.maxsize #10**9*3+1 #for문 밖에서 선언
MixedSolution = 0 
for i in range(N-2): #not N, since) i(N-3), N-2, N-1 살피는 게 마지막 case이기 때문
    FirstSolution = Solutions[i]
    left = i+1 #not i, since) FirstSoltuion 다음부터
    right = N-1
    while left < right:
        MixedSolution = FirstSolution + Solutions[left] + Solutions[right]
        if abs(MixedSolution) < minTake:
            minTake = abs(MixedSolution) #minTake 도입 for abs, sum 연산 간소화
            answer = [FirstSolution, Solutions[left], Solutions[right]]
        if MixedSolution < 0:
            left += 1
        elif MixedSolution > 0: #not ph > abs(sum(answer)) since) 이게 이 BinarySearch의 근본 원리
            right -= 1
        else:
            break

for num in answer:
    print(num, end=' ')


# =======================================
# 출처: https://zu-techlog.tistory.com/25 
# import sys
# input = sys.stdin.readline

# n = int(input())
# lst = sorted(list(map(int, input().split())))

# res = 4000000000 #임의의 max값
# sol_candi = []

# for i in range(n-2):
#     refer = lst[i]
#     l_p = i+1 #왼쪽 포인터
#     r_p = n-1 #오른쪽 포인터
#     while l_p < r_p:
#         cur_sum = refer + lst[l_p] + lst[r_p]
#         if abs(cur_sum) <= abs(res): #기준값보다 작으면
#             sol_candi = [refer, lst[l_p], lst[r_p]] #세 용액 업데이트
#             res = refer + lst[l_p] + lst[r_p] #결과값 업데이트
#         if cur_sum < 0:
#             l_p += 1
#         elif cur_sum > 0:
#             r_p -= 1
#         else:
#             print(*sol_candi)
#             sys.exit()

# print(*sol_candi)
# # * : list, tuple 지칭, parameter가 몇 개인지는 모르겠지만, 그 안의 원소 모두 출력
# # def functionA(*args)로 활용 가능: args = arguments, kargs = key arguments
# # ** : dictionary 지칭