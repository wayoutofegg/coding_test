'''File Functioning on python'''

import sys
read = sys.stdin.readline

A, B = map(int, read().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA = sorted(arrA)
arrB = sorted(arrB)

#A-B
countA_B = 0
for i in range(A):
    left = 0
    right = B-1 #일치하는 B원소를 찾는 것
    while left <= right:
        mid = (left+right)//2
        if arrA[i] == arrB[mid]:
            countA_B += 1
            break
        elif arrA[i] > arrB[mid]:
            left = mid + 1
        else:
            right = mid - 1

#B-A            
countB_A = 0
for i in range(B):
    left = 0
    right = A-1 #일치하는 A원소를 찾는 것
    while left <= right:
        mid = (left+right)//2
        if arrB[i] == arrA[mid]:
            countB_A += 1
            break
        elif arrB[i] > arrA[mid]:
            left = mid + 1
        else:
            right = mid - 1

print(A+B-countA_B-countB_A)