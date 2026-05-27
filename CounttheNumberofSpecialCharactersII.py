from collections import defaultdict

class Solution(object):
    def numberOfSpecialChars(self, word):
        occu = defaultdict(list)

        for i, ch in enumerate(word):
            occu[ch].append(i)

        ans = 0

        for ch in set(word.lower()):
            if ch in occu and ch.upper() in occu:
                if max(occu[ch]) < min(occu[ch.upper()]):
                    ans += 1

        return ans