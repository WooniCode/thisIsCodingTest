#Q22. 블록 이동하기
from collections import deque

input_board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
length = len(input_board)
board = [[1] * (length + 2) for _ in range(length + 2)]
for i in range(1, length + 1):
    for j in range(1, length + 1):
        board[i][j] = input_board[i-1][j-1]

def check_move(pos, board):
    next_pos = []
    pos = list(pos) # 튜플을 리스트로 변환
    pos1x, pos1y, pos2x, pos2y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(4): # 4방향 이동 체
        next_pos1x, next_pos1y, next_pos2x, next_pos2y = pos1x + dx[i], pos1y + dy[i], pos2x + dx[i], pos2y + dy[i]
        if board[next_pos1x][next_pos1y] == 0 and board[next_pos2x][next_pos2y] == 0:
            next_pos.append({(next_pos1x, next_pos1y), (next_pos2x, next_pos2y)})
    # 가로로 놓여있는 경우
    if pos1x == pos2x:
        for i in [-1, 1]:
            if board[pos1x+i][pos1y] == 0 and board[pos2x+i][pos2y] == 0:
                next_pos.append({(pos1x, pos1y), (pos1x + i, pos1y)})
                next_pos.append({(pos2x, pos2y), (pos2x + i, pos2y)})
    elif pos1y == pos2y:
        for i in [-1, 1]:
            if board[pos1x][pos1y+i] == 0 and board[pos2x][pos2y+i] == 0:
                next_pos.append({(pos1x, pos1y), (pos1x, pos1y + i)})
                next_pos.append({(pos2x, pos2y), (pos2x, pos2y + i)})
    return next_pos

def solution(board, length):
    robot = {(1, 1), (1, 2)}
    q = deque()
    visited = []
    q.append((robot, 0))  # 큐 삽입
    visited.append(robot)  # 방문처리
    while q:
        pos, cost = q.popleft()
        if (length, length) in pos:
            return cost
        for next_pos in check_move(pos, board):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)
    return 0

print(solution(board, length))