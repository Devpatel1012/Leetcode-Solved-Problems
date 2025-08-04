class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n, m = len(board), len(board[0])

        def backtrack(i, j, index):
            if index == len(word):
                return True

          
            if i < 0 or j < 0 or i >= n or j >= m or board[i][j] != word[index]:
                return False

            temp = board[i][j]
            board[i][j] = "#"

            found = (backtrack(i+1, j, index+1) or
                     backtrack(i-1, j, index+1) or
                     backtrack(i, j+1, index+1) or
                     backtrack(i, j-1, index+1))

            board[i][j] = temp

            return found

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True

        return False
