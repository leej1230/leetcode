class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        min_sub = 1000001
        for i in range(1,len(arr)):
            min_sub = min(min_sub, abs(arr[i] - arr[i-1]))
        ans = []
        for i in range(1,len(arr)):
            if abs(arr[i] - arr[i-1]) == min_sub:
                ans.append([arr[i-1],arr[i]])
        return ans
        #get arr[-1] - arr[-2]
        #Iterate through array from 1 to n
        #When subtraction of [i]-[i-1] == min abs diff then add to array