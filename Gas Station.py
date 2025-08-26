class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_gas = sum(gas)
        total_cost = sum(cost)

        # If overall gas is less than cost, impossible
        if total_gas < total_cost:
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            # If tank goes negative, can't start from start → move start
            if tank < 0:
                start = i + 1
                tank = 0

        return start
# class Solution(object):
#     def canCompleteCircuit(self, gas, cost):
#         n = len(gas)

#         # Try starting at every station
#         for start in range(n):
#             tank = 0
#             success = True

#             # Try to travel n steps in cycle
#             for i in range(n):
#                 j = (start + i) % n   # wrap around
#                 tank += gas[j] - cost[j]
#                 # print(j ,':' ,tank)
#                 if tank < 0:
#                     success = False
#                     break

#             if success:
#                 return start  # Found valid start

#         return -1  # No solution
