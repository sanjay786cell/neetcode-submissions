class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss, st = sorted(s), sorted(t)
        if ss == st:
            return True
        return False