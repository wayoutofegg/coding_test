#24 
import sys
input = sys.stdin.readline

coins = [5, 2]
result = 0
n = int(input())

for coin in coins:
    if n >= coin:
        result += n//coin    
        n = n%coin
        if n%2==1:
            n += coin
            result -= 1
    else:
        continue

if n != 0:
    print(-1)
else:
    print(result)