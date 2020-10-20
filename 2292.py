# 백준
# 백준 수학 문제

def room_count(number):
    six_num = 1
    count = 1
    while number > six_num and number >1:
        six_num+=(6*count)
        count +=1
    # print(f"six_num : {six_num}")
    return count

n = int(input())
print(room_count(n))