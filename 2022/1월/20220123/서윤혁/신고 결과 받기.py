def solution(id_list, report, k):
    answer = []
    mail = {}
    for i in id_list:
        mail[i] = 0

    li = {}
    for x in report:
        tmp = x.split(' ')
        if tmp[1] not in li:
            li[tmp[1]] = set([tmp[0]])
        else:
            li[tmp[1]].add(tmp[0])
        
    for x, y in li.items():
        if len(y) >= k:
            for z in y:
                mail[z] += 1

    for x, y in mail.items():
        answer.append(y)
        
    return answer