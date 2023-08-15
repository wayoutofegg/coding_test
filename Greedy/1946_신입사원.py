#0 아이디어: 
#출처: https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-1946-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%8B%A0%EC%9E%85-%EC%82%AC%EC%9B%90-%EC%8B%A4%EB%B2%841-%EA%B7%B8%EB%A6%AC%EB%94%94

#1 input보다 sys.stdin.readline 써야 시간초과가 되지 않는다!

import sys
input = sys.stdin.readline

testcase = int(input())

for eachcase in range(testcase):
    n = int(input())
    result = []
    for i in range(n):
        result.append(list(map(int, input().split())))

    #서류 성적 우수한 순으로 정렬
    result = sorted(result, key=lambda a:a[0]) 

    top = 0
    success = 1 #서류 1위
    
    #면접 우수한 사람 count(서류 1위 제외)
    for i in range(1,n):
        if  result[i][1] < result[top][1]: #여기가 핵심
            top = i #면접 순위
            success += 1
        #i 증가: 서류는 부족하더라도 (i=서류 등수)
        #result[top][1]은 감소: 면접은 우수한 학생 선발하겠다
    
    print(success)
