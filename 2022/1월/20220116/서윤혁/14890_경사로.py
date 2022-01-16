from sys import stdin
input = stdin.readline

n, l = map(int, input().split())
li = []
answer = 0

for _ in range(n):
    li.append(list(map(int, input().split())))
    
for i in range(n):
    k = li[i][0]
    f = 0
    cnt = 1
    for j in range(1, n):
        if k == li[i][j]:
            cnt += 1
            
        elif k - li[i][j] == 1 and cnt >= 0:
            cnt = -l + 1
            k = li[i][j]
        elif li[i][j] - k == 1 and cnt >= 0:
            if cnt >= l:
                cnt = 1
                k = li[i][j]
            else:
                f = 1
                break
        else:
            f = 1
            break
    if f == 0 and cnt >= 0:
        answer += 1

for j in range(n):
    k = li[0][j]
    f = 0
    cnt = 1
    for i in range(1, n):
        if k == li[i][j]:
            cnt += 1
            
        elif k - li[i][j] == 1 and cnt >= 0:
            cnt = -l + 1
            k = li[i][j]
        elif li[i][j] - k == 1 and cnt >= 0:
            if cnt >= l:
                cnt = 1
                k = li[i][j]
            else:
                f = 1
                break
        else:
            f = 1
            break
    if f == 0 and cnt >= 0:
        answer += 1

print(answer)