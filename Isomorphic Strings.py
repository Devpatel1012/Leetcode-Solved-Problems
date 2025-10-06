class Solution(object):
    def isIsomorphic(self, s, t):
        def encode(word):
            mapping = {}
            pattern = []
            next_num = 0
            for ch in word:
                if ch not in mapping:
                    mapping[ch] = next_num
                    next_num += 1
                pattern.append(mapping[ch])
            return pattern
        
        return encode(s) == encode(t)
