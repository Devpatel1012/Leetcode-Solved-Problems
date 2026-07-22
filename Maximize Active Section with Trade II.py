class SparseTable(object):
    def __init__(self, data):
        n = len(data)

        if n == 0:
            self.st = []
            self.log = [0]
            return

        # log table
        self.log = [0] * (n + 1)
        for i in xrange(2, n + 1):
            self.log[i] = self.log[i // 2] + 1

        self.st = [list(data)]
        k = 1

        while (1 << k) <= n:
            prev = self.st[-1]
            length = n - (1 << k) + 1
            curr = [0] * length

            offset = 1 << (k - 1)

            for i in xrange(length):
                curr[i] = max(prev[i], prev[i + offset])

            self.st.append(curr)
            k += 1

    def query(self, l, r):
        if l > r:
            return float('-inf')

        k = self.log[r - l + 1]
        return max(
            self.st[k][l],
            self.st[k][r - (1 << k) + 1]
        )


class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):

        n = len(s)
        cnt1 = s.count("1")

        zeroBlocks = []
        blockLeft = []
        blockRight = []

        i = 0
        while i < n:
            st = i

            while i < n and s[i] == s[st]:
                i += 1

            if s[st] == "0":
                zeroBlocks.append(i - st)
                blockLeft.append(st)
                blockRight.append(i - 1)

        m = len(zeroBlocks)

        # Fewer than 2 zero blocks => no gain
        if m < 2:
            return [cnt1] * len(queries)

        tmpSum = [
            zeroBlocks[i] + zeroBlocks[i + 1]
            for i in xrange(m - 1)
        ]

        sparse = SparseTable(tmpSum)

        ans = []

        for l, r in queries:

            i = bisect_left(blockRight, l)
            j = bisect_right(blockLeft, r) - 1

            # fewer than two zero blocks inside query
            if i > m - 1 or j < 0 or i >= j:
                ans.append(cnt1)
                continue

            firstLen = blockRight[i] - max(blockLeft[i], l) + 1
            lastLen = min(blockRight[j], r) - blockLeft[j] + 1

            if i + 1 == j:
                bestGain = firstLen + lastLen
            else:
                val1 = firstLen + zeroBlocks[i + 1]
                val2 = zeroBlocks[j - 1] + lastLen
                val3 = sparse.query(i + 1, j - 2)

                bestGain = max(val1, val2, val3)

            ans.append(cnt1 + bestGain)

        return ans
