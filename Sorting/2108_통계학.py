# 3rd trial: final test
# COunter 함수 아직 덜 익숙함..
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
AllNumbers = []

for i in range(n):
    number = int(input())
    AllNumbers.append(number)
AllNumbers = sorted(AllNumbers)
# 최빈값 구하기
MostFreqNumber = 0
CounterAllNumbers = Counter(AllNumbers)
Freqs = CounterAllNumbers.most_common()
Max_Freq = Freqs[0][1] #[[], [], [숫자, 빈도수], ... ]
Max_Freqs = []

for Freq in Freqs:
    if Freq[1] == Max_Freq:
        Max_Freqs.append(Freq[0]) #최빈'값'만 저장

if len(Max_Freqs) == 1:
    MostFreqNumber = Max_Freqs[0]
else:
    MostFreqNumber = sorted(Max_Freqs)[1]
# print(Freqs)


#print answers
# print('---------------------------')

print(round(sum(AllNumbers)/n))
# print('{:.0f}'.format(sum(AllNumbers)/n)) -0.3 -> -0으로 출력됨
print(AllNumbers[n//2])
print(MostFreqNumber)
print(max(AllNumbers)-min(AllNumbers))





# ===========================
# 2nd trial: c+v, analysis
# 해설: Counter 함수 활용해서 최빈값 구하기
# 출처: https://gyujh.tistory.com/16

# import sys
# from collections import Counter

# n = int(sys.stdin.readline())
# a = []
# for i in range(n):
#     a.append(int(sys.stdin.readline()))

# #산술평균
# print(round(sum(a)/n))      #round() => 반올림 하는 함수

# #중앙값
# print(sorted(a)[len(a)//2]) 

# #최빈값
# count = Counter(a)           #collection 모듈 사용 / Counter() -> 빈도수 구해주는 함수
#                              #딕셔너리 형태로 수와 빈도수가 저장된 배열
# order = count.most_common()  #튜플 형태로 수와 빈도수가 저장된 배열
# max_frequency = order[0][1]  #최대 빈도수

# fq = []                      #최대 빈도수를 가진 수들을 저장하는 리스트
# for i in order:
#     if i[1] == max_frequency: #i[1] => 각 수의 빈도수임. 이것이 최대 빈도수라면
#         fq.append(i[0])       #fq 리스트에 해당 숫자를 추가
        
# if len(fq) == 1:              #만약 최대빈도수를 가진 수가 1개라면
#     print(fq[0])              #첫번째 숫자 출력
# else:
#     print(sorted(fq)[1])      #1개가 아니라면 정렬 후 두번째 인덱스 출력

# #범위
# print(max(a)-min(a))


# print(count)
# print(order)





# ===========================
# 1st trial: 최빈값 for문이 너무 복잡해져서 도중에 포기

# import sys
# input = sys.stdin.readline

# allnumbers = []
# NumberFreq = []

# #-1~-4000, 0, 1~4000 모든 데에 채울 수 있음!

# FirstFreq = 1
# SecondFreq = 1
# answer3 = 0

# n = int(input())
# for i in range(n):
#     number = int(input())
#     allnumbers.append(number)
#     if number in NumberFreq:
#         NumberFreq.index(NumberFreq)[1] += 1
#     else:
#         NumberFreq.append([number, 1])

# #최빈값 구하기
# for i in range(-4001, 4000+1):
#     if NumberFreq[i][1] >= FirstFreq:
#         SecondFreq = FirstFreq
#         FirstFreq = NumberFreq[i][1]

# print('{:.0f}'.format(sum(allnumbers)/n))
# print(allnumbers[n//2])
# print(answer3) #-> 얘를 못 구해서.. for문...
# print(max(allnumbers)-min(allnumbers))