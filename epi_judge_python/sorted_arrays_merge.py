from typing import List
import heapq

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    r = []
    h = []
    heapq.heapify(h)
    for array_idx, array in enumerate(sorted_arrays):
        if array:
            heapq.heappush(h, (array[0], array_idx, 1))

    while h:
        num, array_idx, next_idx = heapq.heappop(h)
        r.append(num)
        if next_idx < len(sorted_arrays[array_idx]):
            heapq.heappush(h, (sorted_arrays[array_idx][next_idx], array_idx, next_idx+1))

    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
