class TimeMap:

    def __init__(self):
        self.timeStampMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeStampMap:
            self.timeStampMap[key].append((timestamp, value))
        else:
            self.timeStampMap[key] = [(timestamp, value)]
        '''
        See if key is in timeStampMap
            if not -> initialize with [(timestamp, value)]
            if exist -> append (timestamp, value)
        '''

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeStampMap:
            return ""
        arr = self.timeStampMap[key]
        left, right = 0, len(arr)-1
        if timestamp >= arr[right][0]:
            return arr[right][1]
        if timestamp < arr[left][0]:
            return ""
        
        while left <= right:
            middle = (left+right)//2
            if arr[middle][0] == timestamp:
                return arr[middle][1]

            if arr[middle][0] < timestamp:
                left = middle + 1
            else:
                right = middle - 1

        if arr[left][0] == timestamp:
            return arr[left][1]
        if arr[right][0] == timestamp:
            return arr[right][1]

        if arr[left][0] > timestamp:
            return arr[right][1]

        return arr[left][1]
        '''
        Retrieve the array from self.timeStampMap
            If there is no array return ""
        initialize left and right with 0 and len(arr)-1
        if timestamp >= arr[right][0] then return arr[right][1]
        if timestamp <= arr[left][0] then return ""

        do binary search until you find a maximum timestamp from array that is smaller than given timestamp
        return the value
        '''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)