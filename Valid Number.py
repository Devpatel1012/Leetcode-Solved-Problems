class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        decimal_used = False
        number_seen = False
        i = 0
        if s[i] in ['+','-']:
            i+=1
        
        while i<len(s):
            cur_char = s[i]
            if cur_char.isalpha():
                if cur_char not in ['e','E']:
                    return False
                else:
                    return number_seen and self.is_valid_interger(s[i+1:])
            elif cur_char == '.':
                if decimal_used:
                    return False
                else:
                    decimal_used =True
            elif cur_char in ['-','+']:
                return False
            else:
                number_seen = True
            i+= 1
        return number_seen
    

    def is_valid_interger(self,s1):
        if not s1:
            return False
        number_seen = False
        i = 0
        if s1[i] in ['+','-']:
            i+=1
        while i <len(s1):
            cur_char = s1[i]
            if not cur_char.isdigit():
                return False
            else:
                number_seen = True
            i+=1
        return number_seen
        
        
        