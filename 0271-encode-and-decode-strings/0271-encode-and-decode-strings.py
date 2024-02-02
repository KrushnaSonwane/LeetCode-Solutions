class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        self.hashT, res = {}, []
        self.A, self.n = {}, len(strs)
        for i, w in enumerate(strs):
            t = ''
            for ch in w:
                res.append((chr((ord(ch)+1)%256)))
                t += chr((ord(ch)+1)%256)
                self.hashT[chr((ord(ch)+1)%256)] = ch
            self.A[i] = t
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i, j = 0, 0
        res = []
        while j < len(s):
            t = []
            for _ in range(len(self.A[i])):
                t.append(self.hashT[s[j]])
                j += 1
            curr = ''.join(t)
            res.append(curr)
            i += 1
        while self.n > len(res):
            res.append("")
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))