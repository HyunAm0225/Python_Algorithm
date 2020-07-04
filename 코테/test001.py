def solution(name_list):
    N = len(name_list)
    for i in range(N):
        str = ""
        for p in range(N):
            if(p==i):
                continue
            str += name_list[p]
        if(str.find(name_list[i]) != -1):
            return True
    return False
    