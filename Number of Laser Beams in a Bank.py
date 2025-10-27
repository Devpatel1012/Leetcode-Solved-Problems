class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        # # Step 1: Count '1's in each row
        # device_count = [row.count('1') for row in bank if row.count('1') > 0]
        
        # # Step 2: Calculate beams between consecutive active rows
        # total = 0
        # for i in range(1, len(device_count)):
        #     total += device_count[i - 1] * device_count[i]
        
        # return total
       
        prev = 0
        total = 0
        for row in bank:
            num = row.count("1")
            if "1" not in row:
                continue
            total += prev * num
            prev = num
        
        return total
        