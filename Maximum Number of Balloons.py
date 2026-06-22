class Solution(object):
    def maxNumberOfBalloons(self, text):
        ava = [1,1,2,2,1]
        ava1 = ['b','a','l','o','n']
        occur = [0]*5
        for i in range(len(text)):
            if text[i] in ava1:
                j = ava1.index(text[i])
                occur[j] += 1

        limits = []
        for need, have in zip(ava, occur):
            limits.append(have // need)
        return min(limits) if limits else 0
        # text.lower()
        # b=text.count("b")
        # a=text.count("a")
        # l=text.count("l")
        # o=text.count("o")
        # n=text.count("n")
        # count=0
        # while b>=1 and a>=1 and l>=2 and o>=2 and n>=1:
        #     b-=1
        #     a-=1
        #     l-=2
        #     o-=2
        #     n-=1
        #     count+=1
        # return count
                