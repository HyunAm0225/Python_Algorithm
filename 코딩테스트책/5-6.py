# 인접 행렬 예제
import sys

max_num = sys.maxsize

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0,7,5],
    [7,0,max_num],
    [5,max_num,0]
]

print(graph)


