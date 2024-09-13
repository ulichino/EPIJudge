import heapq
from typing import List

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    result = []
    max_heap = []
    if k == 0:
        return result

    heapq.heapify(max_heap)
    heapq.heappush(max_heap, (-A[0], 0))
    for i in range(k):
        num, idx = heapq.heappop(max_heap)
        result.append(-num)

        next_idx = idx*2 + 1
        if next_idx < len(A):
            heapq.heappush(max_heap, (-A[next_idx], next_idx))

        next_idx += 1 # idx*2 + 2
        if next_idx < len(A):
            heapq.heappush(max_heap, (-A[next_idx], next_idx))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
