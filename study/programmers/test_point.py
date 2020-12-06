# from collections import deque
answers = [1, 2, 3, 4, 2, 1, 2, 3, 4, 2, 5, 5, 5]


def solution(answers):
    length = len(answers)
    personA = [1, 2, 3, 4, 5]
    personB = [2, 1, 2, 3, 2, 4, 2, 5]
    personC = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a_point = 0
    b_point = 0
    c_point = 0
    for i in range(length):
        if answers[i] == personA[i % len(personA)]:
            a_point += 1
        if answers[i] == personB[i % len(personB)]:
            b_point += 1
        if answers[i] == personC[i % len(personC)]:
            c_point += 1
    data = []
    max_point = max(a_point, b_point, c_point)
    if max_point == a_point:
        data.append(1)
    if max_point == b_point:
        data.append(2)
    if max_point == c_point:
        data.append(3)
    return data


print(solution(answers))
