import sys
import heapq

input = sys.stdin.readline
dic = {}
n = int(input().rstrip())
max_day = 0
result = 0

for _ in range(n):
    cost, day = map(int, input().rstrip().split(' '))
    max_day = max(max_day, day)
    if day not in dic:
        dic[day] = [-cost]
    else:
        heapq.heappush(dic[day], -cost)

tmp = []
keys = list(dic.keys())
keys.sort()

for i in range(len(keys) - 1):
    count = keys[i]
    while count > 0 and dic[keys[i]]:
        cost = heapq.heappop(dic[keys[i]])
        heapq.heappush(dic[keys[i + 1]], cost)
        count -= 1

count = keys[-1]
result = 0

while count > 0 and dic[keys[-1]]:
    result += heapq.heappop(dic[keys[-1]])
    count -= 1
print(-result)
