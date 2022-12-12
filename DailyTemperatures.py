class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pastTemperatures = collections.deque()
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            currentTemperature = temperatures[i]

            while pastTemperatures and temperatures[pastTemperatures[-1]] < currentTemperature:
                prevTemperature = pastTemperatures.pop()
                answer[prevTemperature] = i-prevTemperature
            pastTemperatures.append(i)
        
        return answer
        '''
        use the temperatures as stack
        make new stack to keep past temperatures
        answer array (deq)

        while temperature is not empty
            pop from temperature
            day = 0
            tmp = pasttemperature
            while past temperature stack is not empty
                add 1 to day
                if popped temperature has higher temperature than current one
                    isExist will be true
                    and break
            if isExist is true
                add day to the answer
            else
                add 0
            
            pasttemperature = tmp
            add current temperature to past temperature
            
        return answer
        '''