import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

answer = 0 #정수 범위여서 2로 고정시키고 시작 불가
for i in range(N):
    ArrWithoutNum = arr[:i]+arr[i+1:] #본인 제외가 핵심
    left = 0
    right = len(ArrWithoutNum)-1
    while left < right:
        if arr[i] == ArrWithoutNum[left]+ArrWithoutNum[right]:
            answer += 1
            break
        elif arr[i] > ArrWithoutNum[left]+ArrWithoutNum[right]:
            left += 1
        else:
            right -= 1 #양쪽에서 좁혀온다곤 하나, 이게 logN의 시간 효율인가?

print(answer)

# =======================
# 참고한 풀이 출처: https://baby-ohgu.tistory.com/30