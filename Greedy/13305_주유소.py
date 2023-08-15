n = int(input())
distance = list(map(int, input().split())) #n-1
money = list(map(int, input().split())) #n
oil = money[0]
total = 0

for i in range(n-1):
    oil = min(oil, money[i])
    total += oil*distance[i]

print(total)

# 굳이 정렬할 필요는 없다. 그렇기에 따로 info 안에 묶을 필요도 없다.
# for i in range(n-1):
#     info[i][0], info[i][1] = money[i], distance[i]
#     if i == n-1:
#         info[i+1][0] = money[i+1]
