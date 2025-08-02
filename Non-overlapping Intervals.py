class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        removeCount = 0
        intervals.sort(key=lambda x: x[1])
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < prev_end:
                # Overlap found, increment count
                removeCount += 1
            else:
                # No overlap, update end marker
                prev_end = end

        return removeCount


# class Solution(object):
#     def eraseOverlapIntervals(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: int
#         """
#         if not intervals:
#             return 0

#         # Sort by the end time
#         intervals.sort(key=lambda x: x[1])
#         count = 0
#         prev_end = intervals[0][1]

#         for i in range(1, len(intervals)):
#             start, end = intervals[i]

#             if start < prev_end:
#                 # Overlap found, increment count
#                 count += 1
#             else:
#                 # No overlap, update end marker
#                 prev_end = end

#         return count
