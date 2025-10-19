class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # solution with O(1) space with O(n) time complexity

        cand1,cand2, count1, count2 = None, None, 0, 0

        for num in nums:
            if num == cand1 : 
                count1 += 1
            elif num == cand2 : 
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2  == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        for c in [cand1,cand2]:
            if nums.count(c) > len(nums)//3:
                res.append(c)

        return res        

        # output = []
        # counts = {}
        # n = len(nums) // 3

        # for num in nums:
        #     if num not in counts:
        #         counts[num] = 0
        #     counts[num] += 1
        
        # for num in counts:
        #     if counts[num] > n:
        #         output.append(num)
        
        # return output

        # n = len(nums)
        # res = []
        # mpp = {}
        # for ele in nums:
        #     mpp[ele] = mpp.get(ele, 0) + 1

        # for ele in mpp.keys():
        #     if mpp[ele] > (n//3): 
        #         res.append(ele)
        
        # return res