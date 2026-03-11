class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0: return 1
        return ~n & (1 << n.bit_length()) - 1

        # a=list(bin(n)[2:])
        # for i in range(len(a)):
        #     if a[i]=='0':
        #        a[i]='1'
        #     else:
        #        a[i]='0'
        # a=''.join(a)
        # return int(a,2)



        