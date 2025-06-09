import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # Total number of moves required is (m-1) down moves + (n-1) right moves
        # total_moves = (m - 1) + (n - 1)
        
        # # The number of down moves (or right moves) we need to choose positions for
        # # We can choose the smaller of the two to minimize calculation
        # k_moves = min(m - 1, n - 1) 
        
        # # Calculate C(total_moves, k_moves)
        # # Using math.comb (Python 3.8+) is the most straightforward way
        # return math.comb(total_moves, k_moves)

    # If math.comb is not allowed or for older Python versions, 
    # we can implement combinations manually to avoid large factorials:
    # def uniquePaths_manual_comb(self, m: int, n: int) -> int:
        N = (m - 1) + (n - 1)
        K = min(m - 1, n - 1)
        
        result = 1
        # Calculate N * (N-1) * ... * (N-K+1) / (K * (K-1) * ... * 1)
        for i in range(K):
            result = result * (N - i) // (i + 1)
        return result