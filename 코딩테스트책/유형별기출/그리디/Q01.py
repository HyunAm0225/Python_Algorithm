# 모험가 길드

# 모험가 수 입력받기
n = int(input())

x = list(map(int,input().split()))

x.sort()
# 결과값
result = 0
# 그룹에 포함된 모험가 카운트
count = 0

for i in x:
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:
        result +=1
        count = 0
    # print(f"모험가 {i} 일때 카운트 : {count} 결과 : {result} ")
print(result)

