class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_time = [x[0] for x in intervals]
        end_time = [x[1] for x in intervals]
        start_time.sort()
        end_time.sort()

        count = 0
        answer = -1
        i,j = 0,0
        while i < len(intervals) and j < len(intervals):
            if start_time[i] < end_time[j]:
                i += 1
                count += 1
            else:
                j += 1
                count -= 1
            answer = max(answer, count)
        return answer
        '''
        General Idea
            Sort the starting time and ending time individually
            Have two pointers, if starting time pointer is pointing at value less than ending time pointing at
            increment the pointer by 1 and add 1 to the meeting room count
        '''