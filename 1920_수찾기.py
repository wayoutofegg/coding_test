#2023-07-30 Data Structure 03
#SUCCESS 3RD TRIAL: FINAL TEST
import sys
input = sys.stdin.readline

n = int(input())
given = list(map(int, input().split()))
m = int(input())
request = list(map(int, input().split()))
check = []

given = sorted(given)

for i in range(m):
    left = 0
    right = len(given)-1
    isFound = 0
    while left <= right:
        mid = (left+right) // 2
        if request[i] == given[mid]:
            isFound = 1
            print(1)
            break
        elif request[i] > given[mid]:
            left = mid + 1 #한칸이라도 더 가야 right보다 커져서 while문 종료되겠지!
        else: #elif request[i] < given[mid]:
            right = mid - 1
    
    if isFound == 0:
        print(0)



#SUCCESS 2ND TRIAL: C+V
#REFERENCE: https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-1920%EB%B2%88-%EC%88%98-%EC%B0%BE%EA%B8%B0-Python
#0 IDEA: BINARY SEARCH!! 
#1 각 SEARCH IDEA 익숙해져야 함!

# 입력
# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# arr = list(map(int, input().split()))
# A.sort()			# A 정렬

# # arr의 각 원소별로 이분탐색
# for num in arr:
#     lt, rt = 0, N - 1		# lt는 맨 앞, rt는 맨 뒤
#     isExist = False		# 찾음 여부

#     # 이분탐색 시작
#     while lt <= rt:		# lt가 rt보다 커지면 반복문 탈출
#         mid = (lt + rt) // 2	# mid는 lt와 rt의 중간값
#         if num == A[mid]:	# num(목표값)이 A[mid]값과 같다면 (목표값 존재여부를 알았다면)
#             isExist = True	# isExist Ture 변경
#             print(1)		# 1 출력
#             break		# 반복문 탈출
#         elif num > A[mid]:	# A[mid]가 num보다 작으면
#             lt = mid + 1	# lt를 높임
#         else:			# A[mid]가 num보다 크다면
#             rt = mid - 1	# rt를 낮춤

#     if not isExist:		# 찾지 못한 경우
#         print(0)		# 0 출력





#FAIL 1ST TRIAL: NOTHING SPECIAL
#1 그냥 곧이 곧대로 푸니까 시간 초과 떴음
#2 파이썬 내장 sort 함수 시간 복잡도 O(N*logN)
#3 어떻게 시간 복잡도를 줄일까..?

# import sys
# import heapq
# input = sys.stdin.readline

# n = int(input())
# temp = list(map(int, input().split()))
# given = []
# for i in range(n):
#     heapq.heappush(given, temp[i])

# m = int(input())
# request = list(map(int, input().split()))
# check = []
# for i in range(m):
#     heapq.heappush(check, temp[i])

# for i in range(m):
#     k = check.index(request[i])
#     while True:
#         if given[k] == request[i]:
#             print(1)
#             break
#         elif given[k] > request[i]:
#             k -= 1
#         elif given[k] < request[i]:
#             k += 1
#         elif k == 0 or k == len(request):
#             print(0)
#             break