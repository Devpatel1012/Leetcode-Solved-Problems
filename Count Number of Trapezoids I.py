class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        import math

        group = defaultdict(int)
        for x, y in points:
            group[y] += 1

        pairs = []
        for y in group:
            if group[y] >= 2:
                pairs.append(math.comb(group[y], 2))
            else:
                pairs.append(0)

        a = sum(pairs)
        b = sum(p*p for p in pairs)

        mod = (10**9)+7

        return ((a*a - b) // 2)%mod
