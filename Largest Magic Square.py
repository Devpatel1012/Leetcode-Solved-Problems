class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def check (mat):
            sumd,sumrd = 0,0
            l = len(mat)
            for i in range(l):
                sumd+=mat[i][i]
                sumrd += mat[i][l-i-1]
            if sumd == sumrd : 
                for i in range(l):
                    sumc,sumr = 0,0
                    for j in range(len(mat[0])):
                        sumr += mat[i][j]
                        sumc += mat[j][i]
                    if not(sumd == sumr == sumc):
                        return False
                return True
            else:
                return False

        
        ans = 1
        n = len(grid)
        m = len(grid[0])

        for a in range(min(n,m)+1,1,-1):
            for i in range(n-a+1):
                for j in range(m-a+1):
                    mat = [grid[r][j:j+a] for r in range(i,i+a)]
                    magic = check(mat)
                    if magic:
                        return a
        return ans
        
                    
