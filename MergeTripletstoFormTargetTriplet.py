class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        lowerTriplets = []
        for triplet in triplets:
            for i, v in enumerate(triplet):
                if v > target[i]:
                    break
                if i==2:
                    lowerTriplets.append(triplet)
                    
        mergedTriplet = [-1,-1,-1]
        
        for triplet in lowerTriplets:
            for i, v in enumerate(triplet):
                mergedTriplet[i] = max(mergedTriplet[i], v)
        
        return mergedTriplet == target
        '''
        Notice how when we combine the triplets, we are having every elements' maximum.
            This means that if there is a number that is bigger than target elements, then there will be no case where we will reach the maximum
        
        reject all the triplets that has higher value than target and merge everything

        compare with target
        '''