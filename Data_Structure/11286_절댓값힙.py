# 2023-12-25 Wrong
# 1. 여러 정보 저장하고 싶을 때는 tuple 이용할 것


# Update Data Structure 22

# =================================================
# FAIL 2nd trial: C+V
#0 아이디어: 힙을 tuple로 구성(dictionary처럼 동작)
# try excpet 구문: 예외가 발생하면 except 실행
import sys
import heapq

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
        # abs(num) 기준 정렬, 같다면 num 오름차순 정렬
    else:
        try:
            print(heapq.heappop(heap)[1])
        except: #원소가 없다면
            print(0)

# =================================================
# FAIL 1st trial: misunderstandig about heapq
# binary search로 index 줄여나가는 게 불가능
# heapq.heappush() 동작 원리 이해 부족

# 뭔가 지금까지 heapq에 대해 알고 있던 내용이 전부 무너지는 느낌임
import heapq #list에만 적용 가능
import sys
from collections import deque
input = sys.stdin.readline

IntegerArray = []
AbsValArray = []
NumberOfCommands = int(input())

global IntegerIndex #전역 변수 설정 방법 1/2
IntegerIndex = 0

def FindMinVal(Integer, start, end): #작은 값 찾기!
    if start > end:
        return 0
    mid = (start+end)//2
    if Integer == IntegerArray[mid]:
        global IntegerIndex #전역 변수 설정 방법 2/2
        IntegerIndex= mid
        return str(mid)
    elif Integer < IntegerArray[mid]:
        return FindMinVal(Integer, start, mid-1)
    else:
        return FindMinVal(Integer, mid+1, end)

for _ in range(NumberOfCommands):
    Command = int(input())
    if Command: # only 0 is false
        heapq.heappush(IntegerArray, Command) 
        heapq.heappush(AbsValArray, abs(Command))
    else:
        if IntegerArray:
            start = 0
            end = len(IntegerArray) - 1
            if FindMinVal(-AbsValArray[0], start, end): #한번에는 어려울까: 전역변수 설정
                print(IntegerArray[IntegerIndex])
                heapq.heappop(AbsValArray)
                del IntegerArray[IntegerIndex]

            elif FindMinVal(AbsValArray[0], start, end):
                print(IntegerArray[IntegerIndex])
                heapq.heappop(AbsValArray)
                del IntegerArray[IntegerIndex]

            else:
                print(heapq.heappop(IntegerArray))
                heapq.heappop(AbsValArray)
        else:
            print(0)
