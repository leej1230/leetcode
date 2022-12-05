class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        sortedHand = sorted(hand)

        dp = {}
        for v in sortedHand:
            dp[v] = dp.get(v, 0) + 1

        while dp:
            lowestVal = list(dp.keys())[0]
            dp[lowestVal] -= 1
            if dp[lowestVal]==0:
                dp.pop(lowestVal)
            for i in range(lowestVal+1, lowestVal+groupSize):
                if i not in dp:
                    return False
                dp[i] -= 1
                if dp[i]==0:
                    dp.pop(i)
        return True
        
        '''
        if the length of hand is not divisible by groupsize then return False

        make array of empty sets, number of len(hand)/groupsize

        handLength = len(hand)
        setMaxLength = handLength / groupsize
        result = False

        def dfs(hInd, arrSet):
            if hInd==handLength:
                return True

            for ind,s in enumerate(arrSet):
                if len(s) == 0:
                    saveArrSet = arrSet.copy()
                    saveArrSet[ind].add(hand[hInd])
                    result = result or dfs(hInd+1, saveArrSet)
                    continue
                
                if (len(s) < setMaxLength) and ((hand[hInd]+1 is in s) or (hand[hInd]-1 is in s)):
                    saveArrSet = arrSet.copy()
                    saveArrSet[ind].add(hand[hInd])
                    result = result or dfs(hInd+1, saveArrSet)
                    continue
            
            return result
        
        return dfs(0,arr)

        ----------------------------------------------

        sort the array

        put into hashmap

        while hashmap:
            see the lowest number
            for in that range
                if number not in the hm:
                    return False
                decrement number by 1, if 0 then delete
        
        return True
        '''