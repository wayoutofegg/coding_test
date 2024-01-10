# 2024-01-10 PASS
import sys
input = sys.stdin.readline

coins = []
coin_types, goal = map(int, input().split())
answer = 0
for i in range(coin_types):
    coins.append(int(input()))
    
for i in range(coin_types-1, -1, -1):
    if goal >= coins[i]:
        answer += goal//coins[i]
        goal -= coins[i] * (goal//coins[i])
        
print(answer)

#1 몫 구해서 한 번에 빼는 거 습관화할 것
# count = 0
# n, k = map(int, input().split())
# coins = [0]*n
# howmany = 0

# for i in range(n):
#     coins[i] = int(input())

# for i in range(n-1, -1, -1):
#     if coins[i] > k:
#         continue
#     else:
#         while k >= coins[i]:
#             # 한 번에 뺄 수 있도록!
#             howmany = k//coins[i]
#             k -= coins[i]*howmany
#             count += howmany
#             # k = k-coins[i] 이러면 여러 번 빼야 하니까
#             # count += 1

# print(count)
