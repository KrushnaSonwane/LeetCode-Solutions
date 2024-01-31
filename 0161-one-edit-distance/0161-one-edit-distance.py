class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s)-len(t)) >= 2: return False
        count = 0
        if len(s) == len(t):
            count = 0
            for a, b in zip(s, t):
                if a != b: 
                    count += 1
        elif len(s) > len(t):
            i, j = 0, 0
            count = 0
            while i < len(s) and len(t) > j:
                if s[i] != t[j]:
                    count += 1
                    i += 1
                else:
                    i += 1
                    j += 1
            count += len(s) - i
        else:
            i, j = 0, 0
            while len(s) > i and len(t) > j:
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
                    count += 1
            count += len(t) - j
        return count == 1