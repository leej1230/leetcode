class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        balls = [x for x in range(n)]
        for ball in range(n):
            pos = ball
            prev = ball
            for r in range(len(grid)):
                # Check if ball hit the boundary
                prev = pos
                pos += grid[r][prev]
                if not (-1 < pos < n) or grid[r][prev]!=grid[r][pos]:
                    balls[ball] = -1
                    break
                balls[ball] = pos
        
        return balls