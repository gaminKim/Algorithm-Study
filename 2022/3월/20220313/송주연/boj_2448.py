# 백준 별찍기 11

import sys

N = int(sys.stdin.readline())
depth = N//3

arr = [[' ' for _ in range(5*depth + depth-1)] for _ in range(N)]


def divide(point, r_len):
    if r_len == 3:
        draw(point)
        return
    r, c = point

    r_len //= 2
    c_len = (5 * r_len // 3 + (r_len // 3 - 1)) // 2


    divide(point, r_len)
    divide([r + r_len, c - c_len - 1], r_len)
    divide([r + r_len, c + c_len + 1], r_len)


def draw(point):
    r, c = point
    arr[r][c] = '*'
    arr[r+1][c+1] = '*'
    arr[r + 1][c - 1] = '*'

    for i in range(5):
        arr[r+2][c-2+i] = '*'

    return

divide([0, len(arr[0])//2], N)

for i in range(N):
    for j in range(5*depth + depth - 1):
        print(arr[i][j], end='')
    print()


# python 시간초과
# 참고