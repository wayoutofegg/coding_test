# 두 용액이랑 거의 동일해 보이는데?

import sys
input = sys.stdin.readline

n = int(input())
solutions = list(map(int, input().split()))
solutions = sorted(solutions)

left = 0
right = n-1
answer = [1000000000+1, 1000000000+1] #solutions 내 최댓값 + 1

while left < right:
    left_solution = solutions[left]
    right_solution = solutions[right]
    if abs(left_solution+right_solution) <= abs(sum(answer)):
        answer = [left_solution, right_solution]
    if left_solution + right_solution > 0:
        right -= 1
    else:
        left += 1

print(answer[0], answer[1])