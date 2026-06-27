class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sa = {}
        ta = {}

        for i in s:
            sa[i] = sa.get(i, 0) + 1

        for i in t:
            ta[i] = ta.get(i, 0) + 1

        if sa == ta:
            return True
        else:
            return False
        