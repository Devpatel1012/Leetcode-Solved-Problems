class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0: return 0
        if n == 1: return 1
        if n == 2: return 2

        
        one_step_before = 1 
        
        two_steps_before = 2

        for _ in range(3, n + 1):
            current_ways = one_step_before + two_steps_before
            one_step_before = two_steps_before
            two_steps_before = current_ways
        
        return two_steps_before 