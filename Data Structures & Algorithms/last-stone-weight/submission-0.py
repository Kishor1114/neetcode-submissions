import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]  # Use negative values for max-heap

        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)  # Extract the largest stone
            y = -heapq.heappop(max_heap)  # Extract the second largest stone

            if x != y:
                heapq.heappush(max_heap, -(x - y))  # Push the remaining weight

        return -max_heap[0] if max_heap else 0