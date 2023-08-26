'''Module Providing Function Printing Python version'''
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
apts = []
for _ in range(N):
    apts.append(list(map(int, input())))

#DFS
def search_apt_complex(now_x, now_y, count):
    '''Function Printing Python version'''
    apts[now_x][now_y] = 0
    stepx = [1, -1, 0, 0]
    stepy = [0, 0, 1, -1]
    for k in range(4):
        new_x = now_x + stepx[k]
        new_y = now_y + stepy[k]
        if 0<=new_x<N and 0<=new_y<N and apts[new_x][new_y] == 1:
            apts[new_x][new_y] = 0
            search_apt_complex(new_x, new_y, count)

TotalComlex = 0
for i in range(N):
    for j in range(N):
        if apts[i][j] == 1:
            search_apt_complex(i, j, 0)
            TotalComlex += 1

print(TotalComlex)
