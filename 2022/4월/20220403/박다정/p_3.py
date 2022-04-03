import sys


def solution(n, s, a, b, fares):
    answer = sys.maxsize
    costs = [[sys.maxsize for _ in range(n)] for _ in range(n)]
    
    for fare in fares:
        x, y, cost = fare
        costs[x-1][y-1] = cost
        costs[y-1][x-1] = cost
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    costs[i][j] = 0
                    continue
                if costs[i][j] > costs[i][k] + costs[k][j]:
                    costs[i][j] = costs[i][k] + costs[k][j]
    for i in range(n):
        answer = min(answer, costs[s-1][i] + costs[i][a-1] + costs[i][b-1])
    
    return answer