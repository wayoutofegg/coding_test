scores = dict()
for i in range(1, 8+1):
    scores[i] = int(input())

# print(scores)
scores = dict(sorted(scores.items(), reverse=True, key=lambda a:a[1]))
#dict로 감싸야 list가 아닌 dict 형태로 저장됨
# print(scores)

#짧게 간단히 작성하는 방법 고민
i=0; tot=0
for index, score in scores.items():
    if i == 5:
        break
    i += 1    
    tot += score
print(tot)

i=0; answers=[]
for index, score in scores.items():
    if i == 5:
        break
    i+=1
    answers.append(index)

print(' '.join(map(str, sorted(answers))))