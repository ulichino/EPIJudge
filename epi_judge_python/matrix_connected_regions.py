from typing import List
from collections import deque

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    color = image[x][y]
    queue = deque([(x, y)])
    while queue:
        a,b = queue.popleft()
        image[a][b] = 1 - color
        for i, j in ((a+1, b), (a-1, b), (a, b+1), (a, b-1)):
            if 0 <= i and i < len(image) and 0 <= j and j < len(image[0]) and image[i][j] == color:
                queue.append((i, j))
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
