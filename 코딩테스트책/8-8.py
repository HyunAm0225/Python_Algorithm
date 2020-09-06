# DP문제
# 효율적인 화폐 구성

n,m = map(int,input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

# 한 번 계산된 결과를 저장하기 위해 DP 테이블을 초기화 합니다.
d = [100001] * (m+1)
# 다이나믹 프로그래밍 보텀업
for i in range(n):
    for j in range(coin[i],m+1):
        if d[j-array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j],d[j-array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없을 경우
    print(-1)
else:
    print(d[m])


