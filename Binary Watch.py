class Solution(object):
    def readBinaryWatch(self, turnedOn):
        ans = []
        for hours in range(12):
            for minu in range(60):
                if bin(hours).count('1') + bin(minu).count('1') == turnedOn:
                    time = "{:d}:{:02d}".format(hours, minu)
                    ans.append(time)
        return ans   