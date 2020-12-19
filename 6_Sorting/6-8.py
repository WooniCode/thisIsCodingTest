# 6-8. 두 배열의 원소 교체
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if b[i] > a[i]:
        a[i] = b[i]
    else:
        break

print(sum(a))