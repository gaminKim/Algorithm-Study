from sys import stdin
input = stdin.readline

n = int(input())
li = [False, False] + [True] * (n-1)
prime = []

for i in range(2, n+1):
    if li[i]:
        prime.append(i)
        for j in range(i*i, n+1, i):
            li[j] = False

s = 0
e = 0
sum = 0
cnt = 0

while s <= e:
    
    if sum >= n:
        if sum == n:
            cnt += 1 
        sum -= prime[s]
        s += 1
    elif e == len(prime):
        break
    else:
        sum += prime[e]
        e += 1

print(cnt)