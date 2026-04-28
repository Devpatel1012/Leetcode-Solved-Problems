class Solution(object):
    def minOperations(self, grid, x):
      
        arr = [val for row in grid for val in row]

        target_remainder = arr[0] % x
        for val in arr:
            if val % x != target_remainder:
                return -1
        
        arr.sort()
        n = len(arr)
        median = arr[n // 2]

        total_operations = 0
        for val in arr:
           total_operations += abs(val - median) // x
        return total_operations