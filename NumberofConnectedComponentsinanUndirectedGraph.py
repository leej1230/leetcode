class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [x for x in range(n)]
        rank = [1 for _ in range(n)]
        answer = n
        for edge in edges:
            # Always be A < B
            A = edge[0]
            B = edge[1]
            while A != parents[A]:
                A = parents[A]
            while B != parents[B]:
                B = parents[B]
            if A==B:
                continue
            answer -= 1
            if rank[A] < rank[B]:
                parents[A] = B
                rank[B] += rank[A]
            else:
                parents[B] = A
                rank[A] += rank[B]
        return answer
        '''
        General Idea
            Union Find
                Each node will have parents, and keep update by looking at edge
                Rules:
                    - Let there be array parent
                      Initially parent of all nodes are itself
                    - Let there be a rank array
                      Represents how many children the parent has including itself
                      i.e.) if there is [0,1] edge then the rank is [2,1]
                    - Connect the parents to merge two graphs
                    - Connect so that parents with more children will be a new parent
        '''