import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create an adjacency list representation of the graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Initialize distances to all nodes as infinity except for the source node
        distances = [float("inf")] * (n + 1)
        distances[k] = 0

        # Priority queue to select the next node to visit based on the minimum distance
        pq = [(0, k)]

        while pq:
            distance, node = heapq.heappop(pq)
            if distance > distances[node]:
                continue
            for neighbor, weight in graph[node]:
                if distance + weight < distances[neighbor]:
                    distances[neighbor] = distance + weight
                    heapq.heappush(pq, (distances[neighbor], neighbor))

        # Find the maximum distance among all nodes
        max_distance = max(distances[1:])

        return max_distance if max_distance < float("inf") else -1