from collections import defaultdict, deque

class Solution(object):
    def remainingMethods(self, n, k, invocations):
        connect = defaultdict(list)

        for a, b in invocations:
            connect[a].append(b)

        removableComp = set()
        queue = deque([k])

        while queue:
            curr = queue.popleft()
            if curr in removableComp:
                continue
            removableComp.add(curr)
            for nxt in connect[curr]:
                queue.append(nxt)

        for method in range(n):
            if method not in removableComp:
                if not set(connect[method]).isdisjoint(removableComp):
                    return range(n)  

        return [i for i in range(n) if i not in removableComp]