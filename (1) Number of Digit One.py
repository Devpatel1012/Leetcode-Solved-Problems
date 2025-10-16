class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        # arr = [1]*(n-1)

        # for i in range(1,len(arr)):
        #     digit = str(i)
        #     accourance = arr[i-1]+digit.count('1')
        #     arr[i] = accourance

        # return arr[-1]
   
        # count = 0
        # for i in range(1, n + 1):
        #     count += str(i).count('1')
        # return count


        if n <= 0:
            return 0

        count = 0
        m = 1  # m represents the current digit place: 1, 10, 100, ...

        while m <= n:
            higher = n // (m * 10)        # digits left of current place
            current = (n // m) % 10       # digit at current place
            lower = n % m                 # digits right of current place

            if current == 0:
                count += higher * m
            elif current == 1:
                count += higher * m + (lower + 1)
            else:  # current >= 2
                count += (higher + 1) * m

            m *= 10

        return count

        # the logic behind the if else block is still not clear check it out!!!

        