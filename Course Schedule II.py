class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
            # Build adjacency list + indegree array
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        
        res = []

        # Start with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited = 0

        while queue:
            curr = queue.popleft()
            res.append(curr)
            visited += 1
            

            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        
        return res if visited == numCourses else []
