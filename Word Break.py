class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        hashmap = {0:True}
        for i in range(len(s)+1):
            if hashmap.get(i,False):
                for word in wordDict:
                    n = len(word)
                    if i+n<=len(s) and word == s[i:i+n]:
                        hashmap[i+n] = True
        return hashmap.get(len(s),False)
        
        # wordSet = set(wordDict)   # O(1) lookup
        # reachable = {0}           # ndex 0 is always reachable (empty string)

        # for i in range(len(s)):
        #     if i in reachable:  # only continue from reachable positions
        #         for w in wordSet:
        #             n = len(w)
        #             if s[i:i+n] == w:
        #                 reachable.add(i+n)

        # return len(s) in reachable



                


        