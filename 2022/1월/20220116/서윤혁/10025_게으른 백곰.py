import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ice = [0] * 1000002
li = [list(map(int, input().split())) for _ in range(n)]
my = 0
for x, y in li:
    my = max(my, y)
    ice[y] = x

i = 1
if k * 2 > my:
    print(sum(ice[:]))
else:
    j = 1 + 2 * k
    s = sum(ice[i:j+1])
    answer = s
    while j < my:
        j += 1
        i += 1
        s += ice[j]
        s -= ice[i-1]
        answer = max(answer, s)

    print(answer)