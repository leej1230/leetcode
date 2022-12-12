class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = (collections.deque(list(t)) for t in zip(*sorted(zip(position, speed))))

        timeTaken = collections.deque()
        for i in range(len(position)-1, -1, -1):
            goalTime = (target - position[i]) / speed[i]
            if timeTaken and timeTaken[-1] >= goalTime:
                pass
            else:
                timeTaken.append(goalTime)
        return len(timeTaken)