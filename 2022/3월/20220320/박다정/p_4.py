import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split(' '))
employees = list(map(int, input().rstrip().split(' ')))
compliments = [list(map(int, input().rstrip().split(' '))) for _ in range(m)]
result = [0 for _ in range(n)]
table = [[] for _ in range(n)]
visited = [False for _ in range(n)]
queue = collections.deque([0])

for i in range(len(employees)):
    if i == 0:
        continue
    table[employees[i] - 1].append(i)

for compliment in compliments:
    start, value = compliment
    result[start - 1] += value

visited[0] = True

while queue:
    current = queue.popleft()

    for i in table[current]:
        if not visited[i]:
            visited[i] = True
            result[i] += result[employees[i] - 1]
            queue.append(i)

print(*result)
