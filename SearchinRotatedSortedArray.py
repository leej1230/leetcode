class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # See if target is smaller or bigger or equal with nums[0]
        # If target == nums[0]
        origin = 0 
        l = len(nums)
        if target == nums[origin]:
        #   return 0
            return origin
        tmp = origin
        # If nums[0] > target
        if nums[tmp] > target:
            while nums[tmp] > target:
        #   Points must go left side
                tmp -= 1
        #   Keep go left until
        #       len + i == 0 -> return -1
                if l + tmp == origin:
                    return -1
        #       nums[i] == target -> return (len - i)
                if target == nums[tmp]:
                    return ( l + tmp )
        #       nums[i] < target -> return -1
            return -1
        
        # If nums[0] < target
        if nums[origin] < target:
            while nums[tmp] < target:
        #   Keep go right until
                tmp += 1
                if l - tmp == origin:
                        return -1
        #       nums[i] == target -> return i
                if target == nums[tmp]:
                    return ( tmp )
        #       i == len -> return -1
        #   Points must go right side
        #       nums[i] > target -> return -1
            return -1