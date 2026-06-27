class Solution(object):
    def maximumLength(self, nums):
        seen=set([1])
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        res = 1
        if 1 in freq:
            res = max(1, freq[1] - (freq[1] % 2 == 0))
        for num in freq:
            if num not in seen and freq[num]>=2:
                seen.add(num)
                current=2
                seed=num**2
                while seed in freq :
                    if freq[seed]>=2:
                        current+=2
                        seed=seed**2
                        continue
                    elif freq[seed]==1:
                        current+=1
                        break
                if current%2==0: current-=1
                if current>res: res=current
        return res
        