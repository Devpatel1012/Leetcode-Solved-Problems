class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word [j + 1:]
                nei [pattern].append(word)
        visit = set([beginWord])
        q = deque ([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len (word)):
                    pattern = word[:j] + "*" + word [j + 1:]
                    for neiword in nei [pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            res += 1
        return 0
                