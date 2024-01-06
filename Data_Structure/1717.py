# 2023-01-06 FAIL
# lack of fundamental idea
# you should review of function "find"

'''Function printing python version'''

import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

N, M = map(int, read().split())
parent = [i for i in range(N+1)]

def find(a):
    '''Function printing python version'''
    if a == parent[a]:
        return a
    parent_a = find(parent[a])
    parent[a] = parent_a
    return parent[a]

def union(a, b):
    '''Function printing python version'''
    a = find(a)
    b = find(b)
    if a == b:
        return
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    MergeOrCheck, A, B = map(int, read().split())
    if MergeOrCheck == 0: #Merge
        union(A,B)
    else: #Check
        if find(A) == find(B):
            print("YES")
        else:
            print("NO")

print(parent)

# # =========================================================
# # 핵심: 자료구조 트리 떠올리기
# # https://fre2-dom.tistory.com/197

# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N, M = map(int,input().split())

# parent = [0] * (N+1) # 부모 테이블 생성
# for i in range(N+1): # 자기 자신을 부모로 설정
#     parent[i] = i

# # 루트 노드 찾는 함수
# def find(a):
#     if a == parent[a]: # 자기 자신이 루트 노드이면 a 반환
#         return a
#     # 아니면 그런 루트를 찾을 때까지 계속 재귀
#     # cf. (1,2,3,4)+(5,6,7,8) & 1 2 7
#     # print(parent)에서 (1,1,1,1,1,5,1,5) 안나와도
#     # 루트노드 찾아서 값 출력 가능

#     p = find(parent[a]) # a의 루트 노드 찾기
#     parent[a] = p # 부모 테이블 갱신 -> 나중에는 한다리 건너 바로 찾는다
#     return parent[a] # a의 루트 노드 반환

# # a가 속해있는 집합과 b가 속해있는 집합을 합치는 연산
# def union(a,b):
#     a = find(a) # a의 루트 노드 찾기
#     b = find(b) # b의 루트 노드 찾기

#     if a == b: # a와 b의 루트 노드가 같으면 동일한 집합
#         return
#     if a < b: # a와 b의 루트 노드가 다르면 두 집합을 합치기
#         parent[b] = a
#     else:
#         parent[a] = b

# for _ in range(M):
#     o, a, b = map(int,input().split()) # operation, 원소, 원소
#     if o == 0: # o=0은 두 원소가 포함되어 있는 집합을 합치기
#         union(a,b)
#     elif o == 1: # 두 원소가 동일한 집합인지 판단
#         if find(a) == find(b):
#             print('YES')
#         else:
#             print('NO')

# print(parent)

# ========================================
# 실패
# 사유: (1,2,3,4) + (5,6,7,8) 후 2,7 TRUE 출력 불가
# for _ in range(M):
#     MergeOrCheck, a, b = map(int, read().split())
#     if MergeOrCheck == 0: #Merge
#         if a == b:
#             continue
#         if a < b:
#             if len(groups[b]) > 1:
#                 if groups[a][-1] < groups[b][-1]:
#                     groups[b].pop()
#             groups[b].append(groups[a][-1])
#         else:
#             if len(groups[a]) > 1:
#                 if groups[b][-1] < groups[a][-1]:
#                     groups[b].pop()
#             groups[a].append(groups[b][-1])

#     else:
#         if groups[a][-1] == groups[b][-1]:
#             print("YES")
#         else:
#             print("NO")

# # Debug
# print(groups)
