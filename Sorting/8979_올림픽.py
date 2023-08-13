import sys
input = sys.stdin.readline

N, K  = map(int, input().split())
countries = []
medals = []
for _ in range(N):
    countries.append(list(map(int, input().split())))

countries = sorted(countries, reverse=True, key = lambda a:(a[1], a[2], a[3]))

rank = 1
temp = 1
for i in range(N):
    if i == 0:
        countries[i].append(rank)
    elif countries[i-1][1:4] == countries[i][1:4]:
        countries[i].append(rank)
        temp += 1
    else:
        rank += temp
        countries[i].append(rank)
        temp = 1

# print('-----right after ranking-----')
# print(countries)

countries = sorted(countries, key=lambda a:a[0])
# print('-----answer-----')
print(countries[K-1][4])

# print('-----Debug------')
print(countries)