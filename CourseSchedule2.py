class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incomingEdge = {}
        for x in range(numCourses):
            incomingEdge[x] = 0
        for courses in prerequisites:
            graph[courses[1]].append(courses[0])
            incomingEdge[courses[0]] += 1

        queue = collections.deque()
        for c,n in incomingEdge.items():
            if n==0:
                queue.append(c)

        answer = []
        while queue:
            curCourse = queue.popleft()
            answer.append(curCourse)
            for course in graph[curCourse]:
                incomingEdge[course] -= 1
                if incomingEdge[course] == 0:
                    queue.append(course)
        
        return answer if len(answer)==numCourses else []
        '''
        General Idea
        Topological sort
            Make the graph of prereq -> course
            keep track of incoming edge for each node as well
            Topological sort method
            1. Get all nodes that has no incoming edge, add to queue
            2. pop from queue append to answer list, let adjacent edges have -1 incoming edge
               count, if becomes zero add to the queue
            3. Repeat #2 until queue becomes empty
            In the end answer list should have equal to numCourses or return empty array
        '''