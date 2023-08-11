# ===========================================
from collections import deque

def BFS(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if v == k:
            return array[v]
        for next_v in (v-1, v+1, 2*v):
            if 0<=next_v<MAX and not array[next_v]:
                array[next_v] = array[v]+1
                queue.append(next_v)

n, k = map(int, input().split())
MAX = 100001
array = [0]*MAX

print(BFS(n))


# ==============================
# # first test
# from collections import deque

# def bfs(v):
#     queue = deque([v])
#     while queue:
#         v = queue.popleft()
#         if v == k:
#             return array[v]
#         for next_v in (v-1, v+1, 2*v):
#             if 0<=next_v<Max and array[next_v] == 0:
#                 array[next_v] = array[v]+1
#                 queue.append(next_v)
        
# n, k = map(int, input().split())
# Max = 100001
# array = [0]*Max
# print(bfs(n))


# ================================================
# 출처: https://chancoding.tistory.com/193
# from collections import deque

# def bfs(v):
#     q = deque([v])
#     while q:
#         v = q.popleft()
#         if v == k:
#             return array[v]
#         for next_v in (v-1, v+1, 2*v):
#             if 0 <= next_v < MAX and not array[next_v]:
#                 array[next_v] = array[v] + 1
#                 q.append(next_v)


# MAX = 100001
# n, k = map(int, sys.stdin.readline().split())
# array = [0] * MAX
# print(bfs(n))


# ========================================
# #BFS로 +1하면서 이동, 만약 K만나면 멈추고 출력

# from collections import deque

# subin, sister = map(int, input().split())
# queue = deque([subin]) 
# time = dict()
# time[subin] = 0
# memo = []

# while queue:
#     subin = queue.popleft()

#     for i in range(3):
#         if i == 0: NewSubin = subin - 1
#         elif i == 1: NewSubin = subin + 1
#         else: NewSubin = subin * 2

#     if NewSubin == sister:
#         print(time[subin]+1)
#         break
        
#     else:
#         queue.append(NewSubin)
#         time[NewSubin] = time[subin]+1 #
#         if NewSubin not in memo:
#             memo.append(NewSubin)
#         else:
#             queue.pop()
