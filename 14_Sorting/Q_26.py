# Q26. 카드 정렬하기
import heapq

# array로 풀기
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
count = 0

for i in range(len(array) - 1):
    array.sort()
    count += array[0] + array[1]
    array[0] = array[0] + array[1]
    array[1] = 1e9

print(count)

# heapq로 풀기
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))
result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)