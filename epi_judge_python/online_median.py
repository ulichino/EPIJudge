import heapq
from typing import Iterator, List

from test_framework import generic_test


def online_median(sequence: Iterator[int]) -> List[float]:
    r = []
    min_heap = [] # min of maxes
    max_heap = [] # max of mins
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    for num in sequence:
        heapq.heappush(min_heap, num)
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
        if len(min_heap) < len(max_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        if len(max_heap) == len(min_heap):
            r.append((-max_heap[0] + min_heap[0]) / 2)
        else:
            r.append(min_heap[0])

    return r


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
