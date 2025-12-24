class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        s = sum(apple)
        capacity.sort(reverse = True)
        a = capacity[0]
        if a>=s:
            return 1
        for i in range(1,len(capacity)):
           a+=capacity[i]
           if a>=s:
            return (i+1)


