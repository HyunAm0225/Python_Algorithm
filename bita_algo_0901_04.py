'''
문제 링크 : https://edu.goorm.io/learn/lecture/15551/%EC%9C%84%ED%81%B4%EB%A6%AC-%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%8B%9C%EC%A6%8C2-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%8C%80%EB%B9%84-%EC%9E%85%EB%AC%B8%ED%8E%B8/lesson/761937/09%EC%9B%94-2%EC%A3%BC%EC%B0%A8-%EC%95%A0%ED%8B%8B%ED%95%9C-%EC%B9%9C%EA%B5%AC-1
'''
a = []
# 구할만큼 길이
n = int(input())

# 공백으로 2차원 list 받기
for i in range(n):
    line = []
    for j in range(1):
        line = list(map(int,input().split()))
    a.append(line)

maxdist = 0
ans1 = 0
ans2 = 0

# 두점사이 길이를 구하는 함수
def dist(i,j):
    # print("(a[{}][0] - a[{}][0])**2 + (a[{}][1] - a[{}][1])**2".format(i,j,i,j))
    return ((a[i][0] - a[j][0])**2 + (a[i][1] - a[j][1])**2)

for k in range(n):
    for l in range(n-k-1):
        # print("[{},{}]={}".format(k,l+k+1,dist(k,l+k+1)))
        d = dist(k,l+k+1)
        # print(f"ans : {ans1},{ans2}, maxdist = {maxdist}, d = {d}")
        if(maxdist<d):
            maxdist =  d
            ans1 = k+1
            ans2 = l+k+1+1
print(ans1, ans2)
