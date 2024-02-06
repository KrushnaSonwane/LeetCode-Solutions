class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashT = {}
        for ch in strs:
            c = sorted(ch)
            c = ''.join(c)
            if c in hashT:
                hashT[c].append(ch)
            else:
                hashT[c] = [ch]
        ans = []
        for ch in hashT:
            ans.append(hashT[ch])
        return ans