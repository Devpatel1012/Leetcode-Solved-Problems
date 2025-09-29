class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # patternList = list(pattern)
        # slist = s.split()
        # dic = {}
        # for i in range(len(slist)):
        #     if patternlist[i] not in dic:
        #         dic[patterlist[i]] = slist[i]
        #     else:
        #         sample = dic[patternlist[i]]
        #         if sample != slist[i]:
        #             return False
        # return True
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):
            if c in char_to_word and char_to_word[c] != w:
                return False
            if w in word_to_char and word_to_char[w] != c:
                return False

            char_to_word[c] = w
            word_to_char[w] = c

        return True
        