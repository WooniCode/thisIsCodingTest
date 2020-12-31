# Q03. 문자열 뒤집기
s = str(input())
first = s[0]
sum0 = 0
sum1 = 0
if first == '0':
    sum1 = 1
else:
    sum0 = 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            sum0 += 1
        else:
            sum1 += 1

print(min(sum0, sum1))