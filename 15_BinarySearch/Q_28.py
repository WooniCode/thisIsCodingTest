# Q28. 고정점 찾기
def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return -1

n = int(input())
array = list(map(int, input().split()))

print(binary_search(array, 0, n-1))