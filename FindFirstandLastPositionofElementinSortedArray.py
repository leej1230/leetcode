class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        if not (nums[0] <= target and target <= nums[l-1]):
            return [-1,-1]

        def find_first(arr: List[int], target: int, root: int) -> int:
            i = root
            if arr[root] == target:
                while i > -1 and arr[i] == target:
                    i -= 1
                return i+1
            elif arr[root] < target:
                while i < l and arr[i] < target:
                    i += 1
                if i==l:
                    return -1
                if arr[i]==target:
                    return i
                return -1
            elif arr[root] > target:
                while i > -1 and arr[i] >= target :
                    i -= 1
                if arr[i+1] == target:
                    return i+1
                return -1
        
        leftmost = find_first(nums, target, int(l/2))
        if leftmost == -1:
            return [-1,-1]
        rightmost = leftmost
        while rightmost < l and nums[rightmost] == target:
            rightmost += 1
        return [leftmost, rightmost-1]