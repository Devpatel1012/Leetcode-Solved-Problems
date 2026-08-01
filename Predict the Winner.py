class Solution(object):
    def predictTheWinner(self, nums):

        def game(left, right, p1, p2, turn):
            if left > right:
                return p1 >= p2

            if turn == 0:
                return (
                    game(left + 1, right, p1 + nums[left], p2, 1) or
                    game(left, right - 1, p1 + nums[right], p2, 1)
                )
            else:
                return (
                    game(left + 1, right, p1, p2 + nums[left], 0) and
                    game(left, right - 1, p1, p2 + nums[right], 0)
                )

        return game(0, len(nums) - 1, 0, 0, 0)
    