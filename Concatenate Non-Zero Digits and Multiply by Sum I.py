class Solution:
    def sumAndMultiply(self, n):
        n=str(n)
        if n.count('0')==len(n):
            return 0
        count='' 
        countt=[]   
        for i in n:
            if int(i):
                count+=i
                countt.append(int(i))
        return sum(countt)*int(count)     
