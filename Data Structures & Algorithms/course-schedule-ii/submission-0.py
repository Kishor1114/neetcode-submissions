class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        order = []

        # Construct the graph and count in-degrees
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Initialize a queue with nodes having in-degree zero
        queue = collections.deque(
            [course for course, degree in enumerate(in_degree) if degree == 0]
        )

        # Perform topological sorting and update in-degrees
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If the order doesn't contain all courses, there's a cycle
        return order if len(order) == numCourses else []