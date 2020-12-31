# Q02. 곱하기 혹은 더하기
s = str(input())
result = 0
for i in s:
    i = int(i)
    if i == 0 or i == 1:
        result += i
    elif i == 2 and result < 2:
        result += i
    elif result == 0:
        result = i
    else:
        result *= i

print(result)