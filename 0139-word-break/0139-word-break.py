class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word, Q = set(wordDict), [0]
        visit = set()
        while Q:
            start = Q.pop(0)
            if start == len(s): return 1
            for end in range(start, len(s)):
                if end in visit: continue
                if s[start: end+1] in word:
                    Q.append(end+1)
                    visit.add(end)
        return 0