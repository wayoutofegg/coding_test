from collections import deque
import sys
read = sys.stdin.readline

SUBIN, SISTER = map(int, read().split())
MAX = 100001
visited = [0]*MAX
queue = deque([SUBIN])
while queue:
    now_subin = queue.popleft()
    if SISTER == now_subin:
        print(visited[now_subin])
        break
    for next_subin in (now_subin+1, now_subin-1, now_subin*2):
        if 0<=next_subin<MAX and not visited[next_subin]:
            visited[next_subin] = visited[now_subin]+1
            queue.append(next_subin)