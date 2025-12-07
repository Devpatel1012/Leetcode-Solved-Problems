class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        le = (high - low)+1
        if ((low % 2 != 0) and (high % 2 != 0)):
            return (le//2)+1
        else:
            return le//2