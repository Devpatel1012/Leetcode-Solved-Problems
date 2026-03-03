class Solution(object):
    def findKthBit(self, n, k):
        # curr = "0"
        # for i in range(1,n):
        #     if k<=len(curr):
        #         break

        #     invert = ''.join('1' if bit =='0' else '0' for bit in curr)

        #     curr += '1'
            
        #     curr += invert[::-1]
        
        # return curr[k-1]
        if n == 1:
            return "0"

        length = (1 << n) - 1
        mid = (length // 2) + 1

        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            mirrored = length - k + 1
            bit = self.findKthBit(n - 1, mirrored)
            return "1" if bit == "0" else "0"