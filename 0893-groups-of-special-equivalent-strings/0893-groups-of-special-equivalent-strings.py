class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        hashT = set()
        for W in words:
            odd, even = [], []
            for i, ch in enumerate(W):
                if i%2:odd.append(ch)
                else: even.append(ch)
            hashT.add((''.join(sorted(odd)), ''.join(sorted(even))))
        return len(hashT)