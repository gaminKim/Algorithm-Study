import sys

input = sys.stdin.readline

n = int(input().rstrip())
default_top = [i for i in range(n + 1)]
result = []


def dfs(current, visited):
    if visited[current]:
        return current
    visited[current] = True
    return dfs(default_top[current], visited)


for i in range(n):
    default_top[i + 1] = int(input().rstrip())

for i in range(1, n + 1):
    visited = [False for _ in range(n + 1)]
    if i == dfs(i, visited):
        result.append(i)

print(len(result))

for number in result:
    print(number)
