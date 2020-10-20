# dfs 안보고 구현하기
# dfs는 재귀적으로 동작한다

def dfs(graph,v,visited): # 입력할 그래프, 시작점, 방문된 확인
    # 현재 노드를 방문 처리한다
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문 
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

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
# graph = [[], [2, 3, 4], [4], [4], []]
# print(len(graph)-1)
visited = [False] * len(graph)

dfs(graph,1,visited)