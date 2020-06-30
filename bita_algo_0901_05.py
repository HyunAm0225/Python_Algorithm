'''
문제 링크 : https://edu.goorm.io/learn/lecture/15551/%EC%9C%84%ED%81%B4%EB%A6%AC-%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%8B%9C%EC%A6%8C2-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%8C%80%EB%B9%84-%EC%9E%85%EB%AC%B8%ED%8E%B8/lesson/761935/09%EC%9B%94-2%EC%A3%BC%EC%B0%A8-%EC%8B%A0%EC%97%90%EA%B2%8C%EB%8A%94-%EC%95%84%EC%A7%81-12%EC%B2%99%EC%9D%98-%EB%B0%B0%EA%B0%80-%EC%9E%88%EC%82%AC%EC%98%B5%EB%8B%88%EB%8B%A4-2
'''
a = []
battle_line = []
# 공백으로 2차원 list 받기
for _ in range(11):
    line = []
    for _ in range(1):
        line = list(map(int,input().split()))
    a.append(line)
print("######################")
for i in range(11):
    for j in range(11):
        print(a[j][i],end=" ")
    print()
