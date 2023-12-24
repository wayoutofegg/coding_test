# 2023-12-25 
# 1. deque으로 실제 모습대로 구현하면 훨씬 쉬움
import sys
from collections import deque
input = sys.stdin.readline

answer = []
N, K = map(int, input().split())
people = deque([i for i in range(1, N+1)])

for i in range(N):
    for j in range(K-1):
        people.append(people.popleft())
    answer.append(people.popleft())

print("<" + ', '.join([str(i) for i in answer]) + '>')


#4TH TRIAL: FINAL TEST
# n, k = map(int, input().split())
# circle = [i for i in range(1, n+1)]
# answer = []

# i = 0
# for _ in range(n):
#     i += k-1
#     if i >= len(circle):
#         i = i%len(circle)

#     answer.append(str(circle.pop(i)))

# print('<',', '.join(answer[:]), '>', sep='')

#---------------------------------------------------------------
# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# people = [i for i in range(1, n+1)]
# answer = []

# i = 0
# for _ in range(n):
#     i += k-1 #i번째 원소가 사라지므로 k번째로 가려면 k-1더해야 함
#     if i >= len(people):
#         i = i%len(people) #k가 커서 몇바퀴 도는 경우 고려

#     answer.append(str(people.pop(i)))
# print('<',', '.join(answer[:]),'>', sep='') #sep: ,사이 간격 결정



#-------------------------------------------------------------
# 3rd trial: C+V
# REFERENCE: https://infinitt.tistory.com/213
# N,K = map(int,input().split())
# arr = [i for i in range(1,N+1)]    # 맨 처음에 원에 앉아있는 사람들

# answer = []   # 제거된 사람들을 넣을 배열
# num = 0  # 제거될 사람의 인덱스 번호

# for t in range(N):
#     num += K-1  
#     if num >= len(arr):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
#         num = num%len(arr)
 
#     answer.append(str(arr.pop(num)))
# print("<",", ".join(answer)[:],">", sep='')




#----------------------------------------------------------------------------
#2nd trial: 다른 방법 시도하다가 포기
# 한 번 본 적 있는 문제여서 꼭 고민해서 풀고 싶었는데, 시간 너무 잡아먹음

# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# circle = [i+1 for i in range(n)]
# answer = []

# i = -1
# # remain = 0
# while True:
#     i += 1
#     if i >= n:
#         i -= n
#     if len(circle) == 1:
#         answer.apppend(circle[i])
#         del circle[i]
#         break
#     if (i+1) % k == 0: #index 고려
#         if i > len(circle):
#             i -= k
#         answer.append(circle[i])
#         del circle[i]
#     else:
#         continue

# # only for print <1, 2, 3 ... >
# for i in range(len(answer)):
#     if i == 0:
#         print('<',end='')
#     elif i == len(answer)-1:
#         print(answer[i],end='')
#         print('>', end='')
#         break
#     print(answer[i], end = ', ')



#     if len(circle) == 1:
#         answer.append(circle[0])
#         del circle[0]
#         break

#     for i in range(1,(len(circle)+remain)//k+1):
#         answer.append(circle[i*k-1-remain])

#     temp = (len(circle)+remain)%k

#     for i in range(1,(len(circle)+remain)//k+1):
#         del circle[i*k-i-remain]
    
#     remain = temp

# print(answer)


# ----------------------------------------------------------------------------------------
# 1st trial:
# 1 example는 맞는데, test case 틀림 -> < , , > 형식 안 지켜서 그런 거였음
# 시간초과 떴음 -> go to 2nd trial
# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# circle = [i+1 for i in range(n)]
# answer = []
# # print(people)

# remain = 0
# while True:
#     if len(circle) == 1:
#         answer.append(circle[0])
#         del circle[0]
#         break

#     for i in range(1,(len(circle)+remain)//k+1):
#         answer.append(circle[i*k-1-remain])

#     temp = (len(circle)+remain)%k

#     for i in range(1,(len(circle)+remain)//k+1):
#         del circle[i*k-i-remain]
    
#     remain = temp

# for i in range(len(answer)):
#     if i == 0:
#         print('<',end='')
#     elif i == len(answer)-1:
#         print(answer[i],end='')
#         print('>', end='')
#         break
#     print(answer[i], end = ', ')
