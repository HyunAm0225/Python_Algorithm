# 리스트에 포함된 원소의 숫자를 세는 재귀 함수를 작성하기
def count_lst(lst):
    if lst == []:
        return 0
    else:
        print(f"count_lst({lst[:]}) = 1 + count_lst({lst[1:]})")
        return 1 + count_lst(lst[1:])

print(count_lst([1,2,3,4,1]))