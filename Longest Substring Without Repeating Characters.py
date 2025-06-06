class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        ans = []
        i = 0

        while i < len(s):
            jcheck = []
            a1 = s[i]
            j = i + 1
            count = 1
            jcheck.append(a1)

            while j < len(s):
                a2 = s[j]
                if a2 not in jcheck:
                    jcheck.append(a2)
                    count += 1
                    j += 1
                else:
                    break

            ans.append(count)
            i += 1

        return max(ans)


solution = Solution()
s = "pwwkew"
ans = solution.lengthOfLongestSubstring(s)
print(ans)