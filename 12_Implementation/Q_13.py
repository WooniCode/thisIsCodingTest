# Q13. 치킨 배달
from itertools import combinations

n, m = map(int, input().split())
chicken_map = []
home_list = []
chicken_list = []

for _ in range(n):
    chicken_map.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if chicken_map[i][j] == 1:
            home_list.append((i, j))
        elif chicken_map[i][j] == 2:
            chicken_list.append((i, j))

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken_list, m))

def calculate(candidate):
    result = 0
    for i in home_list:
        min_distance = 1e9
        for j in candidate:
            distance = abs(i[0] - j[0]) + abs(i[1] - j[1])
            min_distance = min(distance, min_distance)
        result += min_distance
    return result

def solution(candidates):
    answer = 1e9
    for i in candidates:
        answer = min(answer, calculate(i))
    print(answer)

solution(candidates)