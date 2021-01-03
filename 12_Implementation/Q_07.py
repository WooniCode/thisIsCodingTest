# Q07. 럭키 스트레이트
n = input()
sum = 0
half = 0
result = 'READY'
for i in range(len(n)):
    sum += int(n[i])

for i in range(len(n)):
    half += int(n[i])
    if sum/2 == half:
        result = 'LUCKY'

print(result)