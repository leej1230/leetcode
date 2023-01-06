class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        intervals.reverse()
        answer = [intervals.pop()]

        while intervals:
            curr = intervals.pop()
            if answer[-1][1] < curr[0]:
                answer.append(curr)
            else:
                answer[-1][1] = max(curr[1], answer[-1][1])
        return answer