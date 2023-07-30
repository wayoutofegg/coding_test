answer = 0
n = int(input())
rowA = list(map(int, input().split()))
rowB = list(map(int, input().split()))

rowA = sorted(rowA, reverse=True)
rowB = sorted(rowB)

for i in range(n):
    answer += rowA[i]*rowB[i]

print(answer)
