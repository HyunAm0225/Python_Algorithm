N = int(input())
ans_lst = []
for i in range(N):
    ans_lst.append(list(str(input()).split()))
    lst_len = len(ans_lst[i])
    # print(lst_len)
    for j in range(0,lst_len):
        # print(f"{ans_lst[i][j]}={ans_lst[i][j][::-1]}")
        ans_lst[i][j] = ans_lst[i][j][::-1]

    for p in range(0,lst_len):    
        print(ans_lst[i][p],end=" ")

    print()