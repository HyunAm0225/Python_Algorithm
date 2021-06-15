n = 10


def solution(n):
    dp = [True] * (n+1)
    m = int(n**0.5)+1
    for i in range(2, m+1):
        if dp[i] == True:
            for j in range(i+i, n+1, i):
                dp[j] = False
    return len([i for i in range(2, n+1) if dp[i] == True])


print(solution(10))
