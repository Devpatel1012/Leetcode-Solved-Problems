import string

class Solution(object):
    def mapWordWeights(self, words, weights):
        lowercase = list(string.ascii_lowercase)
        lowercase.reverse()

        asciistr = []

        for word in words:
            summ = 0
            for char in word:
                summ += weights[ord(char) - 97]

            summ %= 26
            asciistr.append(lowercase[summ])

        return "".join(asciistr)