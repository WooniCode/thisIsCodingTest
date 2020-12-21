# 7-1. 순차 탐색

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1 # 현재의 위치 변환

input_data = input().split()
n = int(input_data[0]) # 원소의 개수
target = input_data[1]
array = input().split()

print(sequential_search(n, target, array))