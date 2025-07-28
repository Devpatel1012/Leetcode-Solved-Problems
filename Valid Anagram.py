class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        freq_s = {}
        freq_t = {}

        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1

        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        return freq_s == freq_t


        