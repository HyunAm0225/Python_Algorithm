# 3진법으로 만드는 코드
def ternary(n):
    tern_list = []
    ans = ''
    while n > 0:
        # print(f"현재 n값 : {n}")
        tern_list.append(n%3)
        n //=3 
    tern_list.reverse()
    return tern_list

def solution(n):
    tern_list = ternary(n)
    ans = 0
    for i,num in enumerate(tern_list):
        num = num * (3**i)
        ans += num
    return ans

n = int(input())
    

print(solution(n))