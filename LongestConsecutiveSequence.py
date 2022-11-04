class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        s = set()
        for num in nums:
            s.add(num)
        for num in nums:
            if num-1 not in s: #num is left most seq.
                tmp = 1
                curr = num + 1
                while curr in s:
                    tmp += 1
                    curr += 1
                ans = max(ans, tmp)
        return ans