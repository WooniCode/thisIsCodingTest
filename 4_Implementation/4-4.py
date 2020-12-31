# 예제 4-4. 게임 개발
n, m = map(int, input().split())
xLoc, yLoc, dirc = map(int, input().split())

move_map = []

for i in range(n):
    move_map.append(list(map(int, input().split())))

move_log = [[0] * m for _ in range(n)]

movX = [-1, 0, 1, 0]
movY = [0, 1, 0, -1]

count = 1
turn_time = 0

def turn_dirc():
    global dirc
    dirc -= 1
    if dirc == -1:
        dirc = 3

while True:
    turn_dirc()
    nx = xLoc + movX[dirc]
    ny = yLoc + movY[dirc]

    if move_map[nx][ny] == 0 and move_log[nx][ny] == 0:
        move_log[nx][ny] = 1
        xLoc = nx
        yLoc = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = xLoc - movX[dirc]
        ny = yLoc = movY[dirc]

        if move_map[nx][ny] == 0:
            xLoc = nx
            yLoc = ny
        else:
            break

print(count)