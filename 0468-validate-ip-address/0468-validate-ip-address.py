class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            A = IP.split('.')
            if len(A)!=4: return "Neither"
            for num in A:
                if not num.isdigit(): return 'Neither'
                if 0 <= int(num) <= 255 and str(int(num))==num: continue
                return 'Neither'
            return 'IPv4'
        else:
            A = IP.split(':')
            if len(A) != 8: return "Neither"
            for num in A:
                if len(num) > 4 or not num: return "Neither"
                for d in num:
                    if '0' <=d <= '9' or 'A' <= d <= 'F' or 'a' <= d <= 'f': continue
                    return 'Neither'
        return 'IPv6'