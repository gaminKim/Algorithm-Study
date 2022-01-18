import math

def solution(fees, records):
    answer = []
    time_cal = {}
    mx_time = 23 * 60 + 59
    
    for x in records:
        x = x.split(' ')
        time = x[0].split(':')
        time = int(time[0]) * 60 + int(time[1])
        
        if x[2] == 'IN':
            if x[1] not in time_cal:
                time_cal[x[1]] = -time
            else:
                time_cal[x[1]] -= time
        else:
            if x[1] not in time_cal:
                time_cal[x[1]] = time
            else:
                time_cal[x[1]] += time
        
    tmp = []
    
    for x, y in time_cal.items():
        if y <= 0:
            y += mx_time
        
        if y <= fees[0]:
            tmp.append((fees[1], int(x)))
        else:       
            tmp.append((fees[1] + math.ceil((y - fees[0]) / fees[2]) * fees[3], int(x)))
    
    tmp.sort(key=lambda x : x[1])
    for x, y in tmp:
        answer.append(x)
    return answer