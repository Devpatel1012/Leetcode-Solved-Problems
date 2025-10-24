class Solution(object):
    def nextBeautifulNumber(self, n):
        def is_balanced(x):
            # count digits 0–9
            cnt = [0] * 10
            y = x
            while y > 0:
                d = y % 10
                if d == 0:
                    return False
                cnt[d] += 1
                y //= 10
            # now validate: for digits 1–9
            for d in range(1, 10):
                if cnt[d] > 0 and cnt[d] != d:
                    return False
            return True
        
        candidate = n + 1
        while True:
            if is_balanced(candidate):
                return candidate
            candidate += 1
            # still working to solve it this way!!
            # There is a way to solve this problem using backtracking by generating numbers greater than the given number of size n. There’s a noticeable pattern where the last numerically balanced number of size n always consists of the digit n repeated n times — for example, for a 3-digit number, the last balanced number is always 333. This pattern holds true for all numbers from size 1 to 9.
# So, my idea is to use backtracking to generate all possible balanced numbers between the given number and the last balanced number of size n, then sort them to find the nearest greater number. This approach makes the solution more efficient, because in the conventional method, if the input number is 333, we would need to run the code 1000 times to reach the next balanced number which is 1333.