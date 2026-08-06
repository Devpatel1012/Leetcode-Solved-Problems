class Solution(object):
    def smallestNumber(self, n, t):
        ans = 0
        no = n
        while ans == 0:
            curr = 1
            for i in str(no):
                curr *= int(i)
            if (curr%t == 0):
                ans = no
                break
            no += 1
        return ans
            


        