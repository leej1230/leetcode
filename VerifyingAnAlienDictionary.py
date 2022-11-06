class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letters = 1
        alien_dict = {}
        for c in order:
            alien_dict[c] = letters
            letters += 1
        
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]): #Next word is shorter
                    return False
                
                if words[i][j] != words[i+1][j]:
                    if alien_dict[words[i][j]] > alien_dict[words[i+1][j]]:
                        return False
                    break # If the first different letters are sorted, then rest doesn't matter
                
        return True