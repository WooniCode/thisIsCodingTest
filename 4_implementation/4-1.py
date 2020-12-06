# 예제 4-1. 상하좌우

n = int(input())
p = input().split()

x, y = 1, 1
move_types = ['L', 'R', 'U', 'D']
x_move = [0, 0, -1, 1]
y_move = [-1, 1, 0, 0]

for i in p:
    for j in range(len(move_types)):
        if move_types[j] == i:
            x = min(max(x+x_move[j], 1), n)
            y = min(max(y+y_move[j], 1), n)
print(x, y)