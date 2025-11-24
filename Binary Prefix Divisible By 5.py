class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        n = len(nums)
        ans = [False]*(n)
        no = ""
        for i in range(n):
            no = no+str(nums[i])
            noint = int(no,2)
            if (noint%5) == 0:
                ans[i] = True
        return ans

        # we can find the binary nuber to the numeric number by doing this operation curr_value = curr_value * 2 + i the code for this is like this :
        
        # result = []

        # curr_value = 0

        # for i in nums:
        #     curr_value = curr_value * 2 + i

        #     if curr_value % 5 == 0:
        #         result.append(True)
        #     else:
        #         result.append(False)
        
        # return result

            
            