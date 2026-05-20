class Solution(object):
    def findThePrefixCommonArray(self, a, b):
        seta = set()
        setb = set()
        ans = []

        for i in range(len(a)):
            seta.add(a[i])
            setb.add(b[i])

            ans.append(len(seta & setb))

        return ans
        