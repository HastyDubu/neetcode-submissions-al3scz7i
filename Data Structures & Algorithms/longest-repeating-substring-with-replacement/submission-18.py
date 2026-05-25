class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        res = 0
        maxf = 0
        for r in range(len(s)):
            c = s[r]
            count[c] = 1 + count.get(c, 0)
            maxf = max(maxf, count[c])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res