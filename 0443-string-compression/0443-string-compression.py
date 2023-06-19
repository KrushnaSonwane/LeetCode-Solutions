class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        l, r, count = 0, 0, 0
        res = 0
        while r < n:
            if chars[l] == chars[r]:
                count += 1
            else:
                chars[res] = chars[l]
                res += 1
                if count >= 2:
                    for ch in str(count):
                        chars[res] = ch
                        res += 1
                l = r
                count = 1
            r += 1
        chars[res] = chars[l]
        res += 1
        if count >= 2:
            for ch in str(count):
                chars[res] = ch
                res += 1
            return res
        return res