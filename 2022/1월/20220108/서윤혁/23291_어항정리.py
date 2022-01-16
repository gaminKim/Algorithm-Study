import sys
from collections import deque
input = sys.stdin.readline

def add():
    t = min(bowl[0])
    for i in range(len(bowl[0])):
        if bowl[0][i] == t:
            bowl[0][i] += 1

def rotate1():
    s, w, h, i = 0, 1, 1, 0
    while True:
        if n - s - w < h:
            break
        
        for nx in range(s, s + w):
            for ny in range(h):
                bowl[s-nx+w][s+ny+w] = bowl[ny][nx]
                bowl[ny][nx] = 0
                
        s += w
        if i % 2 == 0:
            h += 1
        else:
            w += 1
        i += 1

def rotate2():
    tc, w, s, h = 2, n , 0, 1
    
    while tc > 0:
        w //= 2
        for i in range(w):
            for j in range(h):
                bowl[2*h-j-1][n-1-i] = bowl[j][s + i]
                bowl[j][s + i] = 0
        
        s += w
        h *= 2
        tc -= 1

def origin():
    k = 0
    for i in range(n):
        if bowl[0][i] == 0:
            continue
        
        j = 0
        while True:
            if j >= n or bowl[j][i] == 0:
                break
            
            bowl[0][k] = bowl[j][i]
            if j >= 1:
                bowl[j][i] = 0
            j += 1
            k += 1

def cal():
    loc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    plus = []
    minus = []
    
    for i in range(n):
        for j in range(n):
            if bowl[i][j] == 0:
                continue
            for x, y in loc:
                nx = i + x
                ny = j + y
                
                if 0 <= nx < n and 0 <= ny < n and bowl[nx][ny] != 0:
                    if bowl[i][j] > bowl[nx][ny]:
                        dif = (bowl[i][j] - bowl[nx][ny]) // 5
                        plus.append((nx,ny,dif))
                        minus.append((i,j,dif))
                        
    for i, j, d in plus:
        bowl[i][j] += d
        
    for i, j, d in minus:
        bowl[i][j] -= d
        
            
n, k = map(int, input().split())
bowl = []

for i in range(n):
    if i == 0:
        bowl.append(list(map(int, input().split())))
    else:
        bowl.append([0] * n)

res = max(bowl[0]) - min(bowl[0])
cnt = 0

while res > k:
    add()
    rotate1()
    cal()
    origin()
    rotate2()
    cal()
    origin()
    res = max(bowl[0]) - min(bowl[0])
    cnt += 1
    
print(cnt)