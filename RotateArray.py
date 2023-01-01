class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

        """
        General Idea
        1. If we rotate n times, it will be same, so only rotate k%n times (works)
            Code:
                rotateNum = k%len(nums)
                for _ in range(rotateNum):
                    nums.insert(0, nums.pop())
            Analysis:
                insert is O(n) in python (pop is O(1))
                In worst case scenario operation will be occured n-1 times
                Which is O((N-1)N) = O(N^2)
                Memory Space O(1)

        2. Optimize version of method 1
           Previously, we reversed by popping from right side and pushing to left side
           If we use deque() AND deciding the optimal direction of push/pop complexity
           can be optimized.
           Method:
                1. Find k%len(nums)
                2. Copy the nums and turn it into deque
                3. IF k is lower than len(nums)/2
                    POP from right
                    PUSH to left
                4. Else
                    k = len(nums)-k
                    POP from left
                    PUSH to right
                5. Copy the processed arr back to nums
            Analysis:
                At most O(n/2) pop/pushed will be processed, and copying will be O(n)
                Therefore O(n) but if we were asked to return the array, average will be O(n/2)
                which is significantly efficient than O(n) for this context
                Memory space O(n), trade-off :(
        
        3. Reversing the array
           Reverse entire array and then reverse nums[:k] and reverse[k:]
            Code:
                k = k%len(nums)
                nums.reverse()
                nums[:k] = reversed(nums[:k])
                nums[k:] = reversed(nums[k:])
            Analysis:
                O(1 + n + k + n-k) = O(n)
                Memory Space O(1)
                Very cool but how can we reach to this solution
                without the idea of reversing arr :(
        """