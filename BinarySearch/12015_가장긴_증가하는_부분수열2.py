# -======================================
# success final test

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = [0] #LIS: Longest Increasing Sequence
for num in arr:
    if answer[-1]<num:
        answer.append(num)
    else:
        left = 0
        right = len(answer) #not len(arr)
        while left < right:
            mid = (left+right)//2
            if answer[mid] < num:
                left = mid+1
            else:
                right = mid
        answer[right] = num #why right not mid?
print(len(answer)-1)


# ========================================
# success c+v
# n = int(input())
# cases = list(map(int, input().split()))
# lis = [0]

# for case in cases:
#     if lis[-1]<case: #이전 수보다 크다면 일단 lis에 넣기
#         lis.append(case)
#     else:            #이전 수보다 작다면 lis 수정 필요
#         left = 0     #lis에서 case보다 한단계 작은 수 바로 앞에 입력
#         right = len(lis)

#         while left<right:
#             mid = (right+left)//2
#             if lis[mid]<case:
#                 left = mid+1
#             else:
#                 right = mid
#         lis[right] = case

# print(len(lis)-1)

# ====================================
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))

# start = 0
# end = len(arr)-1
# result = 0 

# while start <= end:
#     if start:
#         break
#     mid = (start+end) // 2
#     for i in range(mid):
#         previous = 0
#         length = 0
#         if arr[i] > previous:
#             previous = arr[i]
#             length += 1

# print(result)