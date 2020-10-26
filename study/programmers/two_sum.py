from itertools import permutations
data = list(map(int,input().split()))
new_data = [i for i in permutations(data,2)]
ans = []
for i in new_data:
    ans.append(sum(i))
print(sorted(list(set(ans))))
 