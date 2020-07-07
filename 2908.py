N = list(map(str,input().split()))
print(f"{N[0][::-1] if int(N[0][::-1])>int(N[1][::-1]) else int(N[1][::-1])}")