# https://leetcode.com/problems/valid-palindrome/
import collections
from typing import Deque


def is_palindrome(self, s: str) -> bool:
    strs: Deque = collections.deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # palindrome 판별
    while len(strs) > 1:
        if strs.popleft(0) != strs.pop():
            return False

    return True
