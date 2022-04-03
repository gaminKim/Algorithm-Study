import sys
import itertools
import collections

input = sys.stdin.readline

n, m = map(int, input().rstrip().split(' '))
board = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
cases = list(itertools.combinations([[i, j] for j in range(m) for i in range(n)], 3))
DELTA = ((-1, 0), (1, 0), (0, -1), (0, 1))
result = 0


def is_out(x, y):
    if x < 0 or y < 0:
        return True
    if x > n - 1 or y > m - 1:
        return True
    return False


def bfs(start, labs):
    queue = collections.deque(start)
    visited = [[False for _ in range(m)] for _ in range(n)]
    virus_count = len(start)

    for s in start:
        x, y = s
        visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for delta in DELTA:
            dx, dy = delta
            next_x, next_y = x + dx, y + dy

            if not is_out(next_x, next_y) and not visited[next_x][next_y] and labs[next_x][next_y] == 0:
                virus_count += 1
                visited[next_x][next_y] = True
                queue.append([next_x, next_y])
    return virus_count


def fill_to(locations, value):
    for location in locations:
        x, y = location
        board[x][y] = value


def find_start_virus():
    virus = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                virus.append([i, j])
    return virus


def copy_arr(arr):
    result = []
    for a in arr:
        result.append(a[:])
    return result


wall_count = 0
virus = find_start_virus()

for i in range(len(board)):
    wall_count += board[i].count(1)

for case in cases:
    only_space = True

    for i in range(len(case)):
        if board[case[i][0]][case[i][1]] != 0:
            only_space = False
            break

    if not only_space:
        continue

    fill_to(case, 1)
    start = copy_arr(virus)
    virus_count = bfs(start, board)

    result = max(result, n * m - virus_count - 3 - wall_count)

    fill_to(case, 0)

print(result)
