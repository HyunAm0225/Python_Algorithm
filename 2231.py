N = int(input())
for i in range(N):
    if N == i + sum([int(i) for i in str(i)]):
        print(i)
        break
    else:
        if N-1 == i:
            print(0)