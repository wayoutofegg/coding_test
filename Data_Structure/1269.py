# 2023-12-25 Correct
# 1. 어차피 교집합의 개수는 동일, 탐색 한 번으로 충분
# 2. 하나만 sort해도 돼. 한 쪽은 크기 상관 없이 앞부터 차례대로 보니까.
import sys
from collections import deque
input = sys.stdin.readline

count = 0
sizeA, sizeB = map(int, input().split())
groupA = list(map(int, input().split()))
groupB = list(map(int, input().split()))

groupA = sorted(groupA)

# Binary Search
for i in range(sizeB):
    left = 0
    right = sizeA - 1
    while left <= right:
        mid = (left + right) // 2
        if groupB[i] == groupA[mid]:
            count += 1
            break
        elif groupB[i] > groupA[mid]:
            left = mid + 1
        else:
            right = mid - 1
        
print(sizeA + sizeB - count*2)

# '''File Functioning on python'''

# import sys
# read = sys.stdin.readline

# A, B = map(int, read().split())
# arrA = list(map(int, input().split()))
# arrB = list(map(int, input().split()))

# arrA = sorted(arrA)
# arrB = sorted(arrB)

# #A-B
# countA_B = 0
# for i in range(A):
#     left = 0
#     right = B-1 #일치하는 B원소를 찾는 것
#     while left <= right:
#         mid = (left+right)//2
#         if arrA[i] == arrB[mid]:
#             countA_B += 1
#             break
#         elif arrA[i] > arrB[mid]:
#             left = mid + 1
#         else:
#             right = mid - 1

# #B-A            
# countB_A = 0
# for i in range(B):
#     left = 0
#     right = A-1 #일치하는 A원소를 찾는 것
#     while left <= right:
#         mid = (left+right)//2
#         if arrB[i] == arrA[mid]:
#             countB_A += 1
#             break
#         elif arrB[i] > arrA[mid]:
#             left = mid + 1
#         else:
#             right = mid - 1

# print(A+B-countA_B-countB_A)
