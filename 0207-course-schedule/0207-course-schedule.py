class Solution:
    def canFinish(self, numCourses, prerequisites):
        
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)

        visit = [0] * numCourses

        def dfs(course):
            if visit[course] == 1:   
                return False
            if visit[course] == 2:   
                return True

            visit[course] = 1  

            for nei in graph[course]:
                if not dfs(nei):
                    return False

            visit[course] = 2  
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True