
class Solution(object):
    def smallestPalindrome(self, s):
        store = defaultdict(int)
        res = ''
        singles = ''
        for i in s:
            store[i]+=1
        for letter in string.ascii_lowercase:
            res+=letter*(store[letter]//2)
            if store[letter]%2==1:
                singles+=letter
        return res+singles+res[::-1]
