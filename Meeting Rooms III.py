import heapq

class Solution(object):
    def mostBooked(self, n, m):
        m.sort()
        available = list(range(n))
        heapq.heapify(available)
        
        busy = []
        used = [0] * n

        for start, end in m:
            while busy and busy[0][0] <= start:
                _, room_idx = heapq.heappop(busy)
                heapq.heappush(available, room_idx)

            if available:
                idx = heapq.heappop(available)
                heapq.heappush(busy, [end, idx])
            else:
                earliest_finish, idx = heapq.heappop(busy)
                new_end = earliest_finish + (end - start)
                heapq.heappush(busy, [new_end, idx])
            
            used[idx] += 1
        
        return used.index(max(used))
