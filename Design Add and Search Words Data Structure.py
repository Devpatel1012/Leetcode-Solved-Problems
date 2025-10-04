# class WordDictionary(object):

#     def __init__(self):
#         self.words = []

#     def addWord(self, word):
#         """
#         :type word: str
#         :rtype: None
#         """
#         self.words.append(word)

#     def search(self, word):
#         """
#         :type word: str
#         :rtype: bool
#         """
#         for w in self.words:
#             if len(w) == len(word):
#                 ok = True
#                 for i in range(len(word)):
#                     if word[i] != "." and word[i] != w[i]:
#                         ok = False
#                         break
#                 if ok:
#                     return True
#         return False


class TriNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary(object):
    def __init__(self):
        self.root = TriNode()
    
    def addWord(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TriNode()
            node = node.children[char]
        node.endOfWord = True

    def search(self, word):

        def dfs(node,i):
            if i == len(word):
                return node.endOfWord

            char = word[i]
            if char == '.':
                for child in word.children.values():
                    if dfs(child,i+1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char],i+1)
        
        return dfs(self.root,0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)