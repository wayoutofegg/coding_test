import sys
input = sys.stdin.readline

n = int(input())
profile = []
for i in range(n):
    age, name = input().rstrip().split()
    profile.append([int(age), name]) 
    # 120살 - 50살 - 60살 (str로 설정할 경우!)

profile = sorted(profile, key=lambda a:a[0])
#가입한 순이라면, 따로 정렬해줄 필요는 없음

for i in range(n):
    print(profile[i][0], profile[i][1])