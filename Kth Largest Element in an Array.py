class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # nums = [n*-1 for n in nums ]
        # heapq.heapify(nums)
        # for n in range(k-1):
        #     heapq.heappop(nums)
        # return -heapq.heappop(nums)

        return  heapq.nlargest(k,nums)[-1]

