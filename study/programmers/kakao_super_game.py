n = int(input())
stage = list(map(int,input().split()))

fail_per = []
clear_person = 0
fail_person = 0
for i in range(1,n+1):
    for j in stage:
        if j>=i:
            if j == i:
                fail_person +=1
                clear_person +=1
            else:
                clear_person +=1
    print(f"fail_person={fail_person},clear_person={clear_person}")
    if clear_person == 0:
        fail_per.append((i,0))
    else:    
        fail_per.append((i,fail_person/clear_person))
    fail_person = 0
    clear_person = 0

fail_per.sort(reverse=True, key = lambda x:x[1])
answer = [i[0] for i in fail_per]
print(answer)
