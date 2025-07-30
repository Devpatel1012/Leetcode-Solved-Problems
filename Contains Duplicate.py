class Solution(object):
    def containsDuplicate(self, nums):
        dic = {}
        for val in nums:
            if val in dic:
                return True
            else:
                dic[val] = 1
        return False