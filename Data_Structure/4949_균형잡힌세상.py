# 2023-07-31 Data Structure 12

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