total = int(input())
result = 0

for i in range(100000): #sqrt(4294967295) < 65536 < let 70000 (X)
                        #i*(i+1) > 2*4294967295
    if (i*i+i)/2 > total:
        print(i-1)
        break


# 이런 식으로 일일이 체크하면 시간초과 걸릴 거다
# while result <= total:
#     i += 1
#     result += i

# print(i-1)