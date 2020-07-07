from collections import Counter

N = str(input()).upper()

count = Counter(N)

if len(count)==1:
    print(max(N,key=count.get))
else:
    if count.most_common(2)[0][1]==count.most_common(2)[1][1]:
        print("?")  
    else:
        print(max(N,key=count.get))
