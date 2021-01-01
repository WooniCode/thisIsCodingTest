# Q06. 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야하므로 우선순위 큐 적용
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 시간
    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x:x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]

food_times = list(map(int, input().split()))
k = int(input())
print(solution(food_times, k))