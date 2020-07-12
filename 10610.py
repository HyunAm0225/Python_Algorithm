''' 메모리 초과 오류
from itertools import permutations

N = str(input())
num_lst = []
ans_lst = []
result = 0
for i in N:
    num_lst.append(int(i))

permu = list(permutations(num_lst,len(num_lst)))
# print(permu)


for i in permu:
    test = ""
    for j in range(len(N)):
        test += str(i[j])
    if int(test) % 30 == 0:
        ans_lst.append(int(test))
    else:
        ans_lst.append(-1)

ans_lst = sorted(ans_lst)
result = ans_lst.pop(-1)
print(result)
        
'''

N = input()
lst = list(map(int,N))
_sum = sum(lst)

if _sum%3==0:
    lst.sort(reverse=True)
    end_num = lst[-1]
    if end_num ==0:
        a = ''.join(map(str,lst))
        a = int(a)
        print(a)
    else:
        print(-1)
else:
    print(-1)