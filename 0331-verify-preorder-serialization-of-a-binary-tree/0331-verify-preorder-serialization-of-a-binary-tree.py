class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        A = preorder.split(',')
        if A[0]=='#': return A == ['#']
        def deleteStack():
            while stack and stack[-1]==2: 
                stack.pop()
                
        stack = [0]
        for i in range(1, len(A)):
            if A[i]=='#':
                deleteStack()
                if not stack: return False
            else:
                deleteStack()
                if not stack: return False
                stack.append(0)
            stack[-1] += 1
        return not any(val != 2 for val in stack)