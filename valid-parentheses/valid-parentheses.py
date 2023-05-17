class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if stack: close = stack.pop()
                else: return False
                if ch == ')' and close == '(': continue
                if ch == '}' and close == '{': continue
                if ch == ']' and close == '[': continue
                else: return False
        return stack == []