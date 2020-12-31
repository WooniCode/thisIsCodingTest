# Q05. 볼링공 고르기
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
count = 0

for i in data:
    for j in data:
        if i != j:
            count += 1

print(count//2)