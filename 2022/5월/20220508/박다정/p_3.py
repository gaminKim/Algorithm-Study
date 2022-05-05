import sys
import collections

input = sys.stdin.readline
INF = sys.maxsize
DELTAS = ((-1, 0), (1, 0), (0, -1), (0, 1))
m, n = map(int, input().rstrip().split(' '))
board = [list(map(int, list(input().rstrip()))) for _ in range(n)]
table = [[INF for _ in range(m)] for _ in range(n)]
table[0][0] = 0


def bfs():
    queue = collections.deque([[0, 0]])

    while queue:
        x, y = queue.popleft()

        for delta in DELTAS:
            dx, dy = delta
            next_x, next_y = x + dx, y + dy

            if next_x < 0 or next_y < 0 or next_x > n - 1 or next_y > m - 1:
                continue

            if table[x][y] + 1 > table[next_x][next_y]:
                continue

            if board[next_x][next_y] and table[x][y] + 1 < table[next_x][next_y]:
                table[next_x][next_y] = table[x][y] + 1
                queue.append([next_x, next_y])
            elif not board[next_x][next_y] and table[x][y] < table[next_x][next_y]:
                table[next_x][next_y] = table[x][y]
                queue.append([next_x, next_y])


bfs()
print(table[-1][-1])
