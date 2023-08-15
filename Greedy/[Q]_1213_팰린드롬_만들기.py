#SUCCESS 3rd trial: FINAL TEST
#Q 이런 else는 처음 봐...
import sys
input = sys.stdin.readline

d = dict()
s = input().rstrip()

for i in s:
    if d.get(i) == None:
        d[i] = 1
    else:
        d[i] += 1

center = ''

for k, v in d.items():
    if v%2==1:
        if len(center) > 0:
            print("I'm Sorry Hansoo")
            break
        center = k
else: #Q 이런 else는 처음 보는데...
    ans = ''
    for k, v in sorted(d.items()):
        ans += k*(v//2)
    ans += center + ans[::-1]
    print(ans)

#SUCCESS 2nd trial: C+V
#출처: https://my-coding-notes.tistory.com/530
#1 dictionary 이해하기
#1-1 .get(key): key에 해당하는 value 얻음 
#1-2 .items(): (key, value) 쌍 얻음
# import sys
# input = sys.stdin.readline

# d = dict() #{문자: 해당 문자의 개수}
# s = input().rstrip()
# for i in s: #그냥 문자열도 in s로 활용 가능
#     if d.get(i) == None: #처음 입력되는 알파벳
#         d[i] = 1
#     else:
#         d[i] += 1
        
# center = ''
# for k,v in d.items():
#     if v % 2 == 1:
#         if len(center)>0: #이미 center가 있는데, 또 들어옴
#             print("I'm Sorry Hansoo")
#             break
#         center = k
# else: #대응되는 if가 없는데?
#     ans = ''
#     for k,v in sorted(d.items()): #dictionary 정렬하면 key순서대로 정렬
#         ans+=k*(v//2)
#     ans += center + ans[::-1]
#     print(ans)

#FAIL 1st trial: 나는 왜 이런 식으로 작성하다가 틀리는 걸까
# import sys
# sys = sys.stdin.readline
# name = list(input().rstrip())

# save = ''
# name = sorted(name)
# result = [name[0], name[1]]
# i = 2

# while i <= len(name)-1:
#     if i == len(name)-1:
#         if save == '':
#             save = name[i]
#             i+=1
#             break
#         else:
#             break
        
#     if name[i] == name[i+1]:
#         result.insert(i//2, name[i])
#         result.insert(i//2, name[i+1])
#         i+=2

#     else:
#         if save == '':
#             save = name[i]
#             i+=1
#         else:
#             break    

# if i == len(name):
#     result.insert(i//2, save)
#     for letter in result:
#         print(letter, end='')
# else:
#     print('\"I\'m Sorry Hansoo\"')
            