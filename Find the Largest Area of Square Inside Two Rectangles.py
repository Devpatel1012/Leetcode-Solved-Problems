class Solution(object):
    def largestSquareArea(self, bl, tr):
       
        def area(x1,x2):
            side = min(x2[0] - x1[0],x2[1]-x1[1])
            return (side * side)

        ans = 0
        for i in range(len(bl)):
            cor1 = bl[i]
            cor2 = tr[i]
            for j in range(i+1,len(bl)):
                cor3 = bl[j]
                cor4 = tr[j]

                if (((cor1[0]<=cor4[0])and(cor2[0]>=cor3[0]))and((cor1[1]<=cor4[1])and (cor2[1]>=cor3[1]))):
                    x1,y1 = max(cor1[0],cor3[0]),max(cor1[1],cor3[1])
                    x2,y2 = min(cor2[0],cor4[0]),min(cor2[1],cor4[1])
                    if x1<x2 and y1<y2:
                        ans = max(ans,area([x1,y1],[x2,y2]))
        
        return ans