class Solution(object):
    def smallestSubsequence(self, s):
        occu = {c:i for i,c in enumerate(s)}
        stack = []
        seen = set()

        for i,c in enumerate(s):
            if c not in seen:
                while stack and stack[-1]> c and occu[stack[-1]]>i:
                    seen.remove(stack.pop())
                stack.append(c)
                seen.add(c)
        return ''.join(stack)
        