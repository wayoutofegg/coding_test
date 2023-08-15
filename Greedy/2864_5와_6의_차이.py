a, b = map(int, input().split())
maxA = 0; maxB=0
minA = 0; minB=0
i = 0; j = 0

while a != 0:
    if a%10 == 5:
        maxA += 6*10**i
        minA += (a%10)*10**i
    elif a%10 == 6:
        minA += 5*10**i
        maxA += (a%10)*10**i
    else:
        maxA += (a%10)*10**i
        minA += (a%10)*10**i
    a = a//10
    i += 1

while b != 0:
    if b%10 == 5:
        maxB += 6*10**j
        minB += (b%10)*10**j
    elif b%10 == 6:
        minB += 5*10**j
        maxB += (b%10)*10**j
    else:
        maxB += (b%10)*10**j
        minB += (b%10)*10**j
    b = b//10
    j += 1

print(minA+minB, maxA+maxB)