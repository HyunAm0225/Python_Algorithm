def sum(lst):
    if lst == []:
        return 0
    else:
        print(f"sum({lst[:]}) = {lst[0]} + sum({lst[1:]})")
        return lst[0] + sum(lst[1:])

print(sum([1,2,3,4,5]))