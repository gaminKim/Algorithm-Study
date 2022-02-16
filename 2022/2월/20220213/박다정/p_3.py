import sys
import itertools

input = sys.stdin.readline

n = int(input().rstrip())
board = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
cases = list(itertools.combinations([i for i in range(n)], n // 2))
answer = sys.maxsize

for start in cases:
    link = []
    for i in range(n):
        if i not in start:
            link.append(i)

    start_stat = 0
    link_stat = 0

    for i in start:
        for j in start:
            if i == j:
                continue
            start_stat += board[i][j]

    for i in link:
        for j in link:
            if i == j:
                continue
            link_stat += board[i][j]

    answer = min(answer, abs(start_stat - link_stat))

print(answer)
