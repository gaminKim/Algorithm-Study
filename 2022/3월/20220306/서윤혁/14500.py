import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":

    def dfs(r, c, depth, s):
        global ans

        if s + maxv * (4 - depth) <= ans:
            return

        if depth == 3:
            ans = max(ans, s)
            return
        else:
            for i in range(4):
                nx = r + dr[i]
                ny = c + dc[i]

                if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                    if depth == 1:
                        visit[nx][ny] = 1
                        dfs(r, c, depth + 1, s + board[nx][ny])
                    visit[nx][ny] = 1
                    dfs(nx, ny, depth + 1, s + board[nx][ny])
                    visit[nx][ny] = 0


    n, m = map(int, input().split())
    board = [[int(i) for i in input().split()] for _ in range(n)]
    visit = [([0] * m) for _ in range(n)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    maxv = max(map(max, board))

    ans = 0

    for i in range(n):
        for j in range(m):
            visit[i][j] = 1
            dfs(i, j, 0, board[i][j])
            visit[i][j] = 0

    print(ans)
