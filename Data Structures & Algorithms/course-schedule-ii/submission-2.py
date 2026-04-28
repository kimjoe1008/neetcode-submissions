class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        prs = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            indegree[course] += 1
            prs[prereq].append(course)
        output = []

        def dfs(course):
            output.append(course)
            indegree[course] -= 1
            for pr in prs[course]:
                indegree[pr] -= 1
                if indegree[pr] == 0:
                    dfs(pr)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
        return output if len(output) == numCourses else []