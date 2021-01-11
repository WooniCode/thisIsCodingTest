# Q17. 경쟁적 전염
from collections import deque
n, k = map(int, input().split())
data = []
virus = []

for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] != 0:
            virus.append((data[i][j], 0, i, j))
input_s, input_x, input_y = map(int, input().split())
virus.sort()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    queue = deque()
    for i in virus:
        queue.append(i)

    while queue:
        v, time, x, y = queue.popleft()
        if input_s == time:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if data[nx][ny] == 0:
                    data[nx][ny] = data[x][y]
                    queue.append((v, time+1, nx, ny))

    print(data[input_x-1][input_y-1])

bfs()