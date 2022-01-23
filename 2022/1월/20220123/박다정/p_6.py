def solution(board, skill):
    answer = 0
    accumulate = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    
    
    for s in skill:
        t, r1, c1, r2, c2, degree = s
        
        if t == 1:
            degree *= -1
        
        accumulate[r1][c1] += degree
        accumulate[r2+1][c2+1] += degree
        accumulate[r1][c2+1] += degree * -1
        accumulate[r2+1][c1] += degree * -1
        
    for i in range(len(accumulate)-1):
        for j in range(len(accumulate[0])):
            accumulate[i+1][j] += accumulate[i][j]
    
    for i in range(len(accumulate)):
        for j in range(len(accumulate[0])-1):
            accumulate[i][j+1] += accumulate[i][j]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + accumulate[i][j] > 0:
                answer += 1
    
    return answer