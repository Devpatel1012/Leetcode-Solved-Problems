class Solution(object):
    def binaryGap(self, n):
        Bn = bin(n)[2:]
        if Bn.count('1') == 1:
            return 0
        ans = 0
        curr = 0
        for i in range(len(Bn)):
            if Bn[i] == '1':
                ans = max(ans,curr)
                curr = 1
            else:
                curr+=1
        return ans
                

        