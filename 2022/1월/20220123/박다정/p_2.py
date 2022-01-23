def getPrimeNumber(number):
    limit = int(number ** 0.5)
    numbers = [1 for i in range(number + 1)]
    
    for i in range(2, limit+1):
        if numbers[i] == 0:
            continue
        
        numbers[i] = 1
        
        for j in range(i+i, number + 1, i):
            numbers[j] = 0
            
    return numbers
        

def is_prime(num):
    if num < 2:
        return False
    limit = int(num ** 0.5)
    for i in range(2, limit + 1):
        if num % i == 0:
            return False
    return True

def convert_k_digit_number(n, k):
    result = ''
    while n > 0:
        m = n % k
        result += str(m)
        n = n // k
    return result[::-1]

def solution(n, k):
    answer = 0
    converted_number = convert_k_digit_number(n, k)
    for number in converted_number.split('0'):
        if number == '' or number == '1':
            continue
        
        if is_prime(int(number)):
            answer += 1
    
    return answer