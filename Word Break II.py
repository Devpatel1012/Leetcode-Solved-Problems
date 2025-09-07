class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        
        # res = []
        # def check(i,words):
        #     if i == len(s):
        #         return words
        #     for word in wordDict:
        #         n = len(word)
        #         if s[i:i+n] == word:
        #             words.append(word)
        #             otherWord = check(i+n,words)
        #             res.append(list(words))
        #             words.pop()
        # check(0,[])
        # return res
        res = []

        def check(i, words):
            if i == len(s):  # reached the end
                res.append(" ".join(words))  # build a sentence
                return

            for word in wordDict:
                n = len(word)
                if s[i:i+n] == word:
                    words.append(word)
                    check(i+n, words)
                    words.pop()  # backtrack

        check(0, [])
        return res

                    



