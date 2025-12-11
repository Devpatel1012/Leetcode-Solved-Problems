class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        r,c = {},{}
        for x,y in buildings:
            if x not in r:
                r[x] = [y,y]
            else:
                r[x][0] = min(r[x][0],y)
                r[x][1] = max(r[x][1],y)
            if y not in c:
                c[y] = [x,x]
            else:
                c[y][0] = min(c[y][0],x)
                c[y][1] = max(c[y][1],x)
        
        ans = 0
        for x,y in buildings:
            a,b = r[x]
            e,d = c[y]
            if e<x<d and a<y<b:
                ans+=1
        return ans

