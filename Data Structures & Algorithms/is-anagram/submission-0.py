class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_sorted = ''.join(sorted(s))
            t_sorted = ''.join(sorted(t))
            if s_sorted == t_sorted:
                return True
        return False