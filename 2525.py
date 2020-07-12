h,m = map(int,input().split())
time = int(input())

# print(h, m+time)
if h+(m+time)//60 < 24:
    print(h+(m+time)//60, (m+time)%60)
else:
    print(h+(m+time)//60-24,(m+time)%60)