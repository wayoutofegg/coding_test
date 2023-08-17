'''This code only runs in python'''
import sys
read = sys.stdin.readline

N = int(read())
arr = list(map(int, read().split()))
answer = [-1]*N
stack = []  #index 저장

# Stack 원리 이용!
# 출처: https://hongcoding.tistory.com/40
stack.append(0)
for i in range(1, N):
    # arr[i]보다 큰 수 만날 때까지 반복
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i) # not arr[i], since stack stores index

# print(*answer)

# 증가하는 부분 수열 원리 이용?

# 오른쪽으로 이동, 자기보다 큰 거 나오면 answer
# + answer 전까지 모든 수는 answer랑 동일한 값 (X)
# 반례
# arr       5	3	2	4	6
# answer    6	4	4	6	-1


# (시간초과) 오른쪽으로 이동, 자기보다 큰 거 나오면 answer에 넣기
# for i in range(N):
#     for j in range(i, N):
#         if arr[i] < arr[j]:
#             answer[i] = arr[j]
#             break

print(' '.join(map(str, answer)))
