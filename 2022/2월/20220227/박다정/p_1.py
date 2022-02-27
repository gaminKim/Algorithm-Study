import sys

input = sys.stdin.readline

MAX_COUNT = 10
result = -1
height, width = map(int, input().rstrip().split(' '))
board = [list(input().rstrip()) for _ in range(height)]
goal_location = None
red_location = None
blue_location = None

for i in range(height):
    for j in range(width):
        if board[i][j] == 'R':
            red_location = [i, j]
        elif board[i][j] == 'B':
            blue_location = [i, j]
        elif board[i][j] == 'O':
            goal_location = [i, j]


# 빨간 구슬과 파란 구슬의 위치 비교해서 누가 먼저 움직일지 결정
def which_move(direction, r_location, b_location):
    if direction == 1:
        if r_location[0] < b_location[0]:
            return 'R'
        return 'B'
    elif direction == 2:
        if r_location[0] < b_location[0]:
            return 'B'
        return 'R'
    elif direction == 3:
        if r_location[1] < b_location[1]:
            return 'R'
        return 'B'
    else:
        if r_location[1] < b_location[1]:
            return 'B'
        return 'R'


def move(direction, r_location, b_location):
    first = which_move(direction, r_location, b_location)
    if first == 'B':
        slant_to(b_location, direction, r_location)
        slant_to(r_location, direction, b_location)
    else:
        slant_to(r_location, direction, b_location)
        slant_to(b_location, direction, r_location)
    return [r_location, b_location]


# board와 red, blue 위치 동기화


# 파라미터 이름 수정 할 것
def slant_to(location, direction, other):
    current_x, current_y = location
    # board에 벽 위치 체크
    # 다른 구슬 위치 체크
    if direction == 1:
        for row in range(current_x - 1, 0, -1):
            if board[row][current_y] == '#':
                current_x = row + 1
                break
            if row == goal_location[0] and current_y == goal_location[1]:
                current_x = row
                break
            if row == other[0] and current_y == other[1]:
                current_x = row + 1
                break
            current_x = row
        location[0] = current_x
    elif direction == 2:
        for row in range(current_x + 1, height - 1):
            if board[row][current_y] == '#':
                current_x = row - 1
                break
            if row == goal_location[0] and current_y == goal_location[1]:
                current_x = row
                break
            if row == other[0] and current_y == other[1]:
                current_x = row - 1
                break
            current_x = row
        location[0] = current_x

    elif direction == 3:
        for column in range(current_y - 1, 0, -1):
            if board[current_x][column] == '#':
                current_y = column + 1
                break
            if current_x == goal_location[0] and column == goal_location[1]:
                current_y = column
                break
            if current_x == other[0] and column == other[1]:
                current_y = column + 1
                break
            current_y = column
        location[1] = current_y
    else:
        for column in range(current_y + 1, width - 1):
            if board[current_x][column] == '#':
                current_y = column - 1
                break
            if current_x == goal_location[0] and column == goal_location[1]:
                current_y = column
                break
            if current_x == other[0] and column == other[1]:
                current_y = column - 1
                break
            current_y = column
        location[1] = current_y


def is_goal_location(location):
    global result
    if location[0] == goal_location[0] and location[1] == goal_location[1]:
        return True
    # if r_location[0] == goal_location[0] and r_location[1] == goal_location[1]:
    #     return True
    return False


def change_result(current):
    global result
    if result == -1:
        result = current
    else:
        result = min(result, current)


def dfs(current, r_location, b_location):
    global result

    if current >= MAX_COUNT + 1:
        return

    for i in range(1, 5):
        next_r_location, next_b_location = move(i, r_location[:], b_location[:])

        if is_goal_location(next_b_location):
            continue
        if is_goal_location(next_r_location):
            change_result(current)
        dfs(current + 1, next_r_location, next_b_location)


dfs(1, red_location, blue_location)
print(result)
