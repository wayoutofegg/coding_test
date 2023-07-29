#3nd [PASS] FINAL TEST

import sys
input = sys.stdin.readline

n, length = map(int, input().split())
water = list(map(int, input().split()))
water = sorted(water) #정렬 잊지 말기

result = 1 #마지막 고려하기 위해 +1!
start = water[0]-0.5
end = start + length

for i in range(n):
    if start < water[i] < end:
        continue
    else:
        result += 1
        start = water[i]-0.5
        end = start + length

print(result)

# 2nd [PASS] Trial C+V
# reference: https://data-flower.tistory.com/53
#0 핵심 아이디어: 문제 취지대로 식을 구성해라

# import sys
# input = sys.stdin.readline

# N , L = map(int, input().split())
# arr = list(map(int, input().split(' ')))
# arr.sort()

# start = arr[0]-0.5
# end = start + L
# cnt = 1
# for i in range(0, len(arr)): 
#   if start< arr[i] < end: #0 여기가 핵심
#     continue
#   else:
#     cnt+=1
#     start = arr[i]-0.5
#     end = start + L

# print(cnt)





# FAIL 1st trial: 복잡한 조건문
# import sys
# input = sys.stdin.readline

# result = 0
# tapes = 1
# n, length = map(int, input().split())
# water = list(map(int, input().split()))
# water = sorted(water)

# for i in range(n):
#     happen = 0
#     if i == n-1:
#         if tapes > length:
#             if tapes%length == 0:
#                 result += tapes // length
#             else: 
#                result += tapes // length + 1
#         else:
#             result += 1
#         tapes = 1
#         break

#     elif water[i+1] == water[i]+1:
#         happen = 1
#         tapes += 1
      
#     elif happen == 0:
#         if tapes > length:
#             if tapes%length == 0:
#                 result += tapes // length
#             else: 
#                result += tapes // length + 1
#         else:
#             result += 1
#         tapes = 1

#     else: continue

# print(result)