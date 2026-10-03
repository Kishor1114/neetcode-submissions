from typing import List
from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = [[False] * 26 for _ in range(26)]
        seen = [False] * 26

        for word in words:
            for c in word:
                seen[ord(c) - ord('a')] = True

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            found = False

            for j in range(min_len):
                if w1[j] != w2[j]:
                    u = ord(w1[j]) - ord('a')
                    v = ord(w2[j]) - ord('a')
                    graph[u][v] = True
                    found = True
                    break

            if not found and len(w1) > len(w2):
                return ""

        in_degree = [0] * 26

        for i in range(26):
            for j in range(26):
                if graph[i][j]:
                    in_degree[j] += 1

        queue = deque()

        for i in range(26):
            if seen[i] and in_degree[i] == 0:
                queue.append(i)

        result = []

        while queue:
            u = queue.popleft()
            result.append(chr(u + ord('a')))

            for v in range(26):
                if graph[u][v]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)

        count = sum(seen)

        return "" if len(result) != count else "".join(result)
