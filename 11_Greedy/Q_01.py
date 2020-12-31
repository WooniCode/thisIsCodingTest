# Q01. 모험가 길드
n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)
result = 0
sum = 0
fear = 0

for i in data:
    if fear == 0:
        fear = i
    sum += 1
    if fear == sum:
        result += 1
        sum = 0
        fear = 0

print(result)