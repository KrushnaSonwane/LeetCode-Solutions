class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        flag = 0
        for i in range(0, len(s)):
            if flag == 1:
                flag = 0
            else:
                if s[i] == 'I':
                    if i != len(s)-1:
                        if s[i+1] == 'V':
                            num += 4
                            flag = 1
                        elif s[i+1] == 'X':
                            num += 9
                            flag = 1
                        else:
                            num += 1
                    else:
                        num += 1
                elif s[i] == 'X':
                    if i != len(s)-1:
                        if s[i+1] == 'L':
                            num += 40
                            flag = 1
                        elif s[i+1] == 'C':
                            num += 90
                            flag = 1
                        else:
                            num += 10
                    else:
                        num += 10
                elif s[i] == 'C':
                    if i != len(s)-1:
                        if s[i+1] == 'D':
                            num += 400
                            flag = 1
                        elif s[i+1] == 'M':
                            num += 900
                            flag = 1
                        else:
                            num += 100
                    else:
                        num += 100
                elif s[i] == "V":
                    num += 5
                elif s[i] == "L":
                    num += 50
                elif s[i] == "D":
                    num += 500
                elif s[i] == "M":
                    num += 1000
        return num