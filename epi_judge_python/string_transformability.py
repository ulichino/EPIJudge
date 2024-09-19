import string
from typing import Set
from collections import deque
from test_framework import generic_test


def transform_string(D: Set[str], s: str, t: str) -> int:
    queue = deque([(s, 0)]) # string, distance
    D.remove(s)
    while queue:
        word, length = queue.popleft()
        if word == t:
            return length
        for i in range(len(word)):
            for c in string.ascii_lowercase:
                candidate = word[:i] + c + word[i+1:]
                if candidate in D:
                    queue.append((candidate, length+1))
                    D.remove(candidate)
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
