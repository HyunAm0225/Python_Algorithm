# acm 호텔
# 구현, 수학, 사칙연산

# 테스트 케이스 입력을 받는다
t = int(input())
ans = []
for _ in range(t):
    # h 높이, w 호의 개수, n 번째 손님
    h,w,n = map(int,input().split())
    # h=w=n일때 처리
    if n%h==0:
        ans.append(100*h+(n//h))
    else:
        ans.append(100*(n%h)+(n//h)+1)

# 정답 출력
for i in ans:
    print(i)


# 주의 해야할 테스트 케이스
# 10 10 10
# 10 10 11
# 1 1 1
# 99 99 9801
# 6 12 18