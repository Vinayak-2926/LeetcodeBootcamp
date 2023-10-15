class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapped_chars = set()
        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] in mapped_chars: return False
                mapping[s[i]] = t[i]
                mapped_chars.add(t[i])
            elif mapping[s[i]] != t[i]: return False
        return True