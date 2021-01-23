# Q25. 실패율
n = int(input())
stages = list(map(int, input().split()))
length = len(stages)
answer = []
for i in range(1, n + 1):
    count = stages.count(i)
    if length == 0:
        fail = 0
    else:
        fail = count / length

    answer.append((i, fail))
    length -= count

answer.sort(key=lambda x: x[1], reverse=True)

for i in answer:
    print(i[0])