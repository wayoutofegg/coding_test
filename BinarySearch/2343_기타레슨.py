import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, (input().split()))
BlueRays = list(map(int, input().split()))

def BinarySearch(left, right): # NlogN
    count = 0
    # PartialSum = 0
    SIZE = (left+right)//2
    size = SIZE
    if left > right:
        return left #SIZE 작은 경우를 찾기 위해 left만 바뀐다, 그러니 답은 right
    
    for i in range(len(BlueRays)):
        if size < BlueRays[i]:
            size = SIZE
            count+= 1
        size -= BlueRays[i]
        if i == len(BlueRays)-1 and size != SIZE:
            count +=1

    if count > M:
        return BinarySearch(SIZE + 1, right)
    elif count <= M: #같은 M 담을 수 있다면 작은 size를 출력해야 함
        return BinarySearch(left, SIZE - 1) 
    
print(BinarySearch(max(BlueRays), sum(BlueRays))) 
# 1 -> max(arr): 탐색 횟수 줄일 수 있음(X), 결과값 다름(O)
# 다 1 이라고 생각하면, 100개 5개인 것도 1으로 출력될 수 있음. 
# 가장 최소값은 max(BlueRay)임, 하나는 담을 수 있는 크기여야지

# 등호 표현이 BinarySearch의 핵심이다