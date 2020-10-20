# dfs, bfs 문제
from collections import deque

def dfs(graph,v,visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문 
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph, start,visited):
    # 큐로 설정
    q = deque([start])
    visited[start] = False
    while q:
        v = q.popleft()
        print(v,end=' ')
        graph[v].sort()
        # print(graph[v])
        for i in graph[v]:
            if visited[i]:
                q.append(i)
                visited[i] = False

n,m,v = map(int,input().split())

# 그래프를 n+1만큼 크기 생성
graph = [[] for _ in range(n+1)]
# print(graph)
# 입력 값 입력 받기
for _ in range(m):
    i,data = map(int,input().split())
    graph[i].append(data)
    graph[data].append(i)
# print(graph)
visited = [False] * (n+1)
dfs(graph,v,visited)
print()
bfs(graph,v,visited)

