import sys
import collections

input = sys.stdin.readline

n, m = map(int, input().rstrip().split(' '))
iceberg = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
locations = collections.deque([])
DELTA = ((-1, 0), (1, 0), (0, -1), (0, 1))

for i in range(n):
    for j in range(m):
        if iceberg[i][j] > 0:
            locations.append([i, j])


def warm():
    count_with_ice = collections.deque([])
    for i in range(len(locations)):
        current_x, current_y = locations[i]
        count = 0
        for delta in DELTA:
            dx, dy = delta
            next_x, next_y = current_x + dx, current_y + dy

            if iceberg[next_x][next_y] == 0:
                count += 1

        count_with_ice.append([current_x, current_y, count])

    return count_with_ice


def check(start, visited):
    queue = collections.deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()

        for delta in DELTA:
            dx, dy = delta
            next_x, next_y = x + dx, y + dy

            if iceberg[next_x][next_y] == 0 or visited[next_x][next_y]:
                continue
            visited[next_x][next_y] = True
            queue.append([next_x, next_y])


def clean(result):
    while result:
        x, y, count = result.popleft()
        i_x, i_y = locations.popleft()

        if iceberg[x][y] > count:
            iceberg[x][y] -= count
            locations.append([i_x, i_y])
        else:
            iceberg[x][y] = 0


for year in range(1, 10000):
    result = warm()
    clean(result)
    count = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    for location in locations:
        x, y = location
        if not visited[x][y]:
            count += 1
            check(location, visited)

    if count > 1:
        print(year)
        break
    elif len(locations) == 0:
        print(0)
        break
