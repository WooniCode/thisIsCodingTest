# Q27. 정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left, bisect_right
n, x = map(int, input().split())
array = list(map(int, input().split()))

def count(array, left_val, right_val):
    right_index = bisect_right(array, right_val)
    left_index = bisect_left(array, left_val)
    return right_index - left_index

count = count(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)