# Final Check Out
import sys
input = sys.stdin.readline

from collections import deque


def BFS(v, islands):
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    islands[v[0]][v[1]] = 0
    queue = deque([])
    queue.append(v)
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h and 0<=ny<w and islands[nx][ny]:
                queue.append((nx,ny))
                islands[nx][ny] = 0

while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break

    islands = []
    for _ in range(h):
        islands.append(list(map(int, input().split())))

    count = 0
    for i in range(h):
        for j in range(w):
            if islands[i][j]:
                BFS((i,j), islands)
                count += 1
    # print('answer: ', end=' ')
    print(count)
    

# 관련 자료: https://velog.io/@hamfan524/%EB%B0%B1%EC%A4%80-4963%EB%B2%88-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# import sys
# input = sys.stdin.readline
# # sys.setrecursionlimit(10**6)
# from collections import deque


# def BFS(islands, v, w, h):    
#     #대각선도 가능
#     dx = [-1, 1, 0, 0, 1, 1, -1, -1] 
#     dy = [0, 0, -1, 1, 1, -1, 1, -1]
#     islands[v[0]][v[1]] = 0 #[1]
#     queue = deque([])
#     queue.append(v)

#     while queue:
#         x, y = queue.popleft() #배열(X), tuple(O)
#         # islands[x][y] = 0 -> 여기 말고 [1] 위치
#         for k in range(8):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0<=nx<h and 0<=ny<w and islands[nx][ny]: #한줄에 나타나면 IndexError
#                     queue.append((nx, ny))
#                     islands[nx][ny] = 0


# while True:
#     w, h = map(int, input().split())
#     if w==0 and h==0:
#         break
#     else:
#         islands = []
#         for _ in range(h):
#             islands.append(list(map(int, input().split())))
#             #islands와 map 함수 이름이 같아 list is not callable error 발생!
#         #check
#         # print(islands)

#         count = 0
#         for i in range(h):
#             for j in range(w):
#                 if islands[i][j]:
#                     BFS(islands, (i,j), w, h)
#                     count += 1
#         # print('answer: ', end =' ') # DEBUG
#         print(count)
