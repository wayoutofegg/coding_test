import sys
input = sys.stdin.readline

n = int(input())
points = []
for i in range(n):
    points.append(list(map(int,input().rstrip().split())))

points = sorted(points, key=lambda a:(a[1], a[0]))
#고려할 때 우선순위로 이해하는 게 편함

for i in range(n):
    print(points[i][0], points[i][1])