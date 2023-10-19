class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        A, max_, res = defaultdict(int), 0, ''
        for msg, name in zip(messages, senders):
            A[name] += msg.count(' ') + 1
            if A[name] > max_:
                max_ = A[name]
                res = name
            elif A[name]==max_:
                res = max(res, name)
        return res