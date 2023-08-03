import sys
input = sys.stdin.readline
n = int(input())
answer= []
words = []
for i in range(n):
    word = input().rstrip()
    if word not in words:
        words.append(word)
        answer.append([word, len(word)])
        
answer = sorted(answer, key=lambda a:a[0])
answer = sorted(answer, key=lambda a:a[1])

# print('========================================')
for i in range(len(answer)):
    print(answer[i][0])

# print('\n'.join(map(str, answer[i][0]) for i in range(len(answer))))
# 왜 이렇게 정렬하면 안 돌아가는가?

# set을 활용하면 더 효율적으로 코드 작성 가능!