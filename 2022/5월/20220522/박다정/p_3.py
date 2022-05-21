import sys

input = sys.stdin.readline

n = int(input().rstrip())

utility_pole = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
utility_pole.sort()

table = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if utility_pole[i][1] > utility_pole[j][1]:
            table[i] = max(table[i], table[j] + 1)

print(n - max(table))
