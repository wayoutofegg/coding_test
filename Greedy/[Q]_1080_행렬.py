#3 SUCCESS FINAL TEST
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0
a = []
b = []
for i in range(n):
    a.append(list(map(int, list(input().rstrip()))))
for i in range(n):
    b.append(list(map(int, list(input().rstrip()))))

def change(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if a[i][j] == 0:
                a[i][j] = 1
            else:
                a[i][j] = 0

if n<3 or m<3:
    if a!=b:
        answer = -1
else:
    for i in range(n-2): #n-2, n-1번째는 스스로 바뀔 수 없음
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                answer += 1
                change(i, j)

if answer != -1:
    if a!=b:
        answer = -1

print(answer)


# SUCCESS 2nd trial: C+V
# Q: 이게 최솟값인 걸 어떻게 보장할 수 있나..
# n, m = map(int, input().split()) 
# listA = []
# for _ in range(n): # 리스트A 선언
#     listA.append(list(map(int, list(input()))))
# listB = []
# for _ in range(n): # 리스트B 선언
#     listB.append(list(map(int, list(input()))))


# def check(i, j): # 뒤집기 함수
#     for x in range(i, i+3):
#         for y in range(j, j+3):
#             if listA[x][y] == 0:
#                 listA[x][y] = 1
#             else:
#                 listA[x][y] = 0


# cnt = 0 # 카운트
# if (n < 3 or m < 3) and listA != listB:
#     # 예외 1, 리스트가 작을 때
#     cnt = -1
# else:
#     for r in range(n-2):
#         for c in range(m-2):
#             if listA[r][c] != listB[r][c]:
#                 cnt += 1
#                 check(r, c)

# if cnt != -1:
#     if listA != listB: # A와 B가 같은지 확인
#         cnt = -1
# print(cnt)

# FAIL 1st trial: 감조차 못 잡겠음
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# a = []
# b = []
# for i in range(n):
#     a.append(list(input().rstrip()))
# for i in range(n):
#     b.append(list(input().rstrip()))

# if n < 3 or m < 3:
#     print(-1)

# else:
#     for i in range(n):
#         for j in range(m):
#             if a[i][j] != b[i][j]:
#                 for temp_i in range(i, i+3):
#                     for temp_j in range(j, j+3):
#                         if a[i][j] == 0:
                            