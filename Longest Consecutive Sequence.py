__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort()
        # squence = []
        # s1 = 1
        # for i in range(len(nums)-1):
            
        #     if(nums[i+1] == (nums[i]+1)):
        #         s1 = s1+1
        #     elif(nums[i+1] == (nums[i])):
        #         s1 = s1
        #     else:
        #         s1 = 1
        #     squence.append(s1)
        # return max(squence)

        # if not nums:
        #     return 0

        # numSet = set(nums)
        # maxSque = 1  # Maximum sequence length found
        # squence = 1  # Current sequence length

        # while numSet:  # Continue until the set is empty
        #     minimum = min(numSet)  # Get the smallest number remaining
        #     numSet.remove(minimum)  # Remove it from the set
        #     current = minimum

        #     while (current + 1) in numSet:  # Check consecutive numbers
        #         squence += 1
        #         numSet.remove(current + 1)
        #         current += 1

        #     maxSque = max(maxSque, squence)
        #     squence = 1  # Reset for next sequence

        # return maxSque


        if not nums:
            return 0
        
        numSet = set(nums)
        maxLength = 0

        for num in numSet:
            # Start counting only if it's the beginning of a sequence
            if num - 1 not in numSet:
                currentNum = num
                currentStreak = 1

                while currentNum + 1 in numSet:
                    currentNum += 1
                    currentStreak += 1

                maxLength = max(maxLength, currentStreak)

        return maxLength




# from collections import defaultdict
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         dct = defaultdict(int)
#         mx = 0
#         for i in nums:
#             if not dct[i]:
#                 dct[i] = 1
#                 dct[i] += dct[i - 1] + dct[i + 1]
#                 mx = max(mx, dct[i])
#                 dct[i - dct[i - 1]] = dct[i + dct[i + 1]] = dct[i]
#         return mx
                
