class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = l = res = 0
        count = defaultdict(int)
        for r in range(len(s)):
            c = s[r]
            count[c] += 1
            maxf = max(maxf, count[c])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1) 
        return res