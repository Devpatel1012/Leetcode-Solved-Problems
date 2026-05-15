from bisect import bisect_right

class Solution(object):
    def numMatchingSubseq(self, s, words):

        word_dict = defaultdict(list)
        for word in words:
            word_dict[word[0]].append(word)
        
        count = 0
        for char in s:
            # Get all words waiting for this character
            waiting = word_dict[char]
            word_dict[char] = []
            
            for word in waiting:
                if len(word) == 1:
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return count
