import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n, m, x, y, k = map(int, input().split())
    board = [[int(i) for i in input().split()] for _ in range(n)]
    order = list(map(int, input().split()))

    row_deq = deque([0, 0, 0, 0])
    column_deq = deque([0, 0, 0, 0])

    row_deq[3] = board[x][y]
    column_deq[3] = board[x][y]

    for i in range(k):
        direct = order[i]

        if direct == 1:
            #row_right
            if 0 <= x <= n - 1 and 0 <= y + 1 <= m - 1:
                y += 1
                row_deq.rotate(1)
                column_deq[1] = row_deq[1]
                column_deq[3] = row_deq[3]
                print(row_deq[1])
                if board[x][y] == 0:
                    board[x][y] = column_deq[-1]
                else:
                    column_deq[-1] = board[x][y]
                    row_deq[-1] = board[x][y]
                    board[x][y] = 0
        elif direct == 2:
            #row_left
            if 0 <= x <= n - 1 and 0 <= y - 1 <= m - 1:
                y -= 1
                row_deq.rotate(-1)
                column_deq[1] = row_deq[1]
                column_deq[3] = row_deq[3]
                print(row_deq[1])
                if board[x][y] == 0:
                    board[x][y] = column_deq[-1]
                else:
                    column_deq[-1] = board[x][y]
                    row_deq[-1] = board[x][y]
                    board[x][y] = 0
        elif direct == 3:
            #column_up
            if 0 <= x - 1 <= n - 1 and 0 <= y <= m - 1:
                x -= 1
                column_deq.rotate(-1)
                row_deq[1] = column_deq[1]
                row_deq[3] = column_deq[3]
                print(row_deq[1])
                if board[x][y] == 0:
                    board[x][y] = column_deq[-1]
                else:
                    column_deq[-1] = board[x][y]
                    row_deq[-1] = board[x][y]
                    board[x][y] = 0
        elif direct == 4:
            #column_down
            if 0 <= x + 1 <= n - 1 and 0 <= y <= m - 1:
                x += 1
                column_deq.rotate(1)
                row_deq[1] = column_deq[1]
                row_deq[3] = column_deq[3]
                print(row_deq[1])
                if board[x][y] == 0:
                    board[x][y] = column_deq[-1]
                else:
                    column_deq[-1] = board[x][y]
                    row_deq[-1] = board[x][y]
                    board[x][y] = 0
