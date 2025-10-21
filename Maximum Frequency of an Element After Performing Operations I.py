# import collections
# from sortedcontainers import SortedDict

# class Solution:
#     def maxFrequency(self, nums, k, numOperations): 
#         """
#         Solves LeetCode 3346 using a corrected sweep-line algorithm.
#         """
        
#         # 1. Count elements already at their positions (cost 0 operations)
#         count_at_pos = collections.Counter(nums)
        
#         # 2. Create the sweep-line map (difference array)
#         line = SortedDict()

#         for num in nums:
#             start = num - k
#             end = num + k
            
#             # Mark the start of the range: +1
#             line[start] = line.get(start, 0) + 1
            
#             # Mark the end of the range: -1
#             line[end + 1] = line.get(end + 1, 0) - 1
            
#             # --- THIS IS THE FIX ---
#             # We must also add the original number's position to the map.
#             # This ensures that the sweep-line loop will stop and 
#             # calculate the frequency at this exact position, even if
#             # it's not a boundary point.
#             # Adding 0 (via .get(num, 0)) doesn't affect the sweep-line 
#             # 'current_adjustable' count if the key already exists.
#             line[num] = line.get(num, 0)
#             # -----------------------

        
#         max_freq = 0
        
#         # current_adjustable tracks the total number of nums that 
#         # *can* be transformed into the current 'position'.
#         current_adjustable = 0

#         # 3. Iterate through all sorted critical positions
#         # (This now includes all start points, end points, AND original num points)
#         for position in line:
#             # Update the count of adjustable elements at this position
#             current_adjustable += line[position]
            
#             # Get how many elements are *already* at this position
#             already_at_pos = count_at_pos.get(position, 0)
            
#             # Calculate how many elements *need* an operation
#             # (Total that can reach here) - (Already here)
#             adjustable_needed = current_adjustable - already_at_pos
            
#             # We can only use the operations we have
#             ops_to_use = min(adjustable_needed, numOperations)
            
#             # The total frequency for this 'position' is:
#             # (Already here) + (The ones we can afford to change)
#             total_freq_at_pos = already_at_pos + ops_to_use
            
#             # 4. Update the maximum frequency found
#             max_freq = max(max_freq, total_freq_at_pos)
            
#         return max_freq
# from collections import Counter

# class Solution(object):
#     def maxFrequency(self, A, k, numOperations):
#         A.sort()
#         n = len(A)

#         # case 1
#         count = Counter()
#         res = i = j = 0
#         for a in A:
#             while j < n and A[j] <= a + k:
#                 count[A[j]] += 1
#                 j += 1
#             while i < n and A[i] < a - k:
#                 count[A[i]] -= 1
#                 i += 1
#             cur = min(j - i, count[a] + numOperations)
#             res = max(res, cur)

#         # case 2
#         i = 0
#         for j in range(n):
#             while A[i] + k + k < A[j]:
#                 i += 1
#             res = max(res, min(j - i + 1, numOperations))

#         return res

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        cnt = {}
        d = {}
        
        # Build frequency map and difference map (ensure x is an event key)
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
            d[x] = d.get(x, 0)                 # <-- important: ensure x is present
            d[x - k] = d.get(x - k, 0) + 1
            d[x + k + 1] = d.get(x + k + 1, 0) - 1
        
        s = 0
        answer = 0
        for x in sorted(d.keys()):
            s += d[x]
            freq_here = cnt.get(x, 0)
            answer = max(answer, min(s, freq_here + numOperations))
        
        return answer