class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ''
        for ch in s:
            if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'E' or ch == 'A' or ch == 'I' or ch == 'O' or ch == 'U':
                vowels = ch + vowels
        ans, ptr = '', 0
        for ch in s:
            if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'E' or ch == 'A' or ch == 'I' or ch == 'O' or ch == 'U':
                ans += vowels[ptr]
                ptr += 1
            else:
                ans += ch
        return ans