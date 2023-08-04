# 통계학 문제 참고해서 작성
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
books = []
for i in range(n):
    books.append(input().rstrip())

books = sorted(books)
HowManySellCounter = Counter(books) # HowManySell {책 이름 : 판매량}
HowManySell = HowManySellCounter.most_common() # BestSeller 판매량
BestSellCount = HowManySell[0][1] # 가장 많이 팔린 책의 판매량
BestSellers = [] # BestSellers [ (책 이름, 판매부수) ]

for i in range(len(HowManySell)):
    if HowManySell[i][1] == BestSellCount:
        BestSellers.append(HowManySell[i])
# Check
# print(books)
# print(HowManySellCounter)
# print(BestSellers)

if len(BestSellers) == 1:
    print(BestSellers[0][0])
else:
    print(sorted(BestSellers)[0][0])