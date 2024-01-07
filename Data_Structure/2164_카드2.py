# 2024-01-06 PASS
# Here it is, simpler version
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
cards = deque([i for i in range(1, N+1)])

while True:
    if len(cards) == 1:
        print(cards.pop())
        break
    else:
        cards.popleft()
        cards.append(cards.popleft())

# 2023-07-30 Data Structure 06

# import time
# start = time.time()

# import sys
# input = sys.stdin.readline

# n = int(input())
# cards = []
# for i in range(1,n+1):
#     cards.append(i)

# while len(cards) > 1:
#     if len(cards)%2==0:
#         temp = []
#         for i in range(len(cards)//2):
#             temp.append(cards[i*2+1])
#         cards = temp
#     else:
#         temp = [cards[-1]]
#         del cards[-1]
#         for i in range(len(cards)//2):
#             temp.append(cards[i*2+1])
#         cards = temp

#     # del cards[0]
#     # cards.append(cards[0])
#     # del cards[0] #-------------------> 시간초과

# print(cards[0])
# print(time.time()-start)


#100,000            23s 
#30,000 -> 27232    2.18s
#10,000 -> 3616     0.22s 
