class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_list = collections.defaultdict(set)
        wordList.append(beginWord)

        def differences(word1,word2):
            dif_count = 0

            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    dif_count += 1
            return dif_count

        for i in range(len(wordList)):
            for j in range(i+1,len(wordList)):
                if differences(wordList[i], wordList[j]) <= 1:
                    adj_list[wordList[i]].add(wordList[j])
                    adj_list[wordList[j]].add(wordList[i])

        # print(adj_list)
        if endWord not in adj_list: return 0

        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            for neighbor in adj_list[word]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, length + 1))
        return 0
    