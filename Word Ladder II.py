from collections import defaultdict, deque

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # Edge cases
        if beginWord == endWord:
            return [[beginWord]]
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        L = len(beginWord)  # all words are same length in problem

        # Build pattern -> words map (wildcard adjacency)
        # ensure beginWord included in pool for adjacency construction
        pool = set(wordList)
        pool.add(beginWord)

        patterns = defaultdict(list)
        for word in pool:
            for i in range(L):
                pattern = word[:i] + '*' + word[i+1:]
                patterns[pattern].append(word)

        # BFS to build parent links for shortest paths
        parents = defaultdict(list)  # child_word -> list of parent_words
        # standard BFS but we keep levelVisited to avoid cutting off multiple parents on same level
        queue = deque([beginWord])
        visited = set([beginWord])
        found = False

        while queue and not found:
            level_size = len(queue)
            levelVisited = set()
            for _ in range(level_size):
                word = queue.popleft()
                # visit neighbors via patterns
                for i in range(L):
                    pattern = word[:i] + '*' + word[i+1:]
                    for nei in patterns.get(pattern, []):
                        if nei == word:
                            continue
                        # If neighbor not globally visited yet, it's reachable on next level
                        if nei not in visited:
                            # record parent (word -> nei)
                            parents[nei].append(word)
                            if nei not in levelVisited:
                                levelVisited.add(nei)
                                queue.append(nei)
                            # if we reached endWord, mark found so we stop after finishing this level
                            if nei == endWord:
                                found = True
                        # if nei already visited in previous levels, we ignore it (we only want shortest paths)
            # after processing this BFS level, commit levelVisited to visited
            visited |= levelVisited

        if not found:
            return []

        # Backtrack all paths from endWord to beginWord using parents
        res = []
        path = [endWord]

        def backtrack(word):
            if word == beginWord:
                res.append(path[::-1])  # reverse to get begin->...->end
                return
            for p in parents[word]:
                path.append(p)
                backtrack(p)
                path.pop()

        backtrack(endWord)
        return res
