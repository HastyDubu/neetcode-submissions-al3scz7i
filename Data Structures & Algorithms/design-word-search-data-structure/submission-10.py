class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.word = True
        return

    def search(self, word: str) -> bool:
        def dfs(i, root):
            cur = root
            
            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    for child in cur.children:
                        if dfs(j + 1, cur.children[child]):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        cur = self.root
        return dfs(0, cur)
