class Solution(object):
    def mirrorDistance(self, n):
        return abs(int(str(n)[::-1]) - n)
        