class Solution(object):
    def intersectionSizeTwo(self, intervals):
        # intervals.sort(key=lambda x: (x[1], -x[0]))

        # ans = 0
        # a, b = -1, -1

        # for l, r in intervals:
        #     if l > b:
        #         a = r - 1
        #         b = r
        #         ans += 2
        #     elif l > a:
        #         a = b
        #         b = r
        #         ans += 1

        # return ans
        intervals.sort(key = lambda x:x[1])
        ans = 0 
        curr = []
        for s,e in intervals:
            if not curr or s>curr[1]:
                ans += 2
                curr = [e-1,e]
            elif s>curr[0]:
                ans+=1
                if e == curr[1]:
                    curr = [e-1,e]
                else:
                    curr = [curr[1],e]
        return ans
# class Solution(object):
#     def intersectionSizeTwo(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: int
#         """
#         ans = set()
#         intervals = sorted(intervals,key = lambda x:x[-1])
#         print(intervals)
#         a,b = -1,-1
#         for i,j in enumerate(intervals):
#             boola = True if (a>=j[0] and a<=j[1]) else False
#             boolb = True if (b>=j[0] and b<=j[1]) else False
#             if (boola and boolb):
#                 continue
#             elif(boolb):
#                 ans.add(j[1])
#                 print("adding",a,b, "intervals",j[0],j[1])
#                 a=b
#                 b=j[1]
#             elif(boola):
#                 ans.add(j[1])
#                 a=b
#                 b=j[1]
#             else:
#                 ans.add(j[1]-1)
#                 ans.add(j[1])
#                 a=j[1]-1
#                 b=j[1]
#             if a == b :
#                 a = a-1
#         print(sorted(list(ans)))
#         return len(ans)