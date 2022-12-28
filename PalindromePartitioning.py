class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def checkPal(given):
            # Check if given is palindrome or not
            if len(given)==1:
                return True
            l,r = 0,len(given)-1
            while l<r:
                if given[l] != given[r]:
                    return False
                l += 1
                r -= 1
            return True

        
        answer = []
        def recursivePar(ind,q):
            if ind == len(s):
                nonlocal answer
                answer.append(q.copy())
                return
            
            for i in range(ind,len(s)):
                partition = s[ind:i+1]
                if checkPal(partition):
                    q.append(partition)
                    recursivePar(i+1, q)
                    q.pop()
        
        recursivePar(0, [])
        return answer
        
        '''
        General Idea
        - Since it is looking for substring, we need to go through
          all possilble patterns to partition the string, and backtrack
          is good method to approach that
        - Because each partitions must be palindrome, we can end the
          partitioning process whenever partitioned string is NOT palindrome
        - In a recurisive function, call with the string partitioned and NOT
          partitioned, send the string to palindrome checker, if checker
          returns true, add the partitioned string to array and continue,
          in base case (given index is equal to len) add the array to answer
          array
        '''