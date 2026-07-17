class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_reqs = collections.defaultdict(list)
        visited = set()
        valid = set()
        ordering = []

        for course, pre_req in prerequisites:
            pre_reqs[course].append(pre_req)

        def dfs(course):
            if course in valid:
                return True
            if course not in pre_reqs:
                valid.add(course)
                ordering.append(course)
                return True
            if course in visited:
                return course in valid

            visited.add(course)
            for pre_req in pre_reqs[course]:
                if not dfs(pre_req):
                    return False

            valid.add(course)
            ordering.append(course)
            return True

        for course in range(numCourses):
            if course not in visited:
                dfs(course)
        
        if len(valid) == numCourses: return ordering
        else: return []