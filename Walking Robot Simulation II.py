class Robot(object):

    TDir = {
        0:'East',1:'North',2:'West',3:'South'
    }

    def __init__(self, width, height):
        self.moved = False
        self.idx = 0
        self.pos = list()
        self.dirs = list() 

        pos_ , dir_ = self.pos,self.dirs

        for i in range(width):
            pos_.append((i,0))
            dir_.append(0)
        for i in range(1,height):
            pos_.append((width-1,i))
            dir_.append(1)
        for i in range(width-2,-1,-1):
            pos_.append((i,height-1))
            dir_.append(2)
        for i in range(height-2,0,-1):
            pos_.append((0,i))
            dir_.append(3)
        
        dir_[0] = 3

    def step(self, num):
        self.moved = True
        self.idx = (self.idx + num)% len(self.pos)

    def getPos(self):
        return list(self.pos[self.idx])

    def getDir(self):
        if not self.moved:
            return "East"
        return Robot.TDir[self.dirs[self.idx]]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()