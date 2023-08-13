import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
armors = list(map(int, input().split()))
armors = sorted(armors)

left = 0
right = N-1
answer = 0

while left < right:
    if M == armors[left]+armors[right]:
        answer += 1
        left += 1
        right -= 1
    elif M > armors[left]+armors[right]:
        left += 1
    else:
        right -= 1

print(answer)