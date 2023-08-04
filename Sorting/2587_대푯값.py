arr = []
for _ in range(5):
    arr.append(int(input()))

arr = sorted(arr)
print(sum(arr)//5) #자연수라는 전제
print(arr[2])