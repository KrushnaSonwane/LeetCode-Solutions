class Solution:
    def frequencySort(self, s: str) -> str:
        hashT = {}
        for ch in s:
            if ch not in hashT:
                hashT[ch] = 1
            else:
                hashT[ch] += 1
        freq = []
        d = {}
        for ch in hashT:
            if hashT[ch] not in d:
                d[hashT[ch]] = [ch]
                freq.append(hashT[ch])
            else:
                d[hashT[ch]].append(ch)
        ans = ''
        freq.sort()
        for n in freq[::-1]:
            for ch in d[n]:
                ans += ch * n
        return ans
        