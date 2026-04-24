class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        left = moves.count("L")   
        right = moves.count("R")
        unknown = moves.count("_")
        return abs(left - right) + unknown   
        

class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        ans = float('-inf')
        for i in range(2):
            curr = 0
            if i == 0:             
                for j in moves:
                    if j == 'L' or  j=="_":
                        curr-=1
                    else:
                        curr+=1
            else:
                for j in moves:
                    if j == 'R' or j == '_':
                        curr+=1
                    else:
                        curr-=1
            ans = max(ans,abs(curr))
        return ans

        