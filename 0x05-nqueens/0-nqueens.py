#!/usr/bin/python3
'''n-queens problem refer readme'''

import sys


def check(board, row, col, n):
    '''check if a queen can be placed on board[row][col]'''
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True


def solve(board, col, n):
    '''solve n-queens problem'''
    if col == n:
        print([[i, row.index(1)] for i, row in enumerate(board)])
        return
    for i in range(n):
        if check(board, i, col, n):
            board[i][col] = 1
            solve(board, col + 1, n)
            board[i][col] = 0


def nqueens(n):
    '''n-queens problem'''
    board = [[0 for j in range(n)] for i in range(n)]
    solve(board, 0, n)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)
    nqueens(n)
