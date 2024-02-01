class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        a = 'abcdefghijklmnopqrstuvwxyz'
        b = 'zabcdefghijklmnopqrstuvwxy'
        A = {aa: bb for aa, bb in zip(a, b)}
        hashT = {}
        for w in strings:
            B = [ch for ch in w]
            for _ in range(26):
                flag = 0
                for i, ch in enumerate(B):
                    B[i] = A[ch]
                s = ''.join(B)
                if s in hashT:
                    hashT[s].append(w)
                    flag = 1
                if flag: break
            else:
                hashT[w] = [w]
        return [hashT[ch] for ch in hashT]