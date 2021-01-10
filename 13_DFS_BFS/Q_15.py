# Q15. 특정 거리의 도시 찾기
from collections import deque
n, m, k, x = map(int, input().split()) # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
graph = [[] for _ in range(n+1)]
for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [-1] * (n + 1)
dist[x] = 0

def bfs(x, k):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append(x)

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if dist[i] == -1:
                dist[i] = dist[x] + 1
                queue.append(i)

    count = 0
    for i in range(1, n + 1):
        if dist[i] == k:
            print(i)
            count += 1
    if count == 0:
        print(-1)

bfs(x, k)