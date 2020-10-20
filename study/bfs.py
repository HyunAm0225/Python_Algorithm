# bfs 구현하기
# bfs는 반복을 이용해서 문제를 해결합니다.
from collections import deque

def bfs(graph,start,visited):
    q = deque([start])
    # 현재 노드 방문 처리하기
    visited[start] = True
    # 큐가 빌 때까지 반복 
    while q:
        # 큐에서 하나의 원소를 뽑아 출력
        v = q.popleft()
        print(v,end=' ')
        # 해당 원소와 연결된 ,아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
graph = [
    [],
    [2,3,8], # node 1번 연결된 간선
    [1,7],  # node 2번 연결된 간선
    [1,4,5],    # node 3번 연결된 간선
    [3,5],  # node 4번 연결된 간선
    [3,4],  # node 5번 연결된 간선
    [7], #node 6번에 연결된 간선   
    [2,6,8], # node 7번에 연결된 간선
    [1,7] # node 8번에 연결된 간선
]
# print(len(graph)-1)
# graph = [[], [2, 3, 4], [4], [4], []]
visited = [False] * len(graph)
bfs(graph,1,visited)
