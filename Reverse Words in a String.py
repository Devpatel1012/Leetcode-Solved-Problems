class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split()
        rl = l[::-1]
        res = " ".join(rl)
        return res
        