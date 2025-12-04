class Solution:
    def countCollisions(self, directions: str) -> int:
        # sol 1
        ans = 0
        stack = []

        for i in directions:
            while stack and stack[-1] == 'R' and i == 'L':
                ans += 2
                stack.pop()
                i = 'S'
            
            while stack and stack[-1] == 'R' and i == 'S':
                ans+=1
                stack.pop()

            
            while stack and stack[-1] == 'S' and i == 'L':
                ans+=1
                i = 'S'

            stack.append(i)
        return ans

        # sol 2
        directions = directions.lstrip('L')
        directions = directions.rstrip('R')
    
        ans = 0
        for i in directions:
            if i != 'S' :
                ans+=1
            
        return ans