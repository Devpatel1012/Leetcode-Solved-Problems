from collections import deque

class Solution(object):
    def canReach(self, s, minJump, maxJump):
        n = len(s)

        if s[-1] != '0':
            return False

        q = deque([0])
        farthest = 0

        while q:
            i = q.popleft()

            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump, n - 1)

            for j in range(start, end + 1):
                if s[j] == '0':
                    if j == n - 1:
                        return True
                    q.append(j)

            farthest = end

        return n == 1