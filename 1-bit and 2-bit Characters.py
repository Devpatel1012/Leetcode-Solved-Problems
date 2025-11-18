class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        # if n%2 != 0 and bits[-1] == 0:
        #     return True
        # return False
        i = 0
        while i<n:
            if i!= n-1:
                if bits[i] == 1:
                    i+=2
                else:
                    i+=1
            else:
                if bits[i] == 0:
                    return True
        return False
