# Q19. 연산자 끼워 넣기
from itertools import permutations

def calculate(val1, val2, cal):
    if cal == 0:
        return val1 + val2
    if cal == 1:
        return val1 - val2
    if cal == 2:
        return val1 * val2
    if cal == 3:
        return val1 // val2

n = int(input())
number_list = list(map(int, input().split()))
input_cal_list = list(map(int, input().split()))
cal_list = []

for i in range(4):
    for j in range(input_cal_list[i]):
        cal_list.append(i)

max_value = -1e9
min_value = 1e9


for num in list(permutations(number_list, len(number_list))):
    for cal in list(permutations(cal_list, len(cal_list))):
        value = num[0]
        for i in range(len(cal)):
            value = calculate(value, num[i+1], cal[i])
        max_value = max(value, max_value)
        min_value = min(value, min_value)

print(max_value)
print(min_value)