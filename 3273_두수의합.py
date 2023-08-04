n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr = sorted(arr)

left = 0
right = n-1
count = 0
while left < right:
    if arr[left] + arr[right] == x:
        count += 1
    if arr[left] + arr[right] > x:
        right -= 1
    else:
        left += 1

print(count)