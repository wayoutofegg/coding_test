import sys
input = sys.stdin.readline

s = input()
prev = s[0]
count_to_0 = 0
count_to_1 = 0

for i in range(1, len(s)):
    if s[i] == prev:
        continue
    else:
        prev = s[i]
        if s[i-1] == '0':
            count_to_1 += 1
        else:
            count_to_0 += 1
        
print(min(count_to_0, count_to_1))