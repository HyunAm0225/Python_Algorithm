# def solution(v):
#     answer = []
#     answer.append(v[0][0]^v[1][0]^v[2][0])
#     answer.append(v[0][1]^v[1][1]^v[2][1])
#     return answer

# v = [
#     [1,4],
#     [3,4],
#     [3,10]
# ]
# print(solution(v))

l = [1, 5, 2, 6, 3, 7, 4]

v = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

for i in range(len(v)):
    # print(v[i][0],v[i][1],v[i][2])
    print(l[v[i][0]-1:v[i][1]])

