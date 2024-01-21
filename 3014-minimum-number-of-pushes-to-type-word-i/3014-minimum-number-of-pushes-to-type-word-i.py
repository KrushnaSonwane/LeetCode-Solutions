class Solution:
    def minimumPushes(self, word: str) -> int:
        hashT = Counter(word)
        A = [[hashT[ch], ch] for ch in hashT]
        A.sort(reverse = True)
        res, count, cost = 0, 0, 1
        for c, ch in A:
            res += cost * c
            count += 1
            if count % 8 == 0:
                cost += 1
        return res
            