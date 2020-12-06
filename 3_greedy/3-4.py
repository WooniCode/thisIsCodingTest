# 예제 3-4. 1이 될때까지

# n, k 공백으로 입력받기
n, k = map(int, input().split())
cnt = 0

if k > n:
    cnt = n-1
else:
    while n > 1:
        if n % k == 0:
            n = n//k
            cnt += 1
        else:
            n = n-1
            cnt += 1
print(cnt)