class Solution(object):
    
    def isPalindrome(self, x):
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return False
        stri = str(x)
        ans = True
        reve = stri[::-1]
        if(stri == reve):
            ans = True
        else:
            ans = False

        return ans
soul = Solution()
x = 122
print(soul.isPalindrome(x))