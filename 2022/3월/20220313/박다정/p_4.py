import sys
import heapq

input = sys.stdin.readline

n = int(input())
queue = []
result = []

for _ in range(n):
    current = int(input().rstrip())

    if len(queue) == 0 and current == 0:
        result.append(0)
        continue

    if current == 0:
        result.append(heapq.heappop(queue))
    else:
        heapq.heappush(queue, current)

print('\n'.join(map(str, result)))
