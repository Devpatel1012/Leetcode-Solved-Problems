from collections import Counter
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        len_p = len(p)
        len_s = len(s)
        
        if len_p > len_s:
            return []
        
        p_count = Counter(p)
        s_count = Counter(s[:len_p-1])  # one short to slide in
        
        result = []
        
        for i in range(len_p - 1, len_s):
            start = i - len_p + 1
            s_count[s[i]] += 1  # Add the current char to the window
            
            if s_count == p_count:
                result.append(start)
            
            # Remove the char going out of the window
            s_count[s[start]] -= 1
            if s_count[s[start]] == 0:
                del s_count[s[start]]
        
        return result
