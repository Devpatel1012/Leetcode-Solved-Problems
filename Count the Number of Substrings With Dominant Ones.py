class Solution:
    def numberOfSubstrings(self, s) :
        n = len(s)
        prev= [-1]*n #prev[1] pos of last 0 to the left of 1
        for i in range(1, n):
            if s[i-1]=='0': prev[i] = i-1
            else: prev[i] =  prev[i - 1]
        res = 0
        for i in range(n):

            zeros= 1 if s[i] == '0' else 0

            j=i

            while j>=0 and zeros**2 <= n:
                ones = (i - prev[j])-zeros
                if ones >= zeros**2:
                    res += min(j-prev[j],ones-zeros**2+1)
                j = prev[j]
                zeros +=1


        return res

        #  try to solve by your own this is the question which is solved by the seeing the youtube video!!