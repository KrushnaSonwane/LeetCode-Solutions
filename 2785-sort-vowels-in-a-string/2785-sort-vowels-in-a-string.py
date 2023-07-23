class Solution:
    def sortVowels(self, s: str) -> str:
        res = [ch for ch in s]
        vowels =[]
        for ch in s:
            if ch in 'aeiouAEIOU':
                vowels.append(ch)
        vowels.sort()
        for i, ch in enumerate(res):
            if ch in 'aeiouAEIOU':
                res[i] = vowels.pop(0)
        return ''.join(res)