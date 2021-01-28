# Q35. 못생긴 수
n = int(input())
array = []

for i in range(50):
    for j in range(30):
        for k in range(20):
            number = (2 ** i) * (3 ** j) * (5 ** k)
            array.append(number)
array.sort()

print(array[n-1])