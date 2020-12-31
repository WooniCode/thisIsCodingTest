# 예제 3-3. 숫자 카드 게임

# N, M을 공백으로 구분해 입력받기
n, m = map(int, input().split())

maxNum = 0

for i in range(n):
    data = list(map(int, input().split()))
    maxNum = max(maxNum, min(data))

print(maxNum)