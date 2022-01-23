def solution(id_list, report, k):
    answer = []
    result = {}
    report_counts = {}
    
    for users in report:
        u1, u2 = users.split(' ')

        if u1 not in result:
            result[u1] = set()
            result[u1].add(u2)
        else:
            result[u1].add(u2)
    
    for key, values in result.items():
        for v in values:
            if v not in report_counts:
                report_counts[v] = 1
            else:
                report_counts[v] += 1
                
    for id in id_list:
        count = 0
        
        if id not in result:
            answer.append(count)
            continue
        for reportee in result[id]:
            if not reportee :
                continue
            if report_counts[reportee] >= k:
                count += 1
                        
        answer.append(count)
    return answer