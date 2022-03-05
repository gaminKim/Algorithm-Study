import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().rstrip().split(' '))
board = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
command = list(map(int, input().rstrip().split(' ')))

EAST = 1
NORTH = 3
SOUTH = 4
WEST = 2

deltas = {
    EAST: (0, 1),
    WEST: (0, -1),
    NORTH: (-1, 0),
    SOUTH: (1, 0)
}

dice = [0 for _ in range(6)]
current = {}

current['top'] = 0
current['east'] = 1
current['west'] = 2
current['north'] = 3
current['south'] = 4
current['bottom'] = 5


def set_dice(tile_number, i, j):
    if tile_number == 0:
        board[i][j] = dice[current['bottom']]
    else:
        dice[current['bottom']] = board[i][j]
        board[i][j] = 0


def move_north():
    # top -> north -> bottom -> south -> top
    tmp1 = current['top']
    tmp2 = current['north']
    tmp3 = current['bottom']
    tmp4 = current['south']

    current['top'] = tmp4
    current['north'] = tmp1
    current['bottom'] = tmp2
    current['south'] = tmp3


def move_east():
    # top -> east -> bottom -> west -> top
    tmp1 = current['top']
    tmp2 = current['east']
    tmp3 = current['bottom']
    tmp4 = current['west']

    current['top'] = tmp4
    current['east'] = tmp1
    current['bottom'] = tmp2
    current['west'] = tmp3


def move_south():
    # top -> south -> bottom -> north -> top
    tmp1 = current['top']
    tmp2 = current['south']
    tmp3 = current['bottom']
    tmp4 = current['north']

    current['top'] = tmp4
    current['south'] = tmp1
    current['bottom'] = tmp2
    current['north'] = tmp3


def move_west():
    # top -> west -> bottom -> east -> top
    tmp1 = current['top']
    tmp2 = current['west']
    tmp3 = current['bottom']
    tmp4 = current['east']

    current['top'] = tmp4
    current['west'] = tmp1
    current['bottom'] = tmp2
    current['east'] = tmp3


for i in range(len(command)):
    dx, dy = deltas[command[i]]

    if -1 < x + dx < n and -1 < y + dy < m:
        x += dx
        y += dy

        if command[i] == NORTH:
            move_north()
        if command[i] == SOUTH:
            move_south()
        if command[i] == WEST:
            move_west()
        if command[i] == EAST:
            move_east()
        set_dice(board[x][y], x, y)
        print(dice[current['top']])
