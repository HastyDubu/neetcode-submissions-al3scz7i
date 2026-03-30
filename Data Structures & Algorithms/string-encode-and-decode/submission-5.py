class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for w in strs:
            s += f"{len(w)}#{w}"
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = length + i
            res.append(s[i:j])
            i = j
        return res