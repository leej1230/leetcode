class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        #last_ind
        dp = {}
        nums.sort()
        num_info = {x:0 for x in nums}
        for x in nums:
            num_info[x] += 1
        for ind, arr in enumerate(num_info.items()):
            if(ind == 0):
                prev_key = arr[0]
                dp[ind] = arr[0] * arr[1]
                last_ind = ind
                continue
            
            if(ind == 1):
                if abs(arr[0] - prev_key) == 1:
                    dp[ind] = max(arr[0]*arr[1], dp[ind-1])
                else:
                    dp[ind] = arr[0]*arr[1] + dp[ind - 1]
                prev_key = arr[0]
                last_ind = ind
                continue

            if abs(arr[0] - prev_key) == 1:
                dp[ind] = max(arr[0]*arr[1]+dp[ind-2], dp[ind-1])
            else:
                dp[ind] = arr[0]*arr[1] + dp[ind - 1]

            prev_key = arr[0]
            last_ind = ind
        return dp[last_ind]