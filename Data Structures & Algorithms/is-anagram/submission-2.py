from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counts = Counter(s)
        t_counts = Counter(t)

        return s_counts == t_counts