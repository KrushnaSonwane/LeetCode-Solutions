class Solution:
    def minimumTimeToInitialState(self, word: str, key: int) -> int:
        res = 0
        for i in range(key, len(word), key):
            j, k = i, 0
            while j < len(word) and word[j] == word[k]:
                j += 1
                k += 1
            res += 1
            if j == len(word):
                return res
        return ceil(len(word) / key)