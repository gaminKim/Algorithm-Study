def solution(msg):
    answer = []
    dic = [0]
    k = 0
    
    j = 65
    for i in range(1, 27):
        dic.append(chr(j))
        j += 1
        
    while len(msg) > 0:
        if len(msg) == 1:
            answer.append(dic.index(msg))
            break

        for i in range(1, len(msg)):
            if msg[:i] in dic and msg[:i+1] not in dic:
                k = i
                break
            if i == len(msg) - 1:
                answer.append(dic.index(msg))
                return answer
            
        idx = dic.index(msg[:k])
        answer.append(idx)
        dic.append(msg[:k+1])
        msg = msg[k:]
    
    return answer