class Solution(object):
    def twoEditWords(self, queries, dictionary):
        ans = []
        
        for currq in queries:  
            for currl in dictionary:
                diff = 0
                for m in range(len(currl)):
                    if currl[m] != currq[m]:
                        diff += 1
                        if diff > 2:
                            break
                if diff <= 2:
                    ans.append(currq)
                    break  
        
        return ans