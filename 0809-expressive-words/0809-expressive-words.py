class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        res = 0
        for word in words:
            ptr1, ptr2 = 0, 0
            m, n = len(word), len(s)
            while m > ptr1 and n > ptr2:
                if word[ptr1] != s[ptr2]: break
                f = ff = 1
                while ptr1 + 1 < m and word[ptr1] == word[ptr1 + 1]:
                    f += 1
                    ptr1 += 1
                while ptr2 + 1 < n and s[ptr2] == s[ptr2 + 1]:
                    ff += 1
                    ptr2 += 1
                if f > ff: break
                ptr1 += 1
                ptr2 += 1
                if ff < 3:
                    if ff != f: break
            else:
                if ptr1 == m and ptr2 == n: res += 1
        return res