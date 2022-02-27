import sys
import copy


# input = sys.stdin.readline
#
# n = int(input().rstrip())
# board = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
# result = 0


def pull_to_north(board):
    for i in range(len(board)):
        for j in range(1, len(board)):
            for k in range(j, 0, -1):
                if board[k - 1][i] != 0:
                    break
                elif board[k - 1][i] == 0 and board[k][i] != 0:
                    board[k - 1][i] = board[k][i]
                    board[k][i] = 0
    print(board)


def pull_to_south(board):
    for i in range(len(board)):
        for j in range(len(board) - 1, -1, -1):
            for k in range(j, len(board) - 1):
                if board[k + 1][i] != 0:
                    break
                elif board[k + 1][i] == 0 and board[k][i] != 0:
                    board[k + 1][i] = board[k][i]
                    board[k][i] = 0


def pull_to_west(board):
    for i in range(len(board)):
        for j in range(1, len(board)):
            for k in range(j, 0, -1):
                if board[i][k - 1] != 0:
                    break
                elif board[i][k - 1] == 0 and board[i][k] != 0:
                    board[i][k - 1] = board[i][k]
                    board[i][k] = 0
    print(board)


def pull_to_east(board):
    for i in range(len(board)):
        for j in range(len(board) - 1, -1, -1):
            for k in range(j, len(board) - 1):
                if board[i][k + 1] != 0:
                    break
                elif board[i][k + 1] == 0 and board[i][k] != 0:
                    board[i][k + 1] = board[i][k]
                    board[i][k] = 0


def slant_to_north(board):
    for i in range(1, len(board), 1):
        for j in range(len(board)):
            if board[i - 1][j] == board[i][j]:
                board[i - 1][j] *= 2
                board[i][j] = 0
    print(board)


def slant_to_south(board):
    for i in range(len(board) - 2, -1, -1):
        for j in range(len(board)):
            if board[i + 1][j] == board[i][j]:
                board[i + 1][j] *= 2
                board[i][j] = 0


def slant_to_west(board):
    for i in range(1, len(board)):
        for j in range(len(board)):
            if board[j][i - 1] == board[j][i]:
                board[j][i - 1] *= 2
                board[j][i] = 0
    print(board)


def slant_to_east(board):
    for i in range(len(board) - 2, -1, -1):
        for j in range(len(board)):
            if board[j][i + 1] == board[j][i]:
                board[j][i + 1] *= 2
                board[j][i] = 0


def dfs(current, board):
    global result

    if current > 5:
        for row in board:
            result = max(result, max(row))
        return
    for i in range(1, 5):
        tmp = copy.deepcopy(board)
        if i == 1:
            pull_to_north(tmp)
            slant_to_north(tmp)
            pull_to_north(tmp)
        elif i == 2:
            pull_to_south(tmp)
            slant_to_south(tmp)
            pull_to_south(tmp)
        elif i == 3:
            pull_to_west(tmp)
            slant_to_west(tmp)
            pull_to_west(tmp)
        elif i == 4:
            pull_to_east(tmp)
            slant_to_east(tmp)
            pull_to_east(tmp)
        dfs(current + 1, tmp)


# pull_to_north([
#     [1, 0, 0, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [1, 0, 0, 1]
# ])
#
# pull_to_north([
#     [1, 0, 0],
#     [0, 0, 0],
#     [1, 0, 1]
# ])
#
# pull_to_north([
#     [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [1, 0, 0, 1]
# ])
#
# pull_to_north([
#     [1, 1, 1],
#     [1, 1, 1],
#     [1, 1, 1]
# ])

# pull_to_south([
#     [1, 0, 0, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [1, 0, 0, 1]
# ])
#
# pull_to_south([
#     [1, 0, 0],
#     [0, 0, 0],
#     [1, 0, 1]
# ])
#
# pull_to_south([
#     [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [1, 0, 0, 1]
# ])
#
# pull_to_south([
#     [1, 1, 1],
#     [1, 1, 1],
#     [1, 1, 1]
# ])
#
# pull_to_south([
#     [1, 0, 0, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 1]
# ])

# pull_to_west([
#     [1, 0, 0, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [1, 0, 0, 1]
# ])
#
# pull_to_west([
#     [1, 0, 0],
#     [0, 0, 0],
#     [1, 0, 1]
# ])
#
# pull_to_west([
#     [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [1, 0, 0, 1]
# ])
#
# pull_to_west([
#     [1, 1, 1],
#     [1, 1, 1],
#     [1, 1, 1]
# ])
#
# pull_to_west([
#     [1, 0, 0, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 1]
# ])

# pull_to_east([
#     [1, 0, 0, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [1, 0, 0, 1]
# ])
#
# pull_to_east([
#     [1, 0, 0],
#     [0, 0, 0],
#     [1, 0, 1]
# ])
#
# pull_to_east([
#     [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [1, 0, 0, 1]
# ])
#
# pull_to_east([
#     [1, 1, 1],
#     [1, 1, 1],
#     [1, 1, 1]
# ])
#
# pull_to_east([
# [1, 0, 0, 1],
# [0, 0, 0, 1],
# [0, 0, 0, 1],
# [0, 0, 0, 1]
# ])

# slant_to_north([[1, 0, 0, 1],
#                [0, 0, 0, 1],
#                [0, 0, 0, 1],
#                [0, 0, 0, 1]])
# 
# slant_to_north([
#     [1, 1, 1],
#     [1, 1, 1],
#     [1, 1, 1]
# ])
# 
# slant_to_north([
#     [1, 1, 1],
#     [0, 0, 0],
#     [1, 1, 1]
# ])


# slant_to_south([[1, 0, 0, 1],
#                [0, 0, 0, 1],
#                [0, 0, 0, 1],
#                [0, 0, 0, 1]])
# 
# slant_to_south([
#     [1, 1, 1],
#     [1, 1, 1],
#     [1, 1, 1]
# ])
# 
# slant_to_south([
#     [1, 1, 1],
#     [0, 0, 0],
#     [1, 1, 1]
# ])


# slant_to_west([[1, 0, 0, 1],
#                [0, 0, 0, 1],
#                [0, 0, 0, 1],
#                [0, 0, 0, 1]])
# 
# slant_to_west([
#     [1, 1, 1],
#     [1, 1, 1],
#     [1, 1, 1]
# ])
# 
# slant_to_west([
#     [1, 1, 1],
#     [0, 0, 0],
#     [1, 1, 1]
# ])
# 
# slant_to_west([[1, 1, 1, 1],
#                [1, 1, 1, 1],
#                [1, 1, 1, 1],
#                [1, 1, 1, 1]])


# slant_to_east([[1, 0, 0, 1],
#                [0, 0, 0, 1],
#                [0, 0, 0, 1],
#                [0, 0, 0, 1]])
# 
# slant_to_east([
#     [1, 1, 1],
#     [1, 1, 1],
#     [1, 1, 1]
# ])
# 
# slant_to_east([
#     [1, 1, 1],
#     [0, 0, 0],
#     [1, 1, 1]
# ])
# 
# slant_to_east([[1, 1, 1, 1],
#                [1, 1, 1, 1],
#                [1, 1, 1, 1],
#                [1, 1, 1, 1]])


# dfs(1, board)
# print(result)

# pull_to_west([[8, 16, 16, 8], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
slant_to_west([[8, 16, 16, 8], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
pull_to_west([[8, 32, 0, 8], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
# slant_to_west([[256, 16, 128], [16, 256, 0], [0, 0, 0]])
# pull_to_west([[256, 16, 128], [16, 256, 0], [0, 0, 0]])
