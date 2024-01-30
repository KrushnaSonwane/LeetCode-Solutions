class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for n in tokens:
            if n == '+':
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif n == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif n == '*':
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif n == '/':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(float(first)/second))
            else:
                stack.append(int(n))
        return stack[0]