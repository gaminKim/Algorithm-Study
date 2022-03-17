import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split(' '))
paths = [list(map(int, input().rstrip().split(' '))) for _ in range(m)]
paths.sort(key=lambda x: x[2])
length = n - 2
table = [i for i in range(n + 1)]
result = 0


def find(child):
    if child == table[child]:
        return child
    return find(table[child])


for path in paths:

    if length == 0:
        break

    start, end, cost = path
    start_parent = find(start)
    end_parent = find(end)

    if start_parent == end_parent:
        continue

    if start_parent < end_parent:
        table[end_parent] = start_parent
    else:
        table[start_parent] = end_parent

    result += cost
    length -= 1

print(result)
