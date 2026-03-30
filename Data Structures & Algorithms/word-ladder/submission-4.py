class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        nei = defaultdict(list)
        wordList.append(beginWord)
        for w in wordList:
            for c in range(len(w)):
                pattern = w[:c] + "*" + w[c + 1:]
                nei[pattern].append(w)
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for c in range(len(word)):
                    pattern = word[:c] + "*" + word[c + 1:]
                    for n in nei[pattern]:
                        if n not in visit:
                            visit.add(n)
                            q.append(n)
            res += 1
        return 0