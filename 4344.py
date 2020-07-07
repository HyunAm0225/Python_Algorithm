N = int(input())
ans_list = []
for _ in range(N):
    T = list(map(int,input().split()))
    first_num = T.pop(0)
    ans_list.append(len([i for i in T if i>(sum(T)/first_num)])/first_num)
for i in ans_list:
    print(f'{format(i,"10.3%").strip()}')
