from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    in_degree[word2[j]] += 1
                    break

        queue = deque(char for char, indeg in in_degree.items() if indeg == 0)
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) < len(in_degree):
            return ""
        return "".join(result)