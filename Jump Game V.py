class Solution(object):
    def maxJumps(self, arr, d):

        n = len(arr)

        # value -> index
        withInd = {value: i for i, value in enumerate(arr)}

        visit = [False] * n
        dp = [0] * n

        def dist(inde):

            if visit[inde]:
                return dp[inde]

            nearestjumps = []

            leftPossible = True
            rightPossible = True

            for i in range(1, d + 1):

                left = inde - i
                right = inde + i

                # LEFT
                if leftPossible and 0 <= left < n and arr[left] < arr[inde]:
                    nearestjumps.append(left)
                else:
                    leftPossible = False

                # RIGHT
                if rightPossible and 0 <= right < n and arr[right] < arr[inde]:
                    nearestjumps.append(right)
                else:
                    rightPossible = False

            best = 1   # count current index itself

            for nxt in nearestjumps:
                best = max(best, 1 + dist(nxt))

            visit[inde] = True
            dp[inde] = best

            return best

        for i in range(n):
            dist(i)

        return max(dp)