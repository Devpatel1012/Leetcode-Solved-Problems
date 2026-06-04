class Solution(object):
    def totalWaviness(self, num1, num2):
        ans = 0
        for i in range(num1, num2+1):
            no = str(i)
            n = len(no)
            if n < 3:
                continue
            for j in range(n):
                if (j != 0) and (j != n-1) and ((no[j-1]>no[j] and no[j]<no[j+1]) or (no[j-1]<no[j] and no[j]>no[j+1])):
                    ans += 1
        return ans
        