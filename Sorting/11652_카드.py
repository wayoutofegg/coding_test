# ==============================
# 방법 1: dic 사용
import sys
input = sys.stdin.readline

N = int(input())
dic = dict()
for _ in range(N):
    a = int(input())
    if a not in dic:
        dic[a] = 1
    else:
        dic[a] += 1

MaxFreq = 0
MaxFreqNumbers = []

for number, count in dic.items():
    MaxFreq = max(MaxFreq, count)
for number, count in dic.items():
    if count == MaxFreq:
        MaxFreqNumbers.append(number)

MaxFreqNumbers = sorted(MaxFreqNumbers) #이런 사소한 실수로 틀리진 말자
print(MaxFreqNumbers[0])

# print(dic)
# print(MaxFreqNumbers)

# 출처: https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-11652-%EC%B9%B4%EB%93%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
# result = sorted(dic.items(),key = lambda x : (-x[1],x[0]))
# print(result[0][0])


# ===================================================
# 방법 2: Counter 사용
import sys
from collections import Counter
input = sys.stdin.readline

arr = []
N = int(input())
for _ in range(N):
    a = int(input())
    arr.append(a)

CounterArr = Counter(arr)
CountCounterArr = CounterArr.most_common()
MaxFreq = CountCounterArr[0][1]
MaxFreqNumbers = []
for number in CountCounterArr:
    if number[1] == MaxFreq:
        MaxFreqNumbers.append(number)

MaxFreqNumbers = sorted(MaxFreqNumbers)
print(MaxFreqNumbers[0][0])