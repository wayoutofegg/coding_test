# ===============================
# 2nd trial: C+V
# 출처: https://chancoding.tistory.com/45
#0 아이디어: 이분 탐색

import sys
input = sys.stdin.readline

_ = int(input()) #input이 있으나, 그냥 버려도 OK하다면
N = sorted(list(map(int, input().split())))
_ = int(input())
M = map(int, input().split())

def binary(n, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if n == N[m]:
        return N[start:end+1].count(n) #해당 배열 속 n의 개수
    if n < N[m]: #m이 줄어들어서 N[m]이 n과 가까워져야함
        return binary(n, N, start, m-1)
    else:
        return binary(n, N, m+1, end)


n_dic = dict() #answer

for n in N:
    start = 0
    end = len(N)-1
    if n not in n_dic:
        n_dic[n] = binary(n, N, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M))












# =============================================================
# 1st Trial: 알고리즘은 맞는듯하나, 시간초과
#1 파이썬은 숫자 범위 벗어나면 어떻게 하지?
#    int(a) 씌우는 것처럼 double() 씌우면 되려나

import time
import sys
input = sys.stdin.readline

start = time.time()
n = int(input())
have = list(map(int, input().split()))
m = int(input())
given = list(map(int, input().split()))

have = sorted(have)
answer = dict()
for i in range(len(given)):
    if given[i] in have:
        if given[i] not in answer:
            answer[given[i]] = 1
            have.remove(given[i])
        while given[i] in have:
            answer[given[i]] += 1
            have.remove(given[i])
    else:
        answer[given[i]]=0

print(' '.join(map(str, (answer.values()))))
# print(time.time()-start)