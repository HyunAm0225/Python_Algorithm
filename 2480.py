x,y,z = map(int,input().split())
max_num = max(x,y,z)
if x == y and y == z:
    print(10000+x*1000)
elif x == y and y !=z:
    print(1000+x*100)
elif x!=y and y==z:
    print(1000+y*100)
elif x == z and z!=y:
    print(1000+z*100)
else:
    print(max_num*100)