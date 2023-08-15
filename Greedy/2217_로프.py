#0 아이디어: 고려하는 것들 중 가장 작은 줄의 감당 무게에 따라 전체 감당 무게가 결정된다
#1 모든 rope를 사용하지 않아도 된다. 이게 핵심이네
#2 여러 개라면 그냥 list에 싸그리 때려놓고 비교하면 빠를 수도 있다..!
#3 sort,min 최대한 자제할 것! 사용하는 순간 시간 초과 걸릴 위험 크게 상승한다.

# max_weight = 0
max_weight = []
rope = []
n = int(input())

for i in range(n):
    rope.append(int(input()))

rope = sorted(rope, reverse=True)

for i in range(n):
    # max_weight = max(max_weight, min(rope[i:])*(n-i))
    max_weight.append(rope[i]*(i+1))

print(max(max_weight))