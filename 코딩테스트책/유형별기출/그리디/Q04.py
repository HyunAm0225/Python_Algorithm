# 만들 수 없는 금액
# 그리디 문제
n = int(input())
data = list(map(int,input().split()))
data.sort()

target = 1
for i in data:
    if target < i:
        break
    print(f"i가 {i}일때 target은 {target}")
    target+=i
print(target)