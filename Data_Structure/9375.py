'''This Code was written to use in python environment'''

import sys
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    clothes = {}
    NumOfTypes = []
    ANSWER = 1
    N = int(read())

    for _ in range(N):
        name, kind = read().split()
        #type(): 데이터타입 확인하는 함수 -> kind로 대체
        if kind in clothes:
            clothes[kind].append(name)
        else:
            clothes[kind] = [name]

    # 벗는 경우의 수 고려 -> +1 (핵심!)
    for kind, name in clothes.items():
        ANSWER = ANSWER*(len(name)+1)

    print(ANSWER-1)
    # 일일이 체크하는 건 TOO MUCH TIME
    # K = len(NumOfTypes)
    # temp = [i for i in range(K+1)]
    # for i in range(1, len(NumOfTypes)+1):
    #     if i == 1:
    #         answer += sum(NumOfTypes)
    #     elif i == 2:
    #         for temp1 in range(0, K):
    #             for temp2 in range(temp1+1, K+1):
    #                 answer += NumOfTypes[temp1] * NumOfTypes[temp2]
    #     elif i == 3:
    #         for temp1 in range(0, K-1):
    #             for temp2 in range(temp1+1, K):
    #                 for temp3 in range(temp2+1, K+1):
    #                 answer += NumOfTypes[temp1] * NumOfTypes[temp2]
