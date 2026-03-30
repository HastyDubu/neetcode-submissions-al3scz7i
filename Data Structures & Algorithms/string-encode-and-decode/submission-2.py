class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for w in strs:
            res += f"{len(w)}#{w}"
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        n = 0
        while n < len(s):
            i = n
            while s[i] != "#":
                i += 1
            length = int(s[n:i])
            word = s[i + 1: i + length + 1]
            res.append(word)
            n = i + length + 1
        return res
