class TriNode:
    def __init__(self):
        self.children = {}
        self.word  = None

class Solution(object):
    def findWords(self, board, words):
        root = TriNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TriNode()
                node = node.children[char]
            node.word = word
        rows, cols = len(board), len(board[0])
        result = []

        def dfs (r,c,node):
            char = board[r][c]
            curr = node.children[char]

            if curr.word:
                result.append(curr.word)
                curr.word = None
            
            board[r][c] = "#"

            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] in curr.children:
                    dfs(nr,nc,curr)

            board[r][c] = char

            if not curr.children:
                node.children.pop(char)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r,c,root)
        
        return result


#         rows, cols = len(board), len(board[0])
#         res = set()   # use set to avoid duplicates

#         def dfs(r, c, word, i, visited):
#             if i == len(word):
#                 return True
#             if (r < 0 or c < 0 or r >= rows or c >= cols or
#                 (r, c) in visited or board[r][c] != word[i]):
#                 return False

#             visited.add((r, c))
#             found = (dfs(r+1, c, word, i+1, visited) or
#                      dfs(r-1, c, word, i+1, visited) or
#                      dfs(r, c+1, word, i+1, visited) or
#                      dfs(r, c-1, word, i+1, visited))
#             visited.remove((r, c))
#             return found

#         # check each word individually
#         for word in words:
#             for r in range(rows):
#                 for c in range(cols):
#                     if dfs(r, c, word, 0, set()):
#                         res.add(word)

#         return list(res)


