# Q20. 감시 피하기
from itertools import combinations

n = int(input())
map = []
teacher_list = []
student_list = []
empty_list = []
result = 'NO'

for i in range(n):
    map.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if map[i][j] == 'T':
            teacher_list.append((i, j))
        elif map[i][j] == 'S':
            student_list.append((i, j))
        else:
            empty_list.append((i, j))

candidates = list(combinations(empty_list, 3))

def check(x, y, direction):
    if direction == 0: # 왼쪽 체크
        while y >= 0:
            if map[x][y] == 'S':
                return True
            if map[x][y] == 'O':
                return False
            y -= 1
    if direction == 1: # 오른쪽 체
        while y < n:
            if map[x][y] == 'S':
                return True
            if map[x][y] == 'O':
                return False
            y += 1
    if direction == 2: # 위쪽 체크
        while x >= 0:
            if map[x][y] == 'S':
                return True
            if map[x][y] == 'O':
                return False
            x -= 1
    if direction == 3: # 아래쪽 체크
        while x < n:
            if map[x][y] == 'S':
                return True
            if map[x][y] == 'O':
                return False
            x += 1
    return False


def simulate():
    for teacher in teacher_list:
        tx = teacher[0]
        ty = teacher[1]
        for i in range(4):
            if check(tx, ty, i):
                return False
    return True

for block_list in candidates:
    for block in block_list:
        map[block[0]][block[1]] = 'O'
    if simulate():
        result = 'YES'
        break
    for block in block_list:
        map[block[0]][block[1]] = 'X'

print(result)