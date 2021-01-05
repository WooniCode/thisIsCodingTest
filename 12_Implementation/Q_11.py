# Q11. 뱀
n = int(input())
k = int(input())
board = [[0] * (n+1) for _ in range(n+1)]

for i in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1 # 보드 판에 사과 채워넣기

l = int(input())
rotate = []

for i in range(l):
    c, d = input().split()
    rotate.append((int(c), d))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def solution():
    x, y = 1, 1 # 뱀의 머리 위치
    board[x][y] = 2 # 뱀이 존재하는 위치는 2로 세팅
    direction = 0 # 처음에는 오른쪽을 바라봄
    time = 0
    index = 0 # 다음에 회전할 정보
    q = [(x,y)] # 뱀이 차지하고 있는 위치 정보
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 맵 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx][ny] != 2:
            # 사과가 없을 경우
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
            elif board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        time += 1
        x,y = nx, ny
        if index < l and time == rotate[index][0]:
            direction = turn(direction, rotate[index][0])
            index += 1
        if index == l:
            break
    return time

print(solution())