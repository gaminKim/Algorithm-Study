# 백준 캐슬 디펜스

import sys

N, M ,D = map(int, sys.stdin.readline().split(' '))
arr = []
foe = []


for n in range(N):
    arr.append(sys.stdin.readline().split(' '))
    for m in range(M):
        if arr[n][m] == '1':
            foe.append([n,m])

print(foe)
# 궁수 배치
visited = [False for _ in range(M)]
is_game_over = False
answer = 0
is_killed = [[False for _ in range(M)] for _ in range(N)]

def combi(gung, idx):
    global answer, is_game_over, is_killed
    if len(gung) == 3:
        # start game
        is_game_over = False
        is_killed = [[False for _ in range(M)] for _ in range(N)]
        answer = max(answer, start(gung))
        return

    for g in range(idx, M):
        if not visited[g]:
            gung.append(g)
            combi(gung, g+1)
        visited[g] = False
        gung.pop()



def start(gung):
    time = 0
    count = 0
    while True:
        for g in gung:
            kill = attack(g, time)
            if is_game_over: break
            if kill and not is_killed[kill[0]][kill[1]]:
                is_killed[kill[0]][kill[1]] = True
                count += 1

        if is_game_over: break
        time += 1
    print("result: ", count)
    return count

def attack(gung_m, time):
    global is_game_over
    min_gap = 100000
    kill = tuple()
    can_move = False

    for n,m in foe:
        if n+time >= N:
            continue
        can_move = True
        gap = abs(N - n-time) + abs(gung_m - m)

        if gap > D: continue
        if gap == min_gap and kill[1] < m: continue
        if gap < min_gap:
            if kill and kill[1] < m: continue
            kill = (n,m)
            min_gap = gap

    if not can_move: is_game_over = True
    return kill

combi([], 0)
print(answer)

# 게임 시작

# 공격

# 적 이동