def check(p):
    if p == 1:
        return False
    for i in range(2, int((p + 1) ** 0.5) + 1):
        if p % i == 0:
            return False
    return True
    
def solution(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    
    num = rev_base[::-1]
    
    s = 0
    answer = 0
    isPrime = []
    for i in range(len(str(num))):
        if int(num[i]) == 0:
            if s != i:
                if check(int(num[s:i])):
                    answer += 1
            s = i + 1
    if num[s:] != '' and check(int(num[s:])):
        answer += 1
    
    return answer