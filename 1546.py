N = int(input())
num_list = sorted(list(map(int, input().split())))
best_num = num_list[-1]
ans = sum([i/best_num*100 for i in num_list])/N
print(ans)
