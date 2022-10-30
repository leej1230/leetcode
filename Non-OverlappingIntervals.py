class Solution:        
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        intervals.sort(key = lambda x:(x[0],x[1]))
        # print(intervals)
        mp = defaultdict(list)
        for a,b in intervals:
            mp[a].append(b)
        head = list(mp)[0]
        # print(list(mp)[0])
        goal = mp[list(mp)[-1]][-1]
        # print(mp[list(mp)[-1]][-1])
        
        self.ans = 0
        def dfs(head):
            nx = mp[head]
            l = len(nx)
            v = False
            for num in nx:
                if(num == goal):
                    self.ans += (l - 1)
                    return True
                if(dfs(num)):
                    # print(head)
                    v = True
                    break
            if(v):
                # print(head, nx)
                self.ans += (l - 1)
                return True
            else:
                self.ans += l
                return False
        dfs(head)
        return self.ans
        '''
        ans = 0
        intervals.sort(key=lambda x:(x[0],x[1]))
        prev = intervals[0]
        for interval in intervals[1:]:
            if(prev[1]>interval[0]):
                # Overlapping Condition
                if(prev[1] < interval[1]):
                    # Deleting current interval value
                    ans += 1
                else:
                    prev = interval
                    ans += 1
            else:
                prev = interval
        return ans