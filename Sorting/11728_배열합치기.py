A, B = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.append(1000000001)
b.append(1000000001) #IndexError 방지

answer = []
a_index = 0
b_index = 0
for _ in range(A+B):
    if a[a_index] < b[b_index]:
        answer.append(a[a_index])
        a_index += 1
    else:
        answer.append(b[b_index])
        b_index += 1

print(' '.join(map(str, answer)))