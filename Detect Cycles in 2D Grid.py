class Solution(object):
    def containsCycle(self, grid):
        n, m = len(grid) , len(grid[0])
        check = [[False]*m for i in range(n)]

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(x,y,px,py,char):
            if check[x][y]:
                return True
            check[x][y] = True

            for dx,dy in directions:
                nx,ny = x+dx,y+dy

                if 0<=nx<n and 0<=ny<m and grid[nx][ny] == char:

                    if nx == px and ny == py:
                        continue
                    
                    if dfs(nx,ny,x,y,char):
                        return True
            return False

        for i in range(n):
            for j in range(m):
                if not check[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True
        return False