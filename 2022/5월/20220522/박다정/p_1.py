import sys

input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().rstrip().split(' '))
paths = [list(map(int, input().rstrip().split(' '))) for _ in range(m)]
costs = [INF for _ in range(n)]


def bellman(start):
    costs[start - 1] = 0

    for i in range(n):
        for j in range(m):
            current_bus, next_bus, cost = paths[j]

            if paths[next_bus - 1][0] == INF:
                continue

            if costs[next_bus - 1] > costs[current_bus - 1] + cost:
                costs[next_bus - 1] = costs[current_bus - 1] + cost

                if i == n - 1:
                    return True
    return False


if bellman(1):
    print(-1)
    sys.exit(0)

for bus in range(2, n):
    if costs[bus - 1] == INF:
        print(-1)
    else:
        print(costs[bus - 1])
