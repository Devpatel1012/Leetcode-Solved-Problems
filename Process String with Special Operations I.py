class Solution(object):
    def processStr(self, s):

        result = []
        for ch in s:
            if ch == "*":
                if result:
                    result.pop()
            elif ch == "#":
                result += result
            elif ch == "%":
                result = result[::-1]
            else:
                result.append(ch)
        return "".join(result)