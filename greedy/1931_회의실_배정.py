#1 lambda 사용법 익숙해지기, 저게 key 사용하는 거라는 거 이해하기!
#2 왜 정렬이 꼭 이 순서여야할까...

n = int(input())
meetings = [[0,0] for _ in range(n)]
end = 0
count = 0

for i in range(n):
    meetings[i][0], meetings[i][1] = map(int, input().split())

#[1,4] -> [3,5] -> [0,6]

meetings = sorted(meetings, key = lambda a: a[0])
#[0,6] -> [1,4] -> [3,5]

meetings = sorted(meetings, key=lambda a: a[1])
#[1,4] -> [3,5] -> [4,5] -> [0,6] 

for i, j in meetings:
    if i >= end:
        end = j
        count += 1

print(count)

# --------------------------------------------------------

# 출처: https://jokerldg.github.io/algorithm/2021/03/11/meeting-room.html
#1 lambda 함수 = 함수 한 줄 쓰기 cf. (lambda x,y: x+y)(10, 20)
#2 다차원 배열의 정렬, 기준으로 삼고 싶은 걸 key로 설정하고 sort(key= '기준')

#제출 코드
# N = int(input())
# time = []

# for _ in range(N):
#   start, end = map(int, input().split())
#   time.append([start, end])

# time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
# # print('T1')
# # print(time)

# time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순
# # print('T2')
# # print(time)

#정렬하고 나면, 결과적으로 빨리 시작해서 빨리 끝나는 거가 제일 앞으로 감
#순서의 중요성: [4,5] -> [2,6] -> [1,7] 되어야 함


# last = 0 # 회의의 마지막 시간을 저장할 변수
# conut = 0 # 회의 개수를 저장할 변수

# for i, j in time:
#   if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
#     conut += 1
#     last = j

# print(conut)

# 시도하다가 실패한 코드
# n = int(input())
# meetings = [[0,0] for _ in range(n)]
# schedule = [0]*(2**31-1)
# start = 2**31-1
# end = 0

# for i in range(n):
#     meetings[i][0], meetings[i][1] = map(int, input().split())
#     start = meetings[i][0] if start > meetings[i][0] else start
#     end = meetings[i][1] if end < meetings[i][1] else end

# for i in range(n):
    