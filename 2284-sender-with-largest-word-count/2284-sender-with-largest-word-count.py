class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        A, max_, res = defaultdict(int), 0, ''
        for msg, name in zip(messages, senders):
            A[name] += msg.count(' ') + 1
            if (A[name] > max_) or A[name] == max_ and res < name:
                max_ = A[name]
                res = name
        return res