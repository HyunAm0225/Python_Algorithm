cro = ["c=","c-","dz=","d-","lj","lj","nj","s=","z="]

test = str(input())
count = 0
for i in cro:
    if i in test:
        count += test.count(i)
        test = test.replace(i," ")
# print(test)
test = test.replace(" ","")
print(count+len(test))