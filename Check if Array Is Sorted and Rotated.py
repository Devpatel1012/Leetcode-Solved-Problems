class Solution(object):
    def check(self, nums):
        n = len(nums)
        i = 0
        rot = 0
        while (i<n-1):
            if nums[i]<=nums[i+1]:
                i+=1
            else:
                rot = i+1
                break
        
        print(rot)
        prev = nums[(rot)%n]
        for j in range(1,n):
            curr = nums[(j+rot)%n]
            if curr>=prev:
                prev = curr
            else:
                return False

        return True
            


        