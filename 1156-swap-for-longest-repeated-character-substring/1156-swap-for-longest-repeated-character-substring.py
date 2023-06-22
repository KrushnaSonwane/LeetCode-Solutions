class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = collections.Counter(text)
        hashT = defaultdict(int)
        res = ptr = 0
        for ch in text:
            hashT[ch] += 1
            curr = 0
            for ch2 in hashT:
                if hashT[ch2] > 1: curr += 1
            while len(hashT) > 2 or curr == 2:
                hashT[text[ptr]] -= 1
                if hashT[text[ptr]] == 1: curr -= 1
                if hashT[text[ptr]] == 0: del hashT[text[ptr]]
                ptr += 1                
            for ch2 in hashT:
                res = max(res, hashT[ch2] + int(count[ch2] > hashT[ch2]))
        return res