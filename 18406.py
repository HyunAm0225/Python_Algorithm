N = str(input())
num_list = []
if len(N)%2 ==0:
    for i in N:
        num_list.append(int(i))
    half = int(len(num_list)/2)
    if sum(num_list[:half]) == sum(num_list[half:]):
        print("LUCKY")
    else:
        print("READY")
