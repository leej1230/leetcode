class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Make Graph
        graph = defaultdict(list)
        inputPath = {}
        courses = set()
        for course in prerequisites:
            courses.add(course[0])
            courses.add(course[1])
            graph[course[1]].append(course[0])
            if course[0] not in inputPath:
                inputPath[course[0]] = 1
            else:
                inputPath[course[0]] += 1
            if course[1] not in inputPath:
                inputPath[course[1]] = 0
        
        queue = collections.deque()
        for c,n in inputPath.items():
            if n==0:
                queue.append(c)
        if queue == []:
            return False
        
        while queue:
            curCourse = queue.popleft()
            courses.remove(curCourse)
            for nextCourse in graph[curCourse]:
                # We are going to cut the edge between current course and next course
                inputPath[nextCourse] -= 1
                if inputPath[nextCourse] == 0:
                    queue.append(nextCourse)
                
        return False if courses else True

        '''
        General Idea
            Use topological sort: from the graph of prereq -> course
        '''