class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Dict for directional Graph
        #   {Course: [Courses that points to "Course"]}
        DG = {x:[] for x in range(numCourses)}
        

        # For loop through the prerequisites
        #   i and j -> DG[i] = [j] or append(j)
        for prerequisite in prerequisites:
            DG[prerequisite[0]].append(prerequisite[1])

        ans = []
        # While DG
        while DG:
        #   set empty_node = None
            empty_node = None
        #   For loop DG and find the node that is empty
            for key, val in DG.items():
                if val == []:
                    empty_node = key
                    break
        #   If empty_node was left as None -> No class can be taken return []
            if not empty_node:
                return []
        #   Delete empty_node from DG and append to solution
            DG.pop(empty_node)
            ans.append(empty_node)
        #   For loop through DG
            for key,val in DG.items():
                if empty_node in val:
                    val.remove(empty_node)
        #       If there is empty_node in value of key, delete that one

        if len(ans) <= numCourses:
            return ans
        
        return []