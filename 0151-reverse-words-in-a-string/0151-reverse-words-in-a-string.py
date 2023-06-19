class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        temp = ""
        for ch in s:
            if ch == " " and temp == "":
                continue
            elif ch != " ":
                temp += ch 
            elif ch == " " and temp != "":
                ans = temp + " " + ans
                temp = ""
        if temp != "":
                ans = temp + " " + ans
                
        if ans[-1] == " ":
            return ans[:len(ans)-1]
        return ans