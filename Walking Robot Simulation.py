class Solution(object):
    def robotSim(self, comm, obs):
        obs_set = {tuple (o) for o in obs}
        x = y = 0
        d = 0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        max_dist = 0

        for cmd in comm:
            if cmd == -1:
                d=(d+1)%4
            elif cmd == -2:
                d = (d-1)%4
            else:
                dx,dy = dirs[d]
                for _ in range(cmd):
                    if (x+dx,y+dy)in obs_set:
                        break
                    
                    x+=dx
                    y+=dy
            max_dist = max(max_dist,x**2 + y**2)
        return max_dist


