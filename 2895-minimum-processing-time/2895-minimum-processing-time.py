class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        finalAnwer = 0
        for a in processorTime:
            for _ in range(4):
                finalAnwer = max(finalAnwer, a + tasks.pop())
        return finalAnwer