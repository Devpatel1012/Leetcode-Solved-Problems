class Solution(object):
    def minAbsDiff(self, grid, k):
        n,m = len(grid), len(grid[0])
        result = []

        for i in range(n-k+1):
            row = []
            for j in range(m-k+1):
                values = []
                for r in range(i, i + k):
                    values.extend(grid[r][j:j+k])
                sorted_values = sorted(set(values))

                if len(sorted_values)<=1:
                    row.append(0)
                else:
                    min_diff = float("inf")
                    for idx in range(len(sorted_values)-1):
                        diff = sorted_values[idx+1] - sorted_values[idx]
                        min_diff = min(min_diff,diff)
                    row.append(min_diff)
            result.append(row)
        return result
        