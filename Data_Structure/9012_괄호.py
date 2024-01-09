# 2024-01-09 PASS
#     더 어려운 버전이 앞에 있었음. 그거 풀고 오니까 쉽네 

import sys
input = sys.stdin.readline

N = int(input())
answers = []

def VerifyBrackets(brackets):
    open_brackets = []
    for bracket in brackets:
            if bracket == '(':
                open_brackets.append(bracket)
            else:
                if open_brackets and open_brackets[-1] == '(':
                    open_brackets.pop()
                else: return "NO"
    if len(open_brackets) == 0: return "YES"
    else: return "NO"
    
for i in range(N):
    brackets = []
    brackets = list(input().rstrip())
    answers.append(VerifyBrackets(brackets))
    
print('\n'.join(answers))

# 20230730 Data Structure 01
#1 stack 사용법 익숙해지기
# import sys
# input = sys.stdin.readline

# n = int(input())
# ps = []

# for i in range(n):
#     ps.append(list(input().rstrip()))
#     check = []
#     for j in range(len(ps[i])):
#         if ps[i][j] == '(':
#             check.append(ps[i][j])
#         else: #if ps[i][j] == ')':
#             if '(' in check:
#                 check.pop()
#             else:
#                 check.append(ps[i][j]) #if에서 출력되지 않도록!
#                 print('NO')
#                 break
#                 # exit() #프로그램 종료라 다음 input을 못 받음
#     if len(check) == 0: print('YES')
#     elif len(check) > 0 and '(' in check: print('NO')
#     else: continue #len(check)>0 and ')' in check, printed NO already
