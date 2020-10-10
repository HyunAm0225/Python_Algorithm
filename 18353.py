# 병사 배치하기 문제
n = int(input())
data = list(map(int,input().split()))
data.reverse()

dp = [1] * 2000 # dp로 저장될 크기 최대 2000
# print(data)
for i in range(1,n):
    for j in range(0,i):
        if data[j]<data[i]:
            dp[i] = max(dp[i],dp[j] + 1)

# for i in range(n):
#     print(dp[i],end=" ")
# print()

print(n-max(dp))

