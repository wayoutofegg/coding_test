# 2024-01-10 FAIL
# 1. Greedy Algorithm의 기본도 모두 까먹은 듯
# 2. 이걸 2번 틀렸다. 더 열심히 공부해라
# 3. 마지막 while else 여야 break 끝나고 -1 출력 안 함

import sys
input = sys.stdin.readline
num_sugar = int(input())
num_bag = 0

while num_sugar >= 0:
    if num_sugar % 5 == 0:
        num_bag += num_sugar // 5
        print(num_bag)
        break
    num_sugar -= 3
    num_bag += 1
    
else: print("-1")
