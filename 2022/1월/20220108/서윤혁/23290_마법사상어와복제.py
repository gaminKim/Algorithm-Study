import sys
import copy
from collections import deque

input = sys.stdin.readline

def second(sx, sy):
    for i in range(4):
        for j in range(4):
            if grid[i][j]:
                fish = grid[i][j]
                for k in fish:
                    f = 0
                    d = k
                    for _ in range(8):
                        x, y = dir[d]
                        nx = i + x
                        ny = j + y
                        if (sx, sy) != (nx, ny) and (0<=nx<4 and 0<=ny<4) and (smell[nx][ny] == 0):
                            f = 1
                            break
                        d -= 1
                        if d == 0:
                            d += 8       
                    if f:
                        t_grid[nx][ny].append(d)
                    else:
                        t_grid[i][j].append(k)
            

def third(sx, sy, cnt, depth, visited):
    global max_eat, loc_shark, eat
    
    if depth == 3:
        if max_eat < cnt:
            max_eat = cnt
            loc_shark = (sx, sy)
            tmp = []
            for i in visited:
                tmp.append(i)
            eat = tmp
        return
    
    for j in range(4):
        nx = sx + loc[j][0]
        ny = sy + loc[j][1]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if(nx, ny) not in visited:
                visited.append((nx, ny))
                third(nx, ny, cnt + len(t_grid[nx][ny]), depth + 1, visited)
                visited.remove((nx, ny))
            else:
                third(nx, ny, cnt, depth + 1, visited)
    
    
def fourth():
    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                smell[i][j] -= 1

def fifth():
    for i in range(4):
        for j in range(4):
            for k in copy_grid[i][j]:
                t_grid[i][j].append(k)

    
m, s = map(int, input().split())
grid = [[deque([]) for _ in range(4)] for _ in range(4)]
smell = [[0] * 4 for _ in range(4)]

dir = {
    1: (0, -1),
    2: (-1, -1),
    3: (-1, 0),
    4: (-1, 1),
    5: (0, 1),
    6: (1, 1),
    7: (1, 0),
    8: (1, -1),
}
for _ in range(m):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    
    grid[x][y].append(d)

loc = [(-1, 0), (0, -1), (1, 0), (0, 1)]
sx, sy = map(int, input().split())
sx -= 1 
sy -= 1
ans = 0
loc_shark = (sx, sy)

while s > 0:
    eat = []
    max_eat = -1
    t_grid = [[deque([]) for _ in range(4)] for _ in range(4)]
    copy_grid = copy.deepcopy(grid)
    second(sx, sy)
    third(sx, sy, 0, 0, [])
    for s1, s2 in eat:
        if t_grid[s1][s2]:
            t_grid[s1][s2] = deque([])
            smell[s1][s2] = 3
    fourth()
    fifth()
    grid = copy.deepcopy(t_grid)
    sx, sy = loc_shark
    s -= 1

for i in range(4):
    for j in range(4):
        ans += len(t_grid[i][j])
        
print(ans)