class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            map[course].append(prereq)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if map[course] == []:
                return True
            
            visiting.add(course)
            for pre in map[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            map[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True