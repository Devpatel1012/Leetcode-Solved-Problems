# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res = []
        # nums.sort()  # Sort to handle duplicates

        # def backtrack(start, path):
        #     res.append(list(path))
        #     for i in range(start, len(nums)):
        #         # Skip duplicates
        #         if i > start and nums[i] == nums[i - 1]:
        #             continue
        #         path.append(nums[i])
        #         backtrack(i + 1, path)
        #         path.pop()

        # backtrack(0, [])
        # return res

        result = []  
        current_subset = [] 
        n = len(nums)
        nums.sort()

     
        def backtrack(index):
            if current_subset not in result:
                result.append(list(current_subset))

        
            for i in range(index, n):
                current_subset.append(nums[i])

                backtrack(i + 1)


                current_subset.pop()


        backtrack(0)
        return result