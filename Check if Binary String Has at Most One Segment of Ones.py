class Solution(object):
    def checkOnesSegment(self, s):
        seg = False
        for i in range(len(s)):
            if s[i] == '0':
                continue
            else:
                if seg and s[i-1] == '0':
                    return False
                else:
                    seg = True
        return True
        