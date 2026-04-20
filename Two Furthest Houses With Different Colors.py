class Solution(object):
    def maxDistance(self, colors):
        ans = 0
        n = len(colors)
        for i in range(n):
            curr = colors[i]
            for j in range(i+1,n):
                if colors[j] != curr:
                    ans = max(ans,abs(i-j))
        return ans

        