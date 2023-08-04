import sys
input = sys.stdin.readline

n = int(input())
students = []
for i in range(n):
    name, korean, english, math = input().rstrip().split()
    students.append([name, int(korean), int(english), int(math)])

students = sorted(students, key=lambda a: (-a[1], a[2], -a[3], a[0]))
# 하나는 오름차순, 하나는 내림차순 정렬하고 싶다면 how to -> - 붙이기!

for i in range(n):
    print(students[i][0])