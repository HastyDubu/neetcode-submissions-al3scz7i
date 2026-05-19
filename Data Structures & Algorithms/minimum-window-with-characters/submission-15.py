class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        window, count_t = defaultdict(int), defaultdict(int)
        for c in t:
            count_t[c] += 1
        
        have, need = 0, len(count_t)
        l = 0
        res, resLen = [-1, -1], float("inf")
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] == count_t[s[l]] - 1:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""
            