class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        def backtrack(start, path):
            # If we have 4 parts and are at the end of the string → valid IP
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return
            
            # Try segments of length 1 to 3
            for length in range(1, 4):
                if start + length > len(s):  # Out of bounds
                    break
                segment = s[start:start+length]
                
                # Skip invalid segments (leading zero or >255)
                if (segment[0] == "0" and len(segment) > 1) or int(segment) > 255:
                    continue
                
                backtrack(start + length, path + [segment])

        backtrack(0, [])
        return res
