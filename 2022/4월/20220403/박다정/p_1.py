import sys

input = sys.stdin.readline

n = int(input().rstrip())
schedules = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
table = [0 for _ in range(n + 1)]
current_max_profit = 0
for i in range(len(schedules)):
    day, profit = schedules[i]

    if i + day <= n:
        table[i + day] = max(table[i + day], table[i] + profit, current_max_profit + profit)
        current_max_profit = max(current_max_profit, table[i])

print(table)
print(max(table))
