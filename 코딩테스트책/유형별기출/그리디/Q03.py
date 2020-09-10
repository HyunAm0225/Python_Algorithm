# 문자열 뒤집기
# 백준 1439번 문제

data = input()

count0 = 0 # 전부 0으로 바꾸는것
count1 = 0 # 전부 1로 바꾸는 것


# 첫번 쨰 숫자에 대한 처리
if data[0] == '1':
    count0 +=1
else:
    count1 +=1
# 두 번쨰 원소로 부터 확인하면서 진행
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 +=1
        else:
            count1 +=1

print(min(count0,count1))