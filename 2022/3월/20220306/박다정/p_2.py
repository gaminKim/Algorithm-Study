import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split(' '))
board = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
answer = 0

one_default_horizontal_shape = [[0, 1], [0, 2]]
one_default_vertical_shape = [[1, 0], [2, 0]]

two_default_horizontal_shape = [[0, 1]]
two_default_vertical_shape = [[1, 0]]


def get_default_shape_score(x, y, default):
    result = board[x][y]
    for location in default:
        dx, dy = location
        next_x, next_y = x + dx, y + dy

        if is_out(next_x, next_y):
            return 0
        result += board[next_x][next_y]
    return result


def find_one_horizontal_shape(x, y):
    current = get_default_shape_score(x, y, one_default_horizontal_shape)
    max_value = current

    if not is_out(x - 1, y):
        max_value = max(max_value, current + board[x - 1][y])

    if not is_out(x + 1, y):
        max_value = max(max_value, current + board[x + 1][y])

    if not is_out(x - 1, y + 1):
        max_value = max(max_value, current + board[x - 1][y + 1])

    if not is_out(x + 1, y + 1):
        max_value = max(max_value, current + board[x + 1][y + 1])

    if not is_out(x - 1, y + 2):
        max_value = max(max_value, current + board[x - 1][y + 2])

    if not is_out(x + 1, y + 2):
        max_value = max(max_value, current + board[x + 1][y + 2])

    if not is_out(x, y + 3):
        max_value = max(max_value, current + board[x][y + 3])
    return max_value


def find_one_vertical_shape(x, y):
    current = get_default_shape_score(x, y, one_default_vertical_shape)
    max_value = current

    if not is_out(x, y - 1):
        max_value = max(max_value, current + board[x][y - 1])

    if not is_out(x, y + 1):
        max_value = max(max_value, current + board[x][y + 1])

    if not is_out(x + 1, y - 1):
        max_value = max(max_value, current + board[x + 1][y - 1])

    if not is_out(x + 1, y + 1):
        max_value = max(max_value, current + board[x + 1][y + 1])

    if not is_out(x + 2, y - 1):
        max_value = max(max_value, current + board[x + 2][y - 1])

    if not is_out(x + 2, y + 1):
        max_value = max(max_value, current + board[x + 2][y + 1])

    if not is_out(x + 3, y):
        max_value = max(max_value, current + board[x + 3][y])

    return max_value


def find_two_horizontal_shape(x, y):
    current = get_default_shape_score(x, y, two_default_horizontal_shape)
    max_value = current

    if not is_out(x + 1, y + 1) and not is_out(x + 1, y + 2):
        max_value = max(max_value, current + board[x + 1][y + 1] + board[x + 1][y + 2])

    if not is_out(x - 1, y + 1) and not is_out(x - 1, y + 2):
        max_value = max(max_value, current + board[x - 1][y + 1] + board[x - 1][y + 2])

    return max_value


def find_two_vertical_shape(x, y):
    current = get_default_shape_score(x, y, two_default_vertical_shape)
    max_value = current

    if not is_out(x + 1, y - 1) and not is_out(x + 2, y - 1):
        max_value = max(max_value, current + board[x + 1][y - 1] + board[x + 2][y - 1])

    if not is_out(x + 1, y + 1) and not is_out(x + 2, y + 1):
        max_value = max(max_value, current + board[x + 1][y + 1] + board[x + 2][y + 1])

    return max_value


def find_two_default(x, y):
    current = get_default_shape_score(x, y, two_default_horizontal_shape)
    max_value = current

    if not is_out(x + 1, y) and not is_out(x + 1, y + 1):
        max_value = max(max_value, current + board[x + 1][y] + board[x + 1][y + 1])

    return max_value

# 현재 위치가 경계를 벗어났는지 확인
def is_out(x, y):
    if x < 0 or x > n - 1:
        return True
    if y < 0 or y > m - 1:
        return True
    return False


for i in range(n):
    for j in range(m):
        # 길이 3의 막대에 하나의 블럭을 붙여서 테트로미노를 만들기
        answer = max(answer, find_one_horizontal_shape(i, j))
        answer = max(answer, find_one_vertical_shape(i, j))
        answer = max(answer, find_two_default(i, j))
        answer = max(answer, find_two_horizontal_shape(i, j))
        answer = max(answer, find_two_vertical_shape(i, j))

print(answer)
