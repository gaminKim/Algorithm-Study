import sys
import collections

input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split(' '))
board = [list(input().rstrip()) for _ in range(n)]
DELTA = ((-1, 0), (0, -1), (0, 1), (1, 0))
visited = [[[0 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]


def bfs():
    queue = collections.deque([[0, 0, k]])
    visited[0][0][k] = 1

    while queue:
        x, y, count = queue.popleft()

        if x == n - 1 and y == m - 1:
            print(visited[x][y][count])
            return

        for delta in DELTA:
            dx, dy = delta
            next_x, next_y = x + dx, y + dy

            if next_x < 0 or next_x > n - 1 or next_y > m - 1 or next_y < 0:
                continue

            if not visited[next_x][next_y][count]:
                if board[next_x][next_y] == '0':
                    if not visited[next_x][next_y][k]:
                        visited[next_x][next_y][count] = visited[x][y][count] + 1
                        queue.append([next_x, next_y, count])
                elif board[next_x][next_y] == '1' and count > 0:
                    if not visited[next_x][next_y][count - 1]:
                        visited[next_x][next_y][count - 1] = visited[x][y][count] + 1
                        queue.append([next_x, next_y, count - 1])
    print(-1)


bfs()
