# 조합 문제 참고용

from itertools import permutations

data = [6,10,2]
new_data = [str(i) for i in data]

ans_list = list(map(''.join,permutations(new_data,len(new_data))))
# print(ans_list)
ans_list.sort()
print(int(ans_list.pop()))