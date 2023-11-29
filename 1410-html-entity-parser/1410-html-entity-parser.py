class Solution:
    def entityParser(self, s: str) -> str:
        res, i = [], 0
        while i < len(s):
            if s[i] == '&':
                if i + 5 < len(s) and s[i: i+6] == '&quot;':
                    res.append('"')
                    i += 5
                elif i + 5 < len(s) and s[i: i+6] == '&apos;':
                    res.append("'")
                    i += 5
                elif i + 4 < len(s) and s[i: i+5] == '&amp;':
                    res.append("&")
                    i += 4
                elif i + 3 < len(s) and s[i: i+4] == '&gt;':
                    res.append(">")
                    i += 3
                elif i + 3 < len(s) and s[i: i+4] == '&lt;':
                    res.append("<")
                    i += 3
                elif i + 6 < len(s) and s[i: i+7] == '&frasl;':
                    res.append("/")
                    i += 6
                else:
                    res.append(s[i])
            else:
                res.append(s[i])
            i += 1
        return ''.join(res)