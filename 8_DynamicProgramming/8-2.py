# 8-2 피보나치 함수를 탑다운 다이나믹 프로그래밍으로 구현
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(10))