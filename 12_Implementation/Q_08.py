# Q08. 문자열 재정렬
n = input()
str = []
sum = 0

for i in range(len(n)):
    if n[i].isdecimal():
        sum += int(n[i])
    else:
        str.append(n[i])

str.sort()
for i in str:
    print(i, end='')
print(sum)