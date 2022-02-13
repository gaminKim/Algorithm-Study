import string

def solution(msg):
    answer = []
    dic = {}

    for i, v in enumerate(list(string.ascii_uppercase)):
        dic[v] = i + 1

    dic_index = 27
    start, end = 0, 0
    
    while end <= len(msg):
        end += 1
        
        if end == len(msg):
            answer.append(dic[msg[start:end]])
            end += 1
        
        current = msg[start:end + 1]
        
        if current not in dic:
            dic[current] = dic_index
            dic_index += 1
            answer.append(dic[msg[start:end]])
            start = end
        
    return answer