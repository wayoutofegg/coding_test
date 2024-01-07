# 2024-01-07 FAIL
#     말렸어. 이따가 다시 확인하자

import sys
input = sys.stdin.readline

answer = "no"

def AnswerMe(sentence):    
    brackets = []
    open_brackets = []
    for letter in sentence:
        if letter in '([])':
            brackets.append(letter)
            
    for bracket in brackets:
        if bracket in '[(':
            open_brackets.append(bracket)
        else:
            if open_brackets and bracket == ']':
                if open_brackets[-1] == '[':
                    open_brackets.pop()
            elif open_brackets and bracket == ')':
                if open_brackets[-1] == '(':
                    open_brackets.pop()
            else:
                return "no"
                
    if not open_brackets:
        return "yes"
    return "no"
        
while True:
    sentence = input().rstrip()
    if sentence == '.':
        break
    else:
        sentence = list(sentence)
        print(AnswerMe(sentence))



# 2023-07-31 Data Structure 14

import sys
input = sys.stdin.readline
YesOrNo = []

while True:
    Sentence = input().rstrip()
    if Sentence == '.':
        break
    else:
        Sentence = list(Sentence)
        Brackets = []
        for Letter in Sentence:
            if Letter in '[(':
                Brackets.append(Letter)
            elif Letter == ']':
                if Brackets and Brackets[-1] == '[': 
                    # )]부터 들어오면 Bracket out of range, empty 조건 추가
                    # and에서 앞만 false면 뒤 조건 확인 안 하고 그냥 넘어감
                    Brackets.pop()
                else:
                    YesOrNo.append('no')
                    Brackets.append('NoAppendedAlready')
                    break
            elif Letter == ')':
                if Brackets and Brackets[-1] == '(':
                    Brackets.pop()
                else:
                    YesOrNo.append('no')
                    Brackets.append('NoAppendedAlready')
                    break
            else: continue
    
    if 'NoAppendedAlready' not in Brackets: #이 test case 때문에 3번 틀림 ㅠㅠ
        if len(Brackets) == 0:
            YesOrNo.append('yes')
        else:
            YesOrNo.append('no')

print('\n'.join(YesOrNo[:]))
