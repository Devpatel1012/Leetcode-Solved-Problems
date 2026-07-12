class Solution(object):
    def arrayRankTransform(self, arr):
        occur = defaultdict(int)
        newArr = sorted(list(set(arr)))
        for i in range(len(newArr)):
            occur[newArr[i]] = i+1
        ans = list()
        for i in arr:
            ans.append(occur[i])
        return ans
            

        