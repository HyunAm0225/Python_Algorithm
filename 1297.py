x, y, z = map(int,input().split())

h = (x**2 * (y**2/(y**2 + z**2))) ** 0.5

print(int(h),int(h*(z/y)))