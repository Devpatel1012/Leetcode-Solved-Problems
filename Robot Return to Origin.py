class Solution(object):
    def judgeCircle(self, moves):
        ud = 0
        rl = 0
        for i in moves:
            if i == 'R':
                rl +=1
            elif i == 'U':
                ud += 1
            elif i == 'L':
                rl -= 1
            else:
                ud -= 1
        return True if (ud == rl == 0) else False