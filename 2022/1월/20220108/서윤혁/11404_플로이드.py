import sys

input = sys.stdin.readline
INF = 1e9

n = int(input())
m = int(input())

city = [[INF] * n for _ in range(n)]

for i in range(n):
    city[i][i] = 0

for _ in range(m):
    i, j, cost = map(int, input().split())
    i -= 1
    j -= 1
    city[i][j] = min(cost, city[i][j])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if city[i][k] + city[k][j] < city[i][j]:
                city[i][j] = city[i][k] + city[k][j]

for x in city:
    for i in range(n):
        if x[i] == INF:
            x[i] = 0
    print(' '.join(map(str, x)))