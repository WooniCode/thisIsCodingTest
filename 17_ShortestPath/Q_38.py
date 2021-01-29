# Q38. 정확한 순위
n, m = map(int, input().split())
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    graph[a][a] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

total = 0

# 수행된 결과 출력
for a in range(1, n+1):
    cnt = 0
    for b in range(1, n+1):
        if 0 < graph[a][b] < INF or 0 < graph[b][a] < INF:
            cnt += 1
    if cnt == n - 1:
        total += 1

print(total)