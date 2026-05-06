class Solution(object):
    def rotateTheBox(self, boxGrid):
        n, m = len(boxGrid), len(boxGrid[0])

        for row in boxGrid:
            empty = m - 1 

            for j in range(m - 1, -1, -1):
                if row[j] == '*':
                    empty = j - 1
                elif row[j] == '#':
                    row[j], row[empty] = '.', '#'
                    empty -= 1

        return list(zip(*boxGrid[::-1]))