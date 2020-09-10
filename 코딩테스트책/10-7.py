# 팀결성 문제
# 서로소 집합 자료구조를 이용하여 구한다

def find_parent(parent,x):
    if parent[x] !=x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
parent = [0] * (n+1) # 부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(0,n+1):
    parent[i] = i

# 각 연산을 하나씩 확인
for i in range(m):
    oper,a,b = map(int,input().split())
    # 합집합 (union)
    if oper ==0:
        union_parent(parent,a,b)
    # 찾기(find) 연산 일 경우
    elif oper == 1:
        if find_parent(parent,a) == find_parent(parent,b):
            print("YES")
        else:
            print("NO")