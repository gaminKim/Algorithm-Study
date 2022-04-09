import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, h = map(int, input().split())
a, b = [], []
for _ in range(n//2):
    a.append(int(input()))
    b.append(h - int(input()))
a = sorted(a)
b = sorted(b)

cnt = 0
mn = sys.maxsize
for i in range(h):
    i += 0.5
    t1 = bisect_left(a, i)
    t2 = bisect_right(b, i)
    
    k = (n // 2 - t1 + t2)

    if k == mn:
        cnt += 1
    elif mn > k:
        cnt = 1
        mn = k
        
print(mn, cnt)