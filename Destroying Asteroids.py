class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        for i in range (len(asteroids)):
            if mass<asteroids[i]:
                return False
            mass+=asteroids[i]
        
        return True
            
        