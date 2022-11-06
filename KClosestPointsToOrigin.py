class Solution:
    def euc(self, x: int, y: int):
        return math.sqrt(pow(x,2)+pow(y,2))
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sol = []
        heapq.heapify(sol)
        for point in points:
            heapq.heappush(sol, (self.euc(point[0],point[1]), point[0], point[1]))
        
        a = []
        for _ in range(k):
            tmp = heapq.heappop(sol)
            a.append([tmp[1],tmp[2]])
        return a