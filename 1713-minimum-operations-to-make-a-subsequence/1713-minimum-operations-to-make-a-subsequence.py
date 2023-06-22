class Solution(object):
    def minOperations(self, target, A):
        hashT = {a: i for i, a in enumerate(target)}
        stack = []
        for a in A:
            if a not in hashT: continue
            i = bisect.bisect_left(stack, hashT[a])
            if i == len(stack):
                stack.append(0)
            stack[i] = hashT[a]
        return len(target) - len(stack)