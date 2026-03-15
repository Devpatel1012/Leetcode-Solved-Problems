class Fancy:
    def __init__(self):
        self.seq = []
        self.MOD = 10**9 + 7
        self.mult = 1
        self.add = 0

    def append(self, val):
        inv_mult = pow(self.mult, self.MOD - 2, self.MOD)
        stored = (val - self.add) * inv_mult % self.MOD
        self.seq.append(stored)

    def addAll(self, inc):
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m):
        self.mult = self.mult * m % self.MOD
        self.add = self.add * m % self.MOD

    def getIndex(self, idx):
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mult + self.add) % self.MOD