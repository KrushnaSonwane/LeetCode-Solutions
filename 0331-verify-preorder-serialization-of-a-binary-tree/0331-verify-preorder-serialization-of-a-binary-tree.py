class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        A = preorder.split(',')
        if A[0]=='#': return A == ['#']
        stack = [0]
        for i in range(1, len(A)):
            if A[i]=='#':
                while stack and stack[-1] == 2:
                    stack.pop()
                if not stack: return False
                stack[-1] += 1
            else:
                while stack and stack[-1] == 2:
                    stack.pop()
                if not stack: return False
                stack[-1] += 1
                stack.append(0)
        return not any(val != 2 for val in stack)