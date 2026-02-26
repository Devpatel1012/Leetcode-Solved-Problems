class Solution:
    def numSteps(self, s):
   
        c=0
        
        num=int(s,2)
        while(num!=1):
            if((num&1)==1):
                num+=1
                c+=1
            else:
                num=num>>1
                c+=1
        return c