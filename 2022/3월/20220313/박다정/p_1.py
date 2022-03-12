import heapq
import sys

input = sys.stdin.readline
dic = {}
n = int(input().rstrip())
result = []
queue = []

for _ in range(n):
    current = int(input().rstrip())
    current_abs = abs(current)

    if len(queue) == 0 and current == 0:
        result.append(0)
    elif current == 0:
        key = heapq.heappop(queue)
        result.append(heapq.heappop(dic[key]))
    elif current != 0:
        heapq.heappush(queue, current_abs)

        if current_abs not in dic:
            dic[current_abs] = [current]
        else:
            heapq.heappush(dic[current_abs], current)

print('\n'.join(map(str, result)))
