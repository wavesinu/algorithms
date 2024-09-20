from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        target = ord(target)
        for letter in letters:
            if target < ord(letter):
                return letter

        return letters[0]