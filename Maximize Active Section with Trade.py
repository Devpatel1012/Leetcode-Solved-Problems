class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        total_one = 0
        mx = 0
        cnt = 0
        pre_cnt = float('-inf')
        n = len(s)
        for i, x in enumerate(s):
            cnt += 1
            if i == n - 1 or x != s[i+1]: # i becomes the end
                if x == '1':
                    total_one += cnt
                else:
                    mx = max(mx, pre_cnt + cnt)
                    pre_cnt = cnt
                cnt = 0
        return total_one + mx
