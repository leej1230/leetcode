class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        solutions = []

        cols = set()
        posDiag = set()
        negDiag = set()
        positions = set()
        def backtrack(q):
            # Base Case
            if q == n:
                tmp = [["." for _ in range(n)] for _ in range(n)]
                for position in positions:
                    tmp[position[0]][position[1]] = "Q"

                answer = []
                for row in tmp:
                    answer.append("".join(row))
                solutions.append(answer)
                return

            for i in range(n):
                if i in cols or (q+i) in posDiag or (q-i) in negDiag:
                    continue
                cols.add(i)
                posDiag.add(q+i)
                negDiag.add(q-i)
                positions.add((i,q))
                backtrack(q+1)
                cols.remove(i)
                posDiag.remove(q+i)
                negDiag.remove(q-i)
                positions.remove((i,q))
            return
        backtrack(0)
        
        return solutions
