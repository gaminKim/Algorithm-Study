import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

n = int(input().rstrip())
m = int(input().rstrip())

costs = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
result = [INF for _ in range(n + 1)]
path = [i for i in range(n + 1)]
result_path = []

for _ in range(m):
    start, end, cost = map(int, input().rstrip().split(' '))

    if costs[start][end] < cost:
        continue

    costs[start][end] = cost

start, end = map(int, input().rstrip().split(' '))

tmp = [start]


def bfs(start):
    queue = [[0, (start, 0)]]
    visited = [False for _ in range(n + 1)]
    result[start] = 0
    while queue:
        _, info = heapq.heappop(queue)
        current, current_cost = info
        visited[current] = True
        for i in range(1, n + 1):
            if visited[i] or i == current or costs[current][i] == INF:
                continue

            if result[i] > costs[current][i] + current_cost:
                result[i] = current_cost + costs[current][i]
                path[i] = current
                heapq.heappush(queue, (result[i], [i, result[i]]))
                path[i] = current


bfs(start)
current = end

while current != start:
    result_path.append(current)
    current = path[current]

result_path.append(start)

print(result[end])
print(len(result_path))
print(*result_path[::-1])
