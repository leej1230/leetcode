class Ugly:
    def __init__(self):
        self.nums = nums = [1, ]
        i2 = i3 = i5 = 0

        for i in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)

            if ugly == nums[i2] * 2: 
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1
            
class Solution:
    u = Ugly()
    def nthUglyNumber(self, n):
        return self.u.nums[n - 1]
        '''
        Make a minheap
        Have array of [0,2], [0,3], [0,5]

        initialize answer with 1

        while the count is not equal to n
            pop from heap based on the first element of the array
            add second element to first element
            if first element equals to answer
                first element will be the answer
            else
                increment the count
            push the array into heap again

        --------- solution ----------
        Make everything first in heap -> since we already know that the question will be going to ask 1690th ugly number at most
        '''