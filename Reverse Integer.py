class Solution(object):
    def reverse(self, x):
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        if x < INT_MIN or x > INT_MAX:
            return  0
        else:
            ans = 0
            no = x
            if(no>0):
                while (no > 0):

                    remainder = no % 10
                    ans = (ans * 10) + remainder
                    no = no//10
            elif(no<0):
                print("yes i am negative")
                if no < 0:
                    print("yes i am negative2")
                    no *= -1
                while (no > 0):

                    remainder = no % 10
                    ans = (ans * 10) + remainder
                    no = no // 10
                # print("no:{}"+ format(no))

                if ans > 0:
                   ans *= -1

            if ans < INT_MIN or ans > INT_MAX:
                    return 0
            return ans



soul = Solution()
x = 1534236469
print(soul.reverse(x))
