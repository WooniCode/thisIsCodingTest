# 예제 3-2. 큰 수의 법칙

# n, m, k를 공백으로 구분해 입력받기
n, m, k = map(int, input().split())
# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n-1]
second = data[n-2]

result = 0
cnt = 0

for i in range(m):
    if cnt == k:
        cnt = 0
        result += second
    else:
        cnt += 1
        result += first

print(result)