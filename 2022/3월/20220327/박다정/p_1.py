from datetime import datetime
import math

def fill_park_out_time(records):
    result = {}
    for record in records:
        time, number, state = record.split(' ')
        if number not in result:
            result[number] = [time]
        else:
            result[number].append(time)
            
    for k, v in result.items():
        if len(v) % 2 == 1:
            v.append('23:59')
    return result  


def calculate_park_time(records):
    result = {}
    for k, v in records.items():
        accumulate_time = datetime.strptime('00:00', '%H:%M')
        for i in range(1, len(v), 2):
            accumulate_time += (datetime.strptime(v[i], '%H:%M') - datetime.strptime(v[i-1], '%H:%M'))
        time = str(accumulate_time).split(' ')[1][:5]
        
        hour, minute = map(int, time.split(':'))
        result[k] = hour * 60 + minute
        
    return result

def calculate_cost(fees, records):
    result = []

    for k, v in records.items():
        cost = 0
        
        if v <= fees[0]:
            cost = fees[1]
        else:
            cost = fees[1] + math.ceil((v - fees[0]) / fees[2]) * fees[3]
        result.append([k, cost])
    return result
        
    
def solution(fees, records):
    # 누적 주차 시간 계산
        # 입차 내역만 있고 출차 내역이 없으면 23:59분으로 간주
    records_state = fill_park_out_time(records)
    records = calculate_park_time(records_state)
    result = calculate_cost(fees, records)
    result.sort(key=lambda x: x[0])
    return list(map(lambda x: x[1], result))
    # 요금 계산
        # 기본 시간 일 때 기본 요금 청구
        # 초과하면 기본 요금 + 단위시간 * 단위 요금
        # 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면 올림

    
    # 차량 번호가 작은 자동차부터 요금을 배열에 넣고 return
        
    
    return answer