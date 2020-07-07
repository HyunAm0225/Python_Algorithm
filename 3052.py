ans_list = []
for _ in range(10):
    ans_list.append(int(input())%42)
print(len(set(ans_list)))