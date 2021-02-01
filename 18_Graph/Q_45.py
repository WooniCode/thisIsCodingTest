# Q45. 최종 순위
from collections import deque

# 테스트 회수만큼 반복
for tc in range(int(input())):
    # 노드의 개수 입력 받기
    v = int(input())

    # 모든 노드에 대한 진입차수를 0으로 초기
    indegree = [0] * (v + 1)

    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
    graph = [[False] * (v + 1) for i in range(v + 1)]

    # 등수 입력
    data = list(map(int, input().split()))

    # 방향 그래프의 모든 간선 정보를 입력받기
    for i in range(v):
        for j in range(i + 1, v):
            graph[data[i]][data[j]] = True
            # 진입 차수 1 증가
            indegree[data[j]] += 1

    # 올해 변경된 순위
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1


    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True # 위상 정렬 결과가 오직 하나인지 여부
    cycle = False # 그래프 내 사이클이 존재하는지 여부

    for i in range(v):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break
        now = q.popleft()
        result.append(now)

        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for j in range(1, v + 1):
            if graph[now][j]:
                indegree[j] -= 1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[j] == 0:
                    q.append(j)
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end= ' ')
        print()