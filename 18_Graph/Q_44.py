# Q44. 행성 터널
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수 입력 받기
v = int(input())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
planet = []
edges = []
result = 0

# 부모 테이블에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 행성에 대한 정보를 입력받기
for _ in range(v):
    planet.append(list(map(int, input().split())))

for i in range(v):
    for j in range(v):
        min_length = min(abs(planet[i][0] - planet[j][0]), abs(planet[i][1] - planet[j][1]), abs(planet[i][2] - planet[j][2]))
        edges.append((min_length, i, j))

# 간선을 비용 순으로 정렬
edges.sort()

# 간선을 하나씩 확인하여
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)