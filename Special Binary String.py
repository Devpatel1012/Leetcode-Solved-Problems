class Solution(object):
    def makeLargestSpecial(self, s):
        count = i = 0
        res = []
        for j,c in enumerate(s):
            count += 1 if c == '1' else -1
            if  count == 0:
                res.append('1'+self.makeLargestSpecial(s[i+1:j])+'0') 
                i = j+1
        return ''.join(sorted(res)[::-1])
        