moneys = [500, 100, 50, 10, 5, 1]
howmany = 0
temp = int(input())
payment = 1000-temp

for money in moneys:
    if money > payment:
        continue
    else:
        howmany += payment//money
        payment = payment%money

print(howmany)