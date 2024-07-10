from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder = 0
        for i in logs:
            folder = max(0, folder)
            if i[0].isalnum():
                folder += 1
            elif i == '../':
                folder -= 1
        return max(0,folder)