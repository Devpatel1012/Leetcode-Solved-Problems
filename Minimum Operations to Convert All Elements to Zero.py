class Solution:
    def minOperations(self, nums) :
        ans = 0
        stack = [0]  
        
        for num in nums:

            while stack and stack[-1] > num:
                stack.pop()

            if stack[-1] < num:
                ans += 1
                stack.append(num)
        
        return ans