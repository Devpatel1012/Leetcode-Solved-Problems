# class Solution(object):
#     def getSkyline(self, buildings):
#         """
#         :type buildings: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         if not buildings:
#             return []

#         res = [[buildings[0][0],buildings[0][2]]]
#         l,r,h = buildings[0][0], buildings[0][1], buildings[0][2]

#         for i in range(1,len(buildings)):
#             if h == buildings[i][2]:
#                 r = max(r,buildings[i][1])
#                 l = buildings[i][0]
#                 continue
#             else:
#                 if h < buildings[i][2]:
#                     res.append([buildings[i][0],buildings[i][2]])
#                     if r < buildings[i][1]:
#                         l,r,h = buildings[i][0], buildings[i][1], buildings[i][2]
#                     else:
#                         l,h =  buildings[i][0], buildings[i][2]
#                         r = max(r,buildings[i][1])
                
#                 else:
#                     if r >= buildings[i][0]:
#                         res.append([r,buildings[i][2]])
#                         l,r,h = buildings[i][0], buildings[i][1], buildings[i][2]
#                     else:
#                         res.append([r,0])
#                         l,r,h = buildings[i][0], buildings[i][1], buildings[i][2]
#                         res.append([buildings[i][0],buildings[i][2]])

#         return res


import heapq

class Solution:
    def getSkyline(self, buildings):
        events = []
        for L, R, H in buildings:
            events.append((L, -H))  # building start
            events.append((R, H))   # building end

        
        # Sort events: by x; if tie, start before end
        events.sort(key=lambda x: (x[0], x[1]))
        print(events)

        result = []
        heap = [0]   # current active heights
        prev_max = 0
        height_count = {0: 1}  # to keep track of height frequencies

        for x, h in events:
            if h < 0:  # start of building
                heapq.heappush(heap, h)
                height_count[-h] = height_count.get(-h, 0) + 1
            else:      # end of building
                height_count[h] -= 1
                if height_count[h] == 0:
                    del height_count[h]

                # lazy removal from heap
                while heap and -heap[0] not in height_count:
                    heapq.heappop(heap)

            current_max = -heap[0]
            if current_max != prev_max:
                result.append([x, current_max])
                prev_max = current_max

        return result





        


        