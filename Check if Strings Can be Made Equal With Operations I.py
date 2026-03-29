class Solution(object):
    def canBeEqual(self, s1, s2):
        if s1 == s2:
            return True
        
        for i in range(4):
            if s1[i] != s2[i]:
                if  (i< 2 and s1[i] != s2[i+2] ):
                    return False
                elif (i>=2 and s1[i] != s2[i-2] ):
                    return False
        return True


        