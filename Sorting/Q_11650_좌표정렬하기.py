import sys
input = sys.stdin.readline

n = int(input())
points = []

for i in range(n):
    points.append(list(map(int, input().split())))

# points = sorted(points) -> OK
points = sorted(points, key=lambda a:(a[0], a[1]))
# a[0] 오름차순, a[0] 같다면 a[1] 오름차순

# Q_왜 아래처럼 정렬하면 틀리는 건가
# points = sorted(points, key = lambda a:a[1]) #y좌표 증가순
# points = sorted(points, key = lambda a:a[0]) #x좌표 증가순(y도 증가순)

# print('----------- answer ------------')
for i in range(n):
    print(points[i][0], points[i][1])