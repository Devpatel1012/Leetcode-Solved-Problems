class Solution(object):
    def hasAllCodes(self, s, k):
        total = (2**k)
        ansSet = set()
        for i in range(len(s)-k+1):
            curr = s[i:i+k]
            ansSet.add(curr)
        return len(ansSet) == total

        