# 예제 4-3. 왕실의 나이트

input_val = input()
col = int(ord(input_val[0])) - int(ord('a')) + 1
row = int(input_val[1])

movX = [-2, -2, -1, -1, 1, 1, 2, 2]
movY = [1, -1, 2, -2, 2, -2, 1, -1]

count = 0

for i in range(8):
    if 0 < col + movX[i] < 9 and 0 < row + movY[i] < 9:
        count += 1

print(count)