class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # if n<k:
        #     return []
        # res = []
        # def backtrack(arr,num):
        #     if sum(arr) == n:
        #         return res.append(arr)
        #     for i in range(1,10):
        #         arr.append(num)
        #         backtrack(arr,num+1)
        #         arr.pop()


        # backtrack([],0)
        # return res
        res = []

        def backtrack(start,path,target):
            if len(path) == k and target == 0:
                res.append(path[:])
            if len(path)>k and target != 0:
                return
            for i in range(start,10):
                path.append(i)
                backtrack(i+1,path,target-i)
                path.pop()
        
        backtrack(1,[],n)
        return res