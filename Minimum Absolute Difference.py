class Solution(object):
    def minimumAbsDifference(self, arr):
        ans = []
        minsum = float("inf")
        arr.sort()
        for i in range(len(arr)-1):
            diff = (arr[i+1] - arr[i])
            if diff < minsum:
                minsum = diff
                ans = [[arr[i],arr[i+1]]]
            elif diff == minsum:
                ans.append([arr[i],arr[i+1]])
        
        return ans
