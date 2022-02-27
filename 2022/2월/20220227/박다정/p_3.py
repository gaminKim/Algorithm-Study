import sys
import collections

input = sys.stdin.readline

n = int(input().rstrip())
apple_count = int(input().rstrip())
apples = [[False for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(apple_count):
    x, y = map(int, input().rstrip().split(' '))
    apples[x][y] = True

l = int(input().rstrip())
snake_moves = collections.deque([input().rstrip().split(' ') for _ in range(l)])
current_direction = 4
snake = collections.deque([[1, 1]])
visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]


def change_direction_to_left():
    global current_direction

    if current_direction == 1:
        current_direction = 3
    elif current_direction == 2:
        current_direction = 4
    elif current_direction == 3:
        current_direction = 2
    elif current_direction == 4:
        current_direction = 1


def change_direction_to_right():
    global current_direction

    if current_direction == 1:
        current_direction = 4
    elif current_direction == 2:
        current_direction = 3
    elif current_direction == 3:
        current_direction = 1
    elif current_direction == 4:
        current_direction = 2


def change_direction(direction):
    if direction == 'L':
        change_direction_to_left()
    elif direction == 'D':
        change_direction_to_right()


def move():
    global current_direction
    current_x, current_y = snake[-1]

    if current_direction == 4:
        current_y += 1
    elif current_direction == 3:
        current_y -= 1
    elif current_direction == 2:
        current_x += 1
    elif current_direction == 1:
        current_x -= 1

    snake.append([current_x, current_y])


def is_out():
    head_x, head_y = snake[-1]

    if head_x == 0 or head_x == n + 1:
        return True
    if head_y == 0 or head_y == n + 1:
        return True
    return False


def collison_body():
    head_x, head_y = snake[-1]
    return visited[head_x][head_y]


def flag(x, y):
    visited[x][y] = True


def de_flag(x, y):
    visited[x][y] = False


def is_apple_cell():
    x, y = snake[-1]
    return apples[x][y]


for time in range(1, 10001):
    move()

    if is_out():
        print(time)
        break

    if collison_body():
        print(time)
        break

    flag(snake[-1][0], snake[-1][1])

    if not is_apple_cell():
        x, y = snake.popleft()
        de_flag(x, y)
    else:
        x, y = snake[-1]
        apples[x][y] = False

    if snake_moves:
        second, command = snake_moves[0]

        if int(second) == time:
            change_direction(command)
            snake_moves.popleft()
