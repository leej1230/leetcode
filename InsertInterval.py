class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]
        
        answer = []
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                answer.append(newInterval)
                return answer+intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                answer.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
        answer.append(newInterval)
        return answer