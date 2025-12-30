class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def check(r, c):
            nums = []
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    nums.append(grid[i][j])
            
            if sorted(nums) != list(range(1, 10)):
                return False
            
           
            
            if sum(grid[r][c:c+3]) != 15: return False
            if sum(grid[r+1][c:c+3]) != 15: return False
            if sum(grid[r+2][c:c+3]) != 15: return False
            
            if grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15: return False
            if grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15: return False
            if grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15: return False
            
          
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15: return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15: return False
            
            return True

        rows, cols = len(grid), len(grid[0])
        ans = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if grid[i+1][j+1] == 5:
                    if check(i, j):
                        ans += 1
        return ans
