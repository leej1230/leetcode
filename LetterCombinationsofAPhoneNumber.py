class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        solution = []
        d = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        l = len(digits)
        def backtrack(ind: int, curr_str: str) -> None:
            if ind == l:
                solution.append(curr_str)
                return
            
            letter_arr = d[digits[ind]]

            for alph in letter_arr:
                curr_str += alph
                backtrack(ind + 1, curr_str)
                curr_str = curr_str[:-1]
            return
        
        backtrack(0, "")
        return solution