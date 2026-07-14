class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def subsequencePairCount(self, nums):
        MOD = 1000000007
        m = max(nums)

        dp = [[0] * (m + 1) for _ in xrange(m + 1)]
        dp[0][0] = 1

        
        for num in nums:
            ndp = [[0] * (m + 1) for _ in xrange(m + 1)]

            for j in xrange(m + 1):
                divisor1 = self.gcd(j, num)
                for k in xrange(m + 1):
                    val = dp[j][k]
                    if val == 0:
                        continue

                    divisor2 = self.gcd(k, num)

                    # Ignore num
                    ndp[j][k] = (ndp[j][k] + val) % MOD

                    # Put num in seq1
                    ndp[divisor1][k] = (ndp[divisor1][k] + val) % MOD

                    # Put num in seq2
                    ndp[j][divisor2] = (ndp[j][divisor2] + val) % MOD
                    print("ndp",ndp)

            dp = ndp
            print("dp",dp)

        ans = 0
        for j in xrange(1, m + 1):
            ans = (ans + dp[j][j]) % MOD

        return ans