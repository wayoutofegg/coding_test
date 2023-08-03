# 3rd trial: final test

import sys
input = sys.stdin.readline

n = int(input())
arr = [0]*10001

for i in range(n):
    num = int(input())
    arr[num] += 1

for i in range(10001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)



# ================================================
# success 2nd trial: c+v, analysis
# import sys

# N  = int(sys.stdin.readline())
# arr = [0]*10001

# for _ in range(N):
#     num = int(sys.stdin.readline())
#     arr[num] += 1 # arr[num]에 num이 들어온 개수 count 

# for i in range(10001): 
# 	# arr[i]에 숫자가 들어왔다면 
#     if arr[i] != 0:
#     	# arr[num]에 num이 들어온 개수 만큼 출력 
#         for j in range(arr[i]): 
#             print(i)




# ===========================================
# fail 1st trial: 메모리 제한 문제가 거의 처음임
# import sys
# # import heapq #힙큐를 쓰니까 메모리초과!
# input = sys.stdin.readline

# arr = [0]*10001
# #why 수의 개수가 10,000,000개인데 10,001로 충분?
# #수의 종류가 10,001개로 한정되어 있으므로 거기에 해당 수의 개수를 입력하면 OK

# #빈 리스트에 메모리할당하면 메모리 비효율적
# #원소가 리스트를 초과할 때마다 메모리를 재할당하기 때문임

# n = int(input())
# for i in range(n):
#     arr[i] = int(input()) 
# arr = sorted(arr) 

# # print('=================================')

# for i in range(n):
#     print(arr[i])