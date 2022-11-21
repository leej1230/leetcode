class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        l = len(days)
        dp = [-1] * l
        
        def DPTree(ind):
            if ind >= l:
                return 0
            
            if dp[ind] != -1:
                return dp[ind]
            
            CurrentDate = days[ind]
            
            OL = CurrentDate+1
            tmpInd = ind
            while tmpInd < l and days[tmpInd] < OL:
                tmpInd += 1
            ODP = DPTree(tmpInd) + costs[0]
            
            SL = CurrentDate+7
            while tmpInd < l and days[tmpInd] < SL:
                tmpInd += 1
            SDP = DPTree(tmpInd) + costs[1]
            
            TL = CurrentDate+30
            while tmpInd < l and days[tmpInd] < TL:
                tmpInd += 1
            TDP = DPTree(tmpInd) + costs[2]
            
            dp[ind] = min(ODP, SDP, TDP)
            return dp[ind]

        return DPTree(0)
        '''
        l = len(days)
        Make hashmap
            length of array with length of l
            value will be the minimum on that day

        function DPTree(ind)
            Check if hashmap has ind
                True -> return value for it
            
            Check index is out of range
                True -> 0

            currentDate = days[ind]
            OL = currentDate+1
            tmpInd = ind
            while days[tmpInd] < OL increase tmpInd by 1
            ODP = DPTree(tmpInd) + cost[0]

            SL = currentDate+7
            tmpInd = ind
            while days[tmpInd] < SL increase tmpInd by 1
            ODP = DPTree(tmpInd) + cost[1]

            TL = currentDate+30
            tmpInd = ind
            while days[tmpInd] < TL increase tmpInd by 1
            ODP = DPTree(tmpInd) + cost[2]

            dp[keyForHM] = min(ODP, SDP, TDP)

            return dp[keyForHM]

        '''