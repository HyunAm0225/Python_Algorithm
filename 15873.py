N = str(input())

if int(N[len(N)-2:len(N)]) == 10:
    last_num = int(N[len(N)-2:len(N)])
    first_num = int(N[:len(N)-2])
else:        
    last_num = int(N[-1])
    first_num = int(N[:len(N)-1])

print(last_num + first_num)

