import sys
from collections import deque
input = sys.stdin.readline

SizeOfQueue, NumberOfIndexesToPrint = map(int, input().split())
#input개수 50개 이하니까 탐색 효율 걱정 X
IndexesToPrint = list(map(int, input().split()))

Queue = deque([i for i in range(1, SizeOfQueue+1)])
NumberOfCommand2 = 0
NumberOfCommand3 = 0

for i in range(NumberOfIndexesToPrint): #0~n-1
    if IndexesToPrint[i] == Queue[0]:
        Queue.popleft()
    elif Queue.index(IndexesToPrint[i]) > len(Queue)//2: #오른쪽에 있음
        while IndexesToPrint[i] != Queue[0]:
            NumberOfCommand2 += 1
            Queue.appendleft(Queue.pop())
        Queue.popleft()
    else: #가운데 있다면 이 방법이 더 빠름
        while IndexesToPrint[i] != Queue[0]:
            NumberOfCommand3 += 1
            Queue.append(Queue.popleft())
        Queue.popleft()
    # print(Queue)

print(NumberOfCommand2 + NumberOfCommand3)
