class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        res = 0
        hh, mm = int(loginTime[:2]), int(loginTime[3:])
        hh2, mm2 = int(logoutTime[:2]), int(logoutTime[3:])
        
        if hh > hh2:
            hh2 += 24
        else:
            if hh == hh2:
                if mm > mm2:
                    hh2 += 24
        if mm % 15:
            mm += 15 - (mm % 15)
        if mm == 60:
            hh += 1
            mm = 0
        while hh2 >= hh:
            mm += 15
            if hh == hh2 and mm2 < mm:
                break
            if mm == 60:
                mm = 0
                hh += 1
            res += 1
        return res