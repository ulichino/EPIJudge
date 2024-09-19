from typing import List
from collections import deque

from test_framework import generic_test

def mark_reachable_region(x, y, board):
    queue = deque([(x, y)])
    while queue:
        a, b = queue.popleft()
        board[a][b] = 'T'
        for i, j in ((a+1, b), (a-1, b), (a, b+1), (a, b-1)):
            if 0 <= i and i < len(board) and 0 <= j and j < len(board[0]) and board[i][j] == 'W':
                queue.append((i, j))


def fill_surrounded_regions(board: List[List[str]]) -> None:
    rows = len(board)
    cols = len(board[0])

    for i in range(rows):
        if board[i][0] == 'W':
            mark_reachable_region(i, 0, board)
        if board[i][cols-1] == 'W':
            mark_reachable_region(i, cols-1, board)

    for j in range(cols):
        if board[0][j] == 'W':
            mark_reachable_region(0, j, board)
        if board[rows-1][j] == 'W':
            mark_reachable_region(rows-1, j, board)

    for i in range(rows):
        for j in range(cols):
            board[i][j] = 'B' if board[i][j] != 'T' else 'W'
    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
