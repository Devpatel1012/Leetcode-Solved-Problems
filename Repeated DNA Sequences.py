# class Solution(object):
#     def findRepeatedDnaSequences(self, s):
#         if len(s) < 10:
#             return []
        
#         hashmap = {}
#         result = []
        
#         for i in range(len(s) - 9):
#             substring = s[i:i+10]
#             hashmap[substring] = hashmap.get(substring, 0) + 1
        
#         for key, value in hashmap.items():
#             if value > 1:
#                 result.append(key)
        
#         return result
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        
        seen = set()
        repeated = set()
        
        for i in range(len(s) - 9):
            substring = s[i:i+10]
            if substring in seen:
                repeated.add(substring)
            else:
                seen.add(substring)
        
        return list(repeated)
