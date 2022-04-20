from itertools import combinations_with_replacement

def a(case):
    tmp = {}
    for target in case:
        if target not in tmp:
            tmp[target] = 1
        else:
            tmp[target] += 1
    return tmp


def b(info, i, tmp):
    apeach = 0
    lion = 0
    current = 10-i 
    
    if current not in tmp and info[i] > 0:
        apeach += current
        return [lion, apeach]
    elif current not in tmp and info[i] == 0:
        return [lion, apeach]


    if info[i] < tmp[current]:
        lion += current
    else:
        apeach += current
    return [lion, apeach]

def solution(n, info):
    answer = [0 for _ in range(11)]
    
    # 모든 경우의 수를 계산
    cases = list(combinations_with_replacement([i for i in range(0, 11)], n))
    dic = {}
    scores = set()
    
    for case in cases:
        tmp = a(case)
        
        lion, apeach = 0,0
        
        for i in range(len(info)):
            li, ap = b(info, i, tmp)
            lion += li
            apeach += ap
        
        
        if apeach > lion:
            continue
            
        if lion == apeach:
            continue
                
        if lion - apeach not in dic:
            dic[lion - apeach] = [case]
        else:
            dic[lion - apeach].append(case)
        scores.add(lion - apeach)
        
    if len(scores) == 0:
        return [-1]

    result = dic[max(scores)][0]

    for r in result:
        answer[10-r] += 1
    
    return answer