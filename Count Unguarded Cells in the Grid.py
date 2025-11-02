class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[0]*n for _ in range(m)]

        for r,c in guards:
            grid[r][c] = 1
        for r,c in walls:
            grid[r][c] = 2

        def mark_guarded(r,c):
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr,nc = r+dr, c+dc
                while 0<=nr<m and 0<=nc<n and grid[nr][nc] not in (1,2):
                    if grid[nr][nc] == 0:
                        grid[nr][nc] =3
                    nr += dr
                    nc += dc

        for r,c in guards:
            mark_guarded(r,c)

        ans = sum(grid[r][c] == 0 for r in range(m) for c in range(n))
        return ans        