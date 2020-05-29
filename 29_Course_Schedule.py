class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = collections.defaultdict(list)
        
        for courses in prerequisites:
            d[courses[1]].append(courses[0])
            
        path = [False]*numCourses
        
        for course in range(numCourses):
            if self.isCyclic(course, d, path):
                return False
        return True
    
    def isCyclic(self, course, d, path):
        
        # If we have encountered the course before, cycle exists
        if path[course]:
            return True
        path[course] = True
        
        return_val = False
        
        for child in d[course]:
            return_val = self.isCyclic(child, d, path)
            if return_val:
                break
        
        path[course] = False
        return return_val