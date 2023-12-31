class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        add, bal, = 0, 0
        for c in s:
            bal += 1 if c == '(' else -1
            if bal == -1:
                add += 1
                bal += 1
        return add + bal