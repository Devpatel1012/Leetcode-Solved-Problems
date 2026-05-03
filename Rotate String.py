class Solution(object):
    def rotateString(self, s, goal):
        check = False
        for i in range(len(s)):
            curr = s[-i:] + s[:-i]
            if curr == goal:
                check = True
                break
        return check
        


        