N = int(input())
ans_list = []
def solution(a):
    sum_count = 1
    ans = 0
    for i in a:
        if i == "O":
            ans += sum_count
            sum_count += 1
        else:
            sum_count = 1
    return ans
for _ in range(N):
    T = str(input())
    ans_list.append(solution(T))
for j in ans_list:
    print(j)