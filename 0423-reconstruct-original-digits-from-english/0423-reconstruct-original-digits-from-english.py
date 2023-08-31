class Solution:
    def originalDigits(self, s: str) -> str:
        hashT, res = defaultdict(int), []
        for ch in s: hashT[ch] += 1
        A = [['0','zero'],['6','xsi'],['4','uorf'],['5','five'],['8','geiht'],['2', 'wto'],['3','three'],['1','one'],['7','seven'],['9','enin']]
        for digit, spell in A:
            count = hashT[spell[0]]
            res.append(digit*count)
            for ch in spell:
                hashT[ch] -= count
        return ''.join(sorted(res))