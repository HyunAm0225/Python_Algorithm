A = int(input())
B = int(input())
C = int(input())
result = A*B*C
num_list = []
count_list = [0 for _ in range(10)]
# print(count_list)
for i in str(result):
    num_list.append(int(i))
for j in num_list:
    count_list[j] += 1
for k in count_list:
    print(k)
