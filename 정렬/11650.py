import sys
input = sys.stdin.readline
N = int(input())
ans_lst = []
for _ in range(N):
    ans_lst.append(list(map(int,input().split())))


# for i in range(N):
#     min_index = i
#     for j in range(i+1,N):
#         if ans_lst[min_index][1] > ans_lst[j][1]:
#             min_index = j
#     ans_lst[min_index], ans_lst[i] = ans_lst[i], ans_lst[min_index]



# for i in range(N):
#     min_index = i
#     for j in range(i+1,N):
#         if ans_lst[min_index][0] > ans_lst[j][0]:
#             min_index = j
#     ans_lst[min_index], ans_lst[i] = ans_lst[i], ans_lst[min_index]

# print(ans_lst)
ans_lst = sorted(ans_lst)
for k in range(N):
    print(ans_lst[k][0],ans_lst[k][1])
    