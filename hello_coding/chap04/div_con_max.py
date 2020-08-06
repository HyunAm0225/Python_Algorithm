# 리스트에서 가장 큰 수를 찾으시오

def lst_max(lst):
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    else:
        sub_max = lst_max(lst[1:])
        return lst[0] if lst[0] > sub_max else sub_max

print(lst_max([1,2,3,4,5]))