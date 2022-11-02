class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dp = {}
        for num in nums:
            if num in dp:
                dp[num] += 1
            else:
                dp[num] = 1
        ans = []
        minHeap = []
        heapq.heapify(minHeap)
        for key,val in dp.items():
            heapq.heappush(minHeap, (-val, key))
        for i in range(k):
            a = heapq.heappop(minHeap)
            ans.append(a[1])
            #ans.append(max(dp, key=dp.get))
            #dp.pop(ans[i])
        return ans