s = "1234"
def solution(s):
    answer = True
    for i in s:
        if ord(i)>57 or ord(i)<48:
            answer = False
    return answer

print(solution(s))

# def solution(d,budget):
#     answer = 0
#     test = []
#     for i in range(2**len(d)):
#         flag = bin(i)[2:].zfill(len(d))
#         subset = [d[j] for j in range(len(d)) if flag[j] == '1']
#         test.append(subset)
#     for x in test:
#         if sum(x)== budget:
#             if answer<len(x):
#                 answer = len(x)
#     return answer
