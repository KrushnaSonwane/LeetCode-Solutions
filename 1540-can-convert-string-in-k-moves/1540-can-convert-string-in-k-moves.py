class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t): return False
        hashT = defaultdict(int)
        for a, b in zip(s, t):
            if a != b:
                if b > a:
                    curr = ord(b)-ord(a)
                else:
                    curr = (122-ord(a))+(ord(b)-96)
                hashT[curr] += 1
        for num in sorted(hashT.keys()):
            curr = num
            for _ in range(hashT[num]):
                if curr > k: return False
                curr += 26
        return True