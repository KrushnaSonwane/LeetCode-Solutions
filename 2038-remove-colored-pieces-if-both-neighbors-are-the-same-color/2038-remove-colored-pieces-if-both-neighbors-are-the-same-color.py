class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        A, B = 0, 0
        count = 0
        for color in colors:
            if color == 'A': count += 1
            else:
                if count >= 3:
                    A += count - 2
                count = 0
        if count >= 2:
            A += count - 2
        count = 0
        for color in colors:
            if color == 'B':
                count += 1
            else:
                if count >= 3:
                    B += count - 2
                count = 0
        if count >= 3:
            B += count - 2
        if A > B: return 1
        if A == B: return 0
        return 0