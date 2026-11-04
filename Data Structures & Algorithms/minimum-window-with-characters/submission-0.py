class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t and len(t) > len(s):
            return ""
        # Hashmaps to track count in t and s
        # Variables to track len of current window and len of t
        # final res len variables
        # Pointers to iterate through the string
        window, count_t = {}, Counter(t)
        have, need = 0, len(count_t)
        res_start, res_len = 0, float("infinity")
        left = 0

        # Loop through characters in s and check if they are in t and increment count
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            # If window len is valid, make it smaller
            while have == need:
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res_start = left
                d = s[left]
                window[d] -= 1
                if d in count_t and window[d] < count_t[d]:
                    have -= 1
                left += 1
            
        if res_len == float("infinity"):
            return ""
        return s[res_start:res_start + res_len]
            