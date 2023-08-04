letters = input().rstrip()
suffixes = []

for i in range(len(letters)):
    suffixes.append(letters[i:])

suffixes = sorted(suffixes)
for suffix in suffixes:
    print(suffix)