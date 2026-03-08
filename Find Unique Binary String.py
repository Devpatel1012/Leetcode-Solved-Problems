class Solution(object):
    def findDifferentBinaryString(self, nums):
        inte = set()
        for num in nums:
            inte.add(int(num,2))
        
        n = len(nums)
        for num in range(n+1):
            if num not in inte:
                ans = bin(num)[2:]
                return "0"*(n-len(ans))+ans
        
        return ""
        
        