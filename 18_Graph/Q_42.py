# Q42. 탑승구
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 가진 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 도크 수와 비행기 수 입력 받기
g = int(input())
p = int(input())

parent = [0] * (g + 1) # 부모 테이블 초기화

result = 0

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, g + 1):
    parent[i] = i

# union 연산을 각각 수행
for _ in range(p):
    data = find_parent(parent, int(input()))
    if(data == 0):
        break
    union_parent(parent, data, data - 1)
    result += 1

print(result)