#0 아이디어
#출처: https://bio-info.tistory.com/195
#1 [이중 for문 or sort 여러 개]는 대부분 시간 초과..
#3 heapq로 안 넣어도 heapq로 뺄 수 있더라

#변수 설명
# n     보석 개수           2
# k     보유 가방 개수      1 
# mass  보석 무게
# value 보석 가격
# jewerly = {mass: value}  5:10     100:100
# c     가방 무게 제한      11

#For Final Test
#1202 보석도둑

import sys
import heapq

input = sys.stdin.readline

n, k= map(int, input().split())
jews = []
bags = []
for i in range(n):
    jews.append(list(map(int, input().split())))
for i in range(k):
    bags.append(int(input()))
jews = sorted(jews, key=lambda a:a[0])
bags = sorted(bags)

# print(jews)
# print(bags)

result = 0
tmp = []

for bag in bags:
    while jews and jews[0][0] <= bag:
        heapq.heappush(tmp, -jews[0][1])
        heapq.heappop(jews)
    if tmp:
        result -= heapq.heappop(tmp)

print(result)



#For study
# import sys
# import heapq
# input = sys.stdin.readline

# #input
# jewerlies = [] #value 큰 순서대로 정렬할 수 있어야 함. dict는 불가능
# c = []
# n, k = map(int, input().split())

# for i in range(n):
#     mass, value = map(int, input().split())
#     jewerlies.append([mass, value])

# for i in range(k):
#     c.append(int(input())) #c: 가방 최대 무게 

# #max_value
# jewerlies = sorted(jewerlies, key=lambda a:a[0]) #value 큰 순 정렬
# c = sorted(c)
# max_value = 0
# tmp = []

# for each_c in c:
#     while jewerlies and jewerlies[0][0] <= each_c:
#         heapq.heappush(tmp, -jewerlies[0][1])
#         heapq.heappop(jewerlies) #3 heapq로 안 넣어도 heappop으로 뺄수 있다
#     if tmp:
#         max_value -= heapq.heappop(tmp)

# print(max_value)
    


    
# FAIL First Trial
# for i in range(max(len(jewerlies), len(c))):
#     for j in range(len(c)): #최대한 무게 제한 작은 가방에 넣어야 함
#         if jewerlies[i][0] <= c[j]:
#             if c[j] != -1: 
#                 max_value += jewerlies[i][1]
#                 c[j] = -1 #가방에 들어감
#                 break

# print(max_value)
# print(jewerlies)
# print(c)