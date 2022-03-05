import collections

def solution(rows, columns, queries):
    answer = []
    board = [[i for i in range(row * columns+1, row * columns + columns + 1 )] for row in range(rows)]
    
    for query in queries:
        x1, y1, x2, y2 = query
        result = 10001
        tmp = collections.deque([])
        
        for i in range(y1-1, y2):
            result = min(result, board[x1-1][i])
            tmp.append(board[x1-1][i])
        for i in range(x1, x2):
            result = min(result, board[i][y2-1])
            tmp.append(board[i][y2-1])
        for i in range(y2-2, -1, -1):
            if i == y1 - 1:
                break
            result = min(result, board[x2-1][i])
            tmp.append(board[x2-1][i])
            
        for i in range(x2-1, -1, -1):
            if i == x1 -1:
                break
            result = min(result, board[i][y1-1])
            tmp.append(board[i][y1-1])
        answer.append(result)
        
        for i in range(y1-1, y2-1):
            board[x1-1][i+1] = tmp.popleft()
        for i in range(x1, x2):
            board[i][y2-1] = tmp.popleft()
        for i in range(y2-2, -1, -1):
            if i == y1 - 1:
                break
            board[x2-1][i] = tmp.popleft()
        for i in range(x2-1, -1, -1):
            if i == x1 -1:
                break
            board[i][y1-1] = tmp.popleft()
        
        board[x1-1][y1-1] = tmp.popleft()
        result = min(result, board[x1-1][y1-1])
    return answer