class Solution(object):
    def validateCoupons(self, code, b, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        ans = dict()
        business = {'electronics':0,'grocery':1,'pharmacy':2,'restaurant':3}
        for i in range(len(isActive)):
            if(isActive[i]):
                if code[i] and (all(c.isalnum() or c=='_' for c in code[i])) and (b[i] in business):
                    ans[code[i]] = b[i]
        
        ansi = sorted(ans.items(), key=lambda item: (business[item[1]],item[0]))
        return [code for code,_ in ansi]
