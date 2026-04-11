class Solution(object):
    def minimumDistance(self, nums):
        inde = defaultdict(list)
        for i,n in enumerate(nums):
            inde[n].append(i)
        ans = float("inf")
        good = False
        for i in inde:
            curr = inde[i]
            if len(curr)>=3:
                for i in range(len(curr)+1-3):
                    dist = 2*(curr[i+2] - curr[i])
                    ans = min(ans,dist)
                    good = True
        return ans if good else -1
            
        