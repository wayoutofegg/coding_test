# 과거 코드 수정
d = []

for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

for i in range(19):
    a = input().split()
    for j in range(19):
        d[i+1][j+1] = int(a[j])

n = int(input())
for i in range(n) :
    x, y = input().split()
    x = int(x) #row index
    y = int(y) #column index
    
    #이전 코드
    # for j in range(1, 20): #중복으로 바꾸지 않으면 순서는 상관 없음
        #else 끝나고 아래줄을 안 보고 다음 루프를 돈다 -> column flip만 count
        # if d[j][y] == 0:
        #     d[j][y] = 1
        # else:
        #     d[j][y] = 0
        # if d[x][j] == 0:
        #     d[x][j] = 1
        # else:
        #     d[x][j] = 0

    #수정 코드
    for j in range(1, 20):
        if d[j][y] == 0:
            d[j][y] = 1
        else:
            d[j][y] = 0

    for j in range(1, 20):
        if d[x][j] == 0:
            d[x][j] = 1
        else:
            d[x][j] = 0

for j in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end = ' ')
    print()