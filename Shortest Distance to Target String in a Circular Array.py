class Solution(object):
    def closestTarget(self, words, target, startIndex):
        ans = float("inf")
        exsist = False
        n = len(words)
        for i in range(n):
            if words[(startIndex+i)%n] == target :
                ans = min(ans,i)
                exsist = True
            elif words[(startIndex-i)%n] == target:
                ans = min(ans,i)
                exsist = True
        return ans if exsist else -1

        