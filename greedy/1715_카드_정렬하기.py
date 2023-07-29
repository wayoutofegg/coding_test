#작은 건 작은 거끼리 비교, 큰건 큰 거끼리 비교하는 게 이득임
#큰 걸 작은 거랑 비교하면, 큰 수가 여러 번 세지는 효과가 나거든
#cf.    1   2   3   4   5   6   7   8   9
#       3       7       11      15          36
#       10              11      24          45
#       21                                  21
#       45                                  45

#heapq, stack, queue을 드디어 쓰는구만
#heapq; sort하면서 input 넣고 싶을 때 사용! using tree when you sort
#stack; FIFO
#queue; LIFO

import heapq # 라이브러리다, 자료구조가 아니라

cards = []
n = int(input())
for i in range(n):
    heapq.heappush(cards, int(input())) #1 heapq 알고리즘으로 list에 넣다

if len(cards) == 1:
    print(0)

else:
    answer = 0
    while len(cards) > 1:
        temp1 = heapq.heappop(cards)
        temp2 = heapq.heappop(cards)
        answer += temp1+temp2
        heapq.heappush(cards, temp1+temp2) 
        #이러면 기존에 있는 것까지 포함해서 정렬됨!
    print(answer)

# [FAIL] MY CODE
# cards = []
# total = 0
# n = int(input())
# for i in range(n):
#     cards.append(int(input()))
# cards = sorted(cards)

# while len(cards) > 1:
#     for i in range(0, len(cards), 2):
#         if i+1 == len(cards):
#             cards.append(cards[i])
#             break
#         cards[i] = cards[i]+cards[i+1]
#         cards.append(cards[i])
#         total += cards[i]
#         del cards[i]
#         del cards[i+1]

# print(total)

# # index error
# # while문 대신 짧게 쓸 수 있는 무언가로
