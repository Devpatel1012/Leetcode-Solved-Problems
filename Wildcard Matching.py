class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_idx = 0         # index for s
        p_idx = 0         # index for p
        star_idx = -1     # last position of '*' in p
        s_tmp_idx = -1    # position in s when '*' matched

        while s_idx < len(s):
            if p_idx < len(p) and (p[p_idx] == s[s_idx] or p[p_idx] == '?'):
                # characters match or ?
                s_idx += 1
                p_idx += 1
            elif p_idx < len(p) and p[p_idx] == '*':
                # record star position and start match
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
            elif star_idx != -1:
                # backtrack: retry match from last '*'
                p_idx = star_idx + 1
                s_tmp_idx += 1
                s_idx = s_tmp_idx
            else:
                return False

        # check remaining characters in pattern
        while p_idx < len(p) and p[p_idx] == '*':
            p_idx += 1

        return p_idx == len(p)
