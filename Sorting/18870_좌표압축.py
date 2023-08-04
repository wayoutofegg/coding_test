


# ============================================
# 3RD TRIAL: FINAL TEST
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(list(set(arr))) #list, set 함께 적용!
answer = {arr2[i] : i for i in range(len(arr2))}

for i in arr: #arr에 있는 것들만 갖고 진행
    print(answer[i], end = ' ')

# ========================================
# 2nd trial: c+v, analysis
# 출처: 
# 아이디어: set 함수로 중복 없애고 값 len으로 값 할당한 후 출력...
# dic 한 줄 표현 기억할 것

# import sys

# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))

# arr2 = sorted(list(set(arr)))
# dic = {arr2[i] : i for i in range(len(arr2))}
# for i in arr:
#     print(dic[i], end = ' ')


# # ===========================================
# # fail 1st trial: 
# # 한 배열 안에 모든 정보를 저장하고 싶었음 
# # answer [ value, index, ConvertedValue ]

# import sys
# input = sys.stdin.readline

# n = int(input())
# numbers = list(map(int, input().split()))
# answer = [[0,0,0] for _ in range(1000001)] #주어질 수 있는 최대값보다 크게

# # answer [ value, index, ConvertedValue ]
# for i in range(n):
#     answer[i][0] = numbers[i]
#     answer[i][1] = i

# numbers = sorted(numbers)
# print('sorted numbers')
# print(numbers)
# for i in range(n):
#     if i == 0:
#         answer[i][2] = 0
#     else:
#         if numbers[i-1] == numbers[i]:
#             answer[i][2] = answer[i-1][2]
#         else:
#             answer[i][2] = i #앞에 놓인 수들의 개수

# print('before sorting')
# for i in range(n):
#     print(answer[i], end=' ')
# print()

# answer = sorted(answer, key=lambda a:a[1])

# print('final answer')
# for i in range(n):
#     print(answer[i], end=' ')