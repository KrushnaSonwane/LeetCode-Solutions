class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        A = preorder.split(',')
        if A[0]=='#': return A == ['#']
        stack = [[A[0], 0]]
        for i in range(1, len(A)):
            if A[i]=='#':
                while stack and stack[-1][-1] == 2:
                    stack.pop()
                if not stack: return False
                stack[-1][-1] += 1
            else:
                while stack and stack[-1][-1] == 2:
                    stack.pop()
                if not stack: return False
                stack[-1][1] += 1
                stack.append([A[i], 0])
        for _, val in stack:
            if val != 2: return False
        return True