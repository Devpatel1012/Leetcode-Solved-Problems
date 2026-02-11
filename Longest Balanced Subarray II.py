class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Segment Tree Arrays (4 * n size)
        # mins: stores the minimum value in the range
        # maxs: stores the maximum value in the range
        # lazy: stores pending updates to be pushed down
        mins = [0] * (4 * n)
        maxs = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node):
            if lazy[node] != 0:
                lazy[2*node] += lazy[node]
                mins[2*node] += lazy[node]
                maxs[2*node] += lazy[node]
                
                lazy[2*node+1] += lazy[node]
                mins[2*node+1] += lazy[node]
                maxs[2*node+1] += lazy[node]
                
                lazy[node] = 0

        def update(node, start, end, l, r, val):
            if l > end or r < start:
                return
            if l <= start and end <= r:
                mins[node] += val
                maxs[node] += val
                lazy[node] += val
                return
            
            push(node)
            mid = (start + end) // 2
            update(2*node, start, mid, l, r, val)
            update(2*node+1, mid+1, end, l, r, val)
            
            mins[node] = min(mins[2*node], mins[2*node+1])
            maxs[node] = max(maxs[2*node], maxs[2*node+1])

        # Finds the smallest index in range [0, limit_r] with value 0
        def find_first_zero(node, start, end, limit_r):
            # Optimization: If 0 is not in the range of values [min, max], return -1
            if mins[node] > 0 or maxs[node] < 0:
                return -1
            
            # If leaf node
            if start == end:
                return start if start <= limit_r and mins[node] == 0 else -1
            
            push(node)
            mid = (start + end) // 2
            
            # Try left child first (to find smallest index)
            res = -1
            if start <= limit_r:
                res = find_first_zero(2*node, start, mid, limit_r)
            
            # If not found in left, try right
            if res == -1 and mid + 1 <= limit_r:
                res = find_first_zero(2*node+1, mid+1, end, limit_r)
                
            return res

        last_occurrence = {}
        max_len = 0
        
        for right, num in enumerate(nums):
            prev_idx = last_occurrence.get(num, -1)
            
            # Range update: affect all windows starting after the previous occurrence
            # up to the current right pointer.
            if num % 2 == 0:
                # Even number: +1 balance
                update(1, 0, n-1, prev_idx + 1, right, 1)
            else:
                # Odd number: -1 balance
                update(1, 0, n-1, prev_idx + 1, right, -1)
            
            last_occurrence[num] = right
            
            # Find the leftmost index L where balance is 0
            left_idx = find_first_zero(1, 0, n-1, right)
            
            if left_idx != -1:
                max_len = max(max_len, right - left_idx + 1)
                
        return max_len