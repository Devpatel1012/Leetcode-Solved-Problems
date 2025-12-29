class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        mapping = {}
        for t in allowed:
            key = t[:2]
            mapping.setdefault(key,[]).append(t[2])

        memo = {}        

        def dfs(row):
            if row in memo:
                return memo[row]
            if len(row) == 1:
                memo[row] = True
                return True

            n = len(row)
            for i in range(n-1):
                if row[i:i+2] not in mapping:
                    memo[row] = False
                    return False

            def helper(i,cur):
                if i == n-1:
                    return dfs(cur)
                
                pair = row[i:i+2]
                for com in mapping.get(pair,[]):
                    if helper(i+1,cur+com):
                        return True
                return False

            memo[row] = helper(0,"")
            return memo[row]
        
        return dfs(bottom)

