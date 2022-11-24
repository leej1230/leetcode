class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        '''
        Sort the given tasks in reverse order

        Add everything into dp key-> worksession | val-> number of session

        ans = 0

        while dp
            add 1 to ans (1 session count)

            ST = sessionTime
            input -1 into PST
            while PST != ST
                copy ST to PST
                iterate through the dp
                    if the key <= ST
                        decrement the count in dp
                        delete from DP if count is 0
                        ST - key
                        break
                    
        return ans
        '''