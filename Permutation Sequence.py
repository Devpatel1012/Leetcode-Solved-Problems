class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # nList = [i + 1 for i in range(n)]
        # factorial = 1
        # for i in range(2, n + 1): factorial *= i
        # groupSize = factorial // n
        # group = (k // groupSize) + 1
        # nList[0],nList[group-1] = nList[group-1],nList[0]
        # nList[1:] = sorted(nList[1:])
        # print(nList)
        # print(groupSize)
        # print(group)
        # permutation = (k-(groupSize*(group-1)))
        # print(permutation)
        # if permutation == 1:
        #     result =  "".join(str(x) for x in nList)
        #     return result
        # else:
        #     for i in range(permutation-1):
        #         i = n - 2
        #         while i >= 0 and nList[i] >= nList[i + 1]:
        #             i -= 1

        #         if i >= 0:
                
        #             j = n - 1
        #             while j > i and nList[j] <= nList[i]:
        #                 j -= 1
                    
        #             nList[i], nList[j] = nList[j], nList[i]

                
        #         def reverse_subarray(arr, start, end):
        #             while start < end:
        #                 arr[start], arr[end] = arr[end], arr[start]
        #                 start += 1
        #                 end -= 1

        #         reverse_subarray(nList, i + 1, n - 1)
        #         print(nList)
        #     result =  "".join(str(x) for x in nList)
        #     return result
        
        nums = [str(i) for i in range(1, n + 1)]
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i

        k -= 1  # convert to 0-based index
        result = ""
        for i in range(n, 0, -1):
            idx = k // factorial[i - 1]
            result += nums.pop(idx)
            k %= factorial[i - 1]

        return result


        



        