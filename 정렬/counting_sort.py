# 계수 정렬 연습
N = int(input())
lst = []
ans = []
for _ in range(N):
    lst.append(int(input()))
max_num = max(lst)

count_lst = [0] * (max_num+1)
for i in lst:
    count_lst[i] +=1
# 카운팅 리스트 만들기     
# print(count_lst)

for j in range(1,len(count_lst)):
    count_lst[j] += count_lst[j-1]
# 누적합 값
# print(lst)
# print(count_lst)

for k in range(len(count_lst)+1,-1,-1):
    # print(f"정렬할 수 {lst[k]}")
    count_lst[lst[k]] -=1
    ans[count_lst[lst[k]]] = lst[k]

# print(ans)
for p in ans:
    print(p)