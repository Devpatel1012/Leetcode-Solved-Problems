class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        totalTime = 0
        groupSum = neededTime[0]
        groupMax = neededTime[0]

        for i in range(1,len(colors)):
            if colors[i] == colors[i-1]:
                groupSum += neededTime[i]
                groupMax = max(groupMax,neededTime[i])

            else:
                totalTime += groupSum-groupMax
                groupSum = neededTime[i]
                groupMax = neededTime[i]

        totalTime += groupSum- groupMax
        return totalTime