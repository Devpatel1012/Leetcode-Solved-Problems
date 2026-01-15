class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """


        # hBars.sort()
        # vBars.sort()
        # hdiff=0
        # vdiff=0
        # count=0
        # i=0
        # j=0
        # while i<(len(hBars)-1): 
        #     if hBars[i]+1==hBars[i+1]:
        #         count+=1
        #         i+=1
        #     else:
        #         hdiff=max(hdiff,count)
        #         count=0
        #         i+=1
        # hdiff=max(hdiff,count)
        # count=0
        # while j<(len(vBars)-1): 
        #     if vBars[j]+1==vBars[j+1]:
        #         count+=1
        #         j+=1
        #     else:
        #         vdiff=max(vdiff,count)
        #         count=0
        #         j+=1
        # vdiff=max(vdiff,count)
        
        # x=min(vdiff,hdiff)

        # return (x+2)**2
        
        def maxsequence(arr):
            start,end, maxseq = 0,0,0
            for i in arr:
                if i-1 not in arr:
                    currnum, currseq = i,1
                    while currnum+1 in arr:
                        currseq +=1
                        currnum = currnum+1

                    if currseq > maxseq:
                        maxseq = currseq
                        start = i
                        end = currnum
            return [start,end]

        hBars.sort(reverse = True)
        vBars.sort(reverse = True) 
        hseq = maxsequence(hBars)
        vseq = maxsequence(vBars)
        squarel = min(hseq[1]-hseq[0]+2,vseq[1]-vseq[0]+2)
        return (squarel*squarel)


        


        
