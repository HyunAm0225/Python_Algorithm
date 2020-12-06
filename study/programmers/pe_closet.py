# 테스트 케이스
from collections import deque
n = 7
lost = [2, 3, 4]
reserve = [1, 2, 3, 6]

# 구현


def solution(n, lost, reserve):
    answer = n
    lost_count = 0
    lost.sort()
    reserve.sort()
    new_lost = list(set(lost)-(set(lost) & set(reserve)))
    new_reserve = list(set(reserve)-(set(lost) & set(reserve)))
    print(new_lost)
    print(new_reserve)
    for i in new_reserve:
        if i-1 in new_lost:
            new_lost.remove(i-1)
        elif i+1 in new_lost:
            new_lost.remove(i+1)
        else:
            continue
    return answer-len(new_lost)


print(solution(n, lost, reserve))
