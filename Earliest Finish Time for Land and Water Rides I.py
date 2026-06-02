class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        n , m = len(landStartTime), len(waterStartTime)

        ans = float("inf")

        for i in range(n):
            land = landStartTime[i] + landDuration[i]
            for j in range(m):
                water = waterStartTime[j]+ waterDuration[j]

                if land >= waterStartTime[j]:
                    ans = min(ans,(land+waterDuration[j]))
                else:
                    offset = waterStartTime[j] - land
                    ans = min(ans,(land+offset+waterDuration[j]))
                
                if water >= landStartTime[i]:
                    ans = min(ans,(water + landDuration[i]))
                
                else:
                    offset = landStartTime[i] - water
                    ans = min(ans,(water + offset + landDuration[i]))
        
        return ans


        