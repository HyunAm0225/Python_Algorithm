'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
선택정렬 예제
'''
T = int(input())
x = []
for _ in range(T):
    x.append(int(input()))
# print(x)

for i in range(T):
    min_index = i
    for j in range(i+1,T):
        if x[min_index]>x[j]:
            min_index = j
    x[i],x[min_index] = x[min_index], x[i]

for j in x:
    print(j)

