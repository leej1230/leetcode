class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow
        '''
        Approach 1, using hashmap -> memory space will be O(n)
        hm = set()
        for A in nums:
            if A in hm:
                return A
            hm.add(A)

        Approach 2, using fast and slow pointer -> O(1) memory space
        By using Floyd's algorithm, we can find the node that is separated from cycling start node
        by certain distance. This distance is same as distance between cycling start node and head
        of the node.
        Run Fast and Slow algorithm once and find overlap node
        Run one more Slow from head and find another overlap node
        This node will be a cycling start node (node that came from two different node = duplicating)
        '''