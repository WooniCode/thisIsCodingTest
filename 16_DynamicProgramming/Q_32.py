# Q32. 정수 삼각형
n = int(input())
dp = [[-1e9] * n for i in range(n)]

for i in range(n):
    array = list(map(int, input().split()))
    for j in range(len(array)):
        dp[i][j] = array[j]

for i in range(n):
    for j in range(n):
        if j == 0:
            dp[i][j] = dp[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j-1] + dp[i][j]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]) + dp[i][j]

result = 0
for i in range(n):
    result = max(result, dp[i][n-1])

print(result)