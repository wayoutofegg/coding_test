# 시간복잡도 낮추는 방법은 없을까
import sys
input = sys.stdin.readline

dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))

dwarfs = sorted(dwarfs)

for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if sum(dwarfs) - dwarfs[i] - dwarfs[j] == 100:
           dwarf1 = i
           dwarf2 = j
           break 

for i in range(9):
    if i == dwarf1 or i == dwarf2:
        continue
    else:
        print(dwarfs[i])