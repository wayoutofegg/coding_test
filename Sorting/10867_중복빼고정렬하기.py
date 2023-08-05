import sys
input = sys.stdin.readline

N = int(input())
arr = list(set(map(int, input().rstrip().split())))
print(' '.join(map(str, sorted(arr))))