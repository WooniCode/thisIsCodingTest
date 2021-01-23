# Q24. 안테나
n = int(input())
array = list(map(int, input().split()))
array.sort()

print(array[n//2 - 1])