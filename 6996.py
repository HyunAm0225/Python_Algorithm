N = int(input())
ans_lst = []
for _ in range(N):
    a,b = map(str,input().split())
    if ''.join(sorted(a)) == ''.join(sorted(b)):
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")