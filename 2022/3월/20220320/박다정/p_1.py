import sys

input = sys.stdin.readline


def main(n, limit, items):
    table = [[0 for _ in range(limit + 1)] for _ in range(n)]

    for i in range(n):

        for j in range(limit + 1):

            w, v = items[i]

            if j < w:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(table[i - 1][j], table[i - 1][j - w] + v)

    print(table[n - 1][limit])


if __name__ == '__main__':
    n, k = map(int, input().rstrip().split(' '))
    items = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
    main(n, k, items)
