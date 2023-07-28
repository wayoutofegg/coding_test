n = int(input())
times = list(map(int, input().split()))
times.sort()
answer = 0

for i in range(n):
    answer += sum(times[0:i+1])

print(answer)
