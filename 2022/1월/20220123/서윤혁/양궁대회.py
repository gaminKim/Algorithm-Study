import copy
answer = [0] * 11
max_score = -1
partner_score = 0

def dfs(curr, cnt, ar, score, ar2):
    global max_score, answer, partner_score
    
    if cnt == 0:
        if score > partner_score and max_score <= score - partner_score:
            if max_score == score - partner_score:
                for i in reversed(range(len(ar2))):
                    if ar2[i] < answer[i]: 
                        break
                    elif ar2[i] > answer[i]:
                        answer = copy.deepcopy(ar2)
                        break
            else:
                max_score = score - partner_score
                answer = copy.deepcopy(ar2)
        return
    
    for i in range(1, 11):
        nx = curr + i
        if nx < 0 or nx >= 11: continue
        arrow = ar[nx] + 1
        if nx < 10 and cnt - arrow >= 0:
            score += (10 - nx)
            if arrow != 1:
                partner_score -= (10 - nx)
            cnt -= arrow
            ar2[nx] += arrow
            dfs(nx, cnt, ar, score, ar2)
            score -= (10 - nx)
            if arrow != 1:
                partner_score += (10 - nx)
            cnt += arrow
            ar2[nx] -= arrow
        elif nx == 10:
            ar2[nx] += cnt
            cnt = 0
            dfs(nx, cnt, ar, score, ar2)
            cnt += ar2[nx]
            ar2[nx] = 0
            

def solution(n, info):
    global partner_score
    
    partner_score = sum([10-i for i in range(len(info)) if info[i] > 0])

    for i in range(11):
        tmp = [0] * 11
        cnt = n
        score = 0
        if cnt - (info[i] + 1) >= 0:
            tmp[i] += info[i] + 1
            score += 10 - i
            if info[i] + 1 != 1:
                partner_score -= 10 - i
            dfs(i, cnt - tmp[i], info, score, tmp)
            tmp[i] -= info[i] + 1
            if info[i] + 1 != 1:
                partner_score += 10 - i
            score -= 10 - i
    
    if sum(answer) == 0:
        return [-1]
    else:
        return answer