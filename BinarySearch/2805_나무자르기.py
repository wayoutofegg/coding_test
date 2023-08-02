

# ================================
# SUCCES 3rd TRIAL: FINAL TEST

import sys
input = sys.stdin.readline

NumberOfTrees, LogsHeNeed = map(int, input().split())
Trees = list(map(int, input().split()))
start, end = 0, max(Trees)-1
while start <= end:
    SumOfLogs = 0
    mid = (start+end) // 2
    for tree in Trees:
        if tree > mid:
            SumOfLogs += tree-mid
    if SumOfLogs >= LogsHeNeed:
        start = mid+1
    else: #SumOfLogs < LogsHeNeed
        end = mid-1

print(end) #같은 경우 고려! 

# ================================
# SUCCES 2ND TRIAL: C+V
# REFERENCE: https://claude-u.tistory.com/446
#0 아이디어: 정답 자체를 이분 탐색으로 구함 (나: 정답은 LINEAR, 마지막 나무를 이분탐색)
# TIME COMPLEXITY: O(NlogN)
# 지금까지 binary search algorithm을 단편적으로 이해(암기)하고 있었음

# N, M = map(int, input().split())
# tree = list(map(int, input().split()))
# start, end = 1, max(tree) #이분탐색 검색 범위 설정

# while start <= end: #적절한 벌목 높이를 찾는 알고리즘
#     mid = (start+end) // 2
    
#     log = 0 #벌목된 나무 총합
#     for i in tree:
#         if i >= mid:
#             log += i - mid
    
#     #벌목 높이를 이분탐색
#     if log >= M:
#         start = mid + 1
#     else:
#         end = mid - 1
# print(end)

# ===================================================
# FAIL 1ST TRIAL: TIME-OUT 6TIMES
# import sys
# input = sys.stdin.readline

# global Trees
# global previous_mid

# NumberOfTrees, TreeLengthHeNeed = map(int, input().split())
# Trees = list(map(int, input().split()))
# Trees = sorted(Trees, reverse=True)
# previous_mid = -1 #같은 tree만 있는 경우 대비

# def SearchLastTree(start, end, height):
#     global previous_mid

#     mid = (start+end)//2
#     if start > end: #원래라면 탈출 조건
#         return previous_mid
#     if height == Trees[mid]:
#         if mid == previous_mid:
#             return previous_mid
#         # 같은 높이 tree 여러 개 -> 가장 마지막 tree index를 return
#         # count 함수 대체 -> 전과 같다면 countX (시간 초과 해결2)
#         i = previous_mid+1
#         while True:
#             if i<=NumberOfTrees-1 and Trees[i] == height:
#                 i += 1
#             # if i == NumberOfTrees-1: i -= 1
#             else:
#                 break
#         NumberOfSameTrees = i - previous_mid - 1
#         if NumberOfSameTrees > 1:
#             mid = previous_mid + NumberOfSameTrees
#         previous_mid = mid        
#         return mid
#     elif height > Trees[mid]: #내림차순 정렬이라 반대로
#         return SearchLastTree(start, mid-1, height)
#     else:
#         return SearchLastTree(mid+1, end, height)

#     # Linear Search (X)
#     # i += 1 
#     # if Trees[i] <= height:
#     #     break

# global SumOfLogs
# SumOfLogs = 0

# for height in range(max(Trees), -1, -1): 
#     # for문 함수 아님
#     # global SumOfTree for문 내에서 또 선언했더니 컴파일 error
#     Temp = previous_mid
#     LastTreeIndex = SearchLastTree(0, NumberOfTrees-1, height)

#     #매번 sum할 필요 없도록/한번에 1만큼 생기니까 (시간 초과 해결1)
#     if height == Trees[LastTreeIndex]:
#         SumOfLogs += Temp+1
#     if height != Trees[LastTreeIndex]:
#         SumOfLogs += LastTreeIndex+1
    
#     if SumOfLogs >= TreeLengthHeNeed:
#         print(height)
#         break